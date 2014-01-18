# Everblog = Flask + AngularJS + Bootstrap 
Based on Angular-Flask by Ryan Shea @ ryanshea.org

Part of the credit goes to Postach.io, but mostly just another branch from EverMark chrome app.
The idea is simple: use Evernote as the interface and storage for writing blog post. 
Choose a notebook in your Evernote account dedicated to your blog. Setup settings.py with your evernote developer token, notestore url and the GUID 
of the dedicated notebook. That's it! 

[More work is of course needed to make a production-ready version out of this. Work is ongoing...]

This is how the settings.py should look like:
```
DEBUG = True
SECRET_KEY = '21jh3g4h21jlg49090sfq0ujksdfsejhfls' # make sure to change this

EN_DEV_TOKEN = "[your evernote dev token]"
EN_NOTESTORE_URL = "[notestore url]"
EN_NB_GUID = "[notebook GUID]"
```

### How to Get Started

1. clone this repo

2. install all the necessary packages (best done inside of a virtual environment)
> pip install -r requirements.txt

3. run the app
> python runserver.py

4. Connect to your Evernote by filling in the details in settings.py

5. check out your blog
> http://localhost:5000/everblog

6. if you like this project, give it a star :)
