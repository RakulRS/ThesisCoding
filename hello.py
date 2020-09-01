#!/home/ubuntu/video_reg/venv/bin/python
import flask
from flask import Flask
from flask_restful import Resource, Api
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import cv2 
import io
from googleapiclient.http import MediaIoBaseDownload
import shutil
import os
import random
import glob
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/api/*')

api = Api(app)
@app.route('/')
def hello_world():
    path='/home/ubuntu/video_reg/output_file/*.txt'
    list_file=glob.glob('{0}'.format(path))
    files = sorted(list_file, key=os.path.getmtime)
    if len(files)>=1:
        newest=files[-1]
        with open (newest) as f:
            data=f.readlines()
        output=random.choice(data)
        return output



if __name__ == '__main__':
    app.run()
    