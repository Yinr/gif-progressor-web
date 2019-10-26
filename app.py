#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
from flask import Flask, request, render_template, send_from_directory
from werkzeug import secure_filename
from GifProgressor import Progressor, Position

ALLOWED_EXTENSIONS = set(['gif'])
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_ROOT = os.path.relpath(".")
IMG_ROOT = os.path.join(APP_ROOT, 'images')
STATIC_ROOT = os.path.join(APP_ROOT, 'static')

if not os.path.isdir(IMG_ROOT):
    os.mkdir(IMG_ROOT)

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/", methods=["POST"])
def process():

    # retrieve file from html file-picker
    upload = request.files.getlist("file")[0]
    print("File name: {}".format(upload.filename))
    if not allowed_file(upload.filename):
        error_message = "The selected file is not supported"
        return render_template('index.html',
                               error_message=error_message), 400

    secureFilename = secure_filename(upload.filename)
    # TODO: customize secure filename
    if '.' not in secureFilename:
        secureFilename += '.gif'
    filename = str(int(time.time())) + "_" + secureFilename
    print("File accepted as: {}".format(filename))

    # save file
    destination = "/".join([IMG_ROOT, filename])
    # print("File saved to to:", destination)
    upload.save(destination)

    position = request.form['position']
    color = request.form['color']

    progressor = Progressor().setPosition(int(position))
    progressor = progressor.setColor((255, 0, 0, 100))
    progressor.handle(destination)
    if progressor:
        progressor.save(destination)

    filepath = '/images/' + filename

    return render_template("index.html", upload_image=filepath, color=color, position=position)


@app.route('/images/<filename>')
def download_image(filename):
    return send_from_directory(IMG_ROOT, filename)


@app.route('/assets/<filename>')
def static_file(filename):
    return send_from_directory(STATIC_ROOT, filename)


if __name__ == "__main__":
    app.run()
