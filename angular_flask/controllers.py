import os
from functools import update_wrapper
from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort, current_app
from datetime import timedelta, datetime

from bson.json_util import dumps

from angular_flask import app


from slugify import slugify
from random import randint

from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec



#
# CORS DECORATOR
#
def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/everblog')
@app.route('/everpost/<guid>')
def basic_pages(**kwargs):
	return make_response(open('angular_flask/templates/index.html').read())





##########
# REST API for Evernote
#
@app.route('/api/evernote', methods = ['GET'])
@crossdomain(origin='*')
def get_ev_notes():
  dev_token = app.config['EN_DEV_TOKEN']
  notestore_url = app.config['EN_NOTESTORE_URL']
  nb_guid = app.config['EN_NB_GUID']
 
  client = EvernoteClient(token=dev_token)
  note_store = client.get_note_store()

  filt = NoteFilter()
  filt.notebookGuid = nb_guid

  spec = NotesMetadataResultSpec()
  spec.includeTitle = True

  notemetalist = note_store.findNotesMetadata(dev_token, filt, 0, 100, spec)
  notes = []
  for note_data in notemetalist.notes:
    note = note_store.getNote(dev_token, note_data.guid, True, True, True, True)

    title = note.title
    author = note.attributes.author
    date = note.updated
    url = note.attributes.sourceURL    
    cont = note.content
    note_tags = []

    tag_guids = note.tagGuids
    if tag_guids is not None:
      for tag_guid in tag_guids:
        tag = note_store.getTag(dev_token, tag_guid)
        note_tags.append({'guid': tag_guid, 'name': tag.name})

    notes.append({'guid': note_data.guid, 'title': title, 'date_modified': date, 'author': author, 'content': cont, 'tags': note_tags})
  
  #print notes
  return dumps(notes)

@app.route('/api/evernote/<guid>', methods = ['GET'])
@crossdomain(origin='*')
def get_ev_note(guid):
  dev_token = app.config['EN_DEV_TOKEN']
 
  client = EvernoteClient(token=dev_token)
  note_store = client.get_note_store()

  note = note_store.getNote(dev_token, guid, True, True, True, True)

  title = note.title
  author = note.attributes.author
  date = note.updated
  url = note.attributes.sourceURL    
  cont = note.content
  note_tags = []

  tag_guids = note.tagGuids
  if tag_guids is not None:
    for tag_guid in tag_guids:
      tag = note_store.getTag(dev_token, tag_guid)
      note_tags.append({'guid': tag_guid, 'name': tag.name})

  return dumps({'guid': guid, 'title': title, 'date_modified': date, 'author': author, 'content': cont, 'tags': note_tags})


######
# Misc
#

# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),
							   'img/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

