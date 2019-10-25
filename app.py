#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, send_from_directory
import os
from GifProgressor import Progressor, Position

ACCEPT_EXT = set(['.gif'])
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_ROOT = os.path.relpath(".")
IMG_ROOT = os.path.join(APP_ROOT, 'images')

if not os.path.isdir(IMG_ROOT):
    os.mkdir(IMG_ROOT)

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/", methods=["POST"])
def process():

    # retrieve file from html file-picker
    upload = request.files.getlist("file")[0]
    print("File name: {}".format(upload.filename))
    filename = upload.filename

    # file support verification
    ext = os.path.splitext(filename)[1]
    if ext.lower() in ACCEPT_EXT:
        print("File accepted")
    else:
        return render_template('index.html', error_message='The selected file is not supported'), 400

    # TODO: Rename file
    # save file
    destination = "/".join([IMG_ROOT, filename])
    # print("File saved to to:", destination)
    upload.save(destination)

    progressor = Progressor().setPosition(Position.bottom).setColor((255, 0, 0, 100))
    progressor.handle(destination)
    if progressor:
        progressor.save(destination)

    filepath = '/images/' + filename

    return render_template("index.html", upload_image=filepath)


@app.route('/images/<filename>')
def download_image(filename):
    return send_from_directory(IMG_ROOT, filename)


if __name__ == "__main__":
    app.run()
