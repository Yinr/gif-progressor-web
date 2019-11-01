#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
from GifProgressor import Progressor

ALLOWED_EXTENSIONS = set(['gif'])
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_ROOT = os.path.relpath(".")
IMG_ROOT = os.path.join(APP_ROOT, 'images')
STATIC_ROOT = os.path.join(APP_ROOT, 'static')
LAYUI_ROOT = os.path.join(STATIC_ROOT, 'layui')

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
    position = request.form['position']
    color = request.form['color']
    width = request.form['width']
    upload = request.files.getlist("file")[0]
    print(upload)

    print("File name: {}".format(upload.filename))
    if not allowed_file(upload.filename):
        error_message = "The selected file is not supported"
        return render_template('index.html',
                               error_message=error_message,
                               color=color,
                               position=position), 400

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

    progressor = Progressor(pos=int(position), color=color, width=int(width))
    progressor.handle(destination)
    if progressor:
        progressor.save(destination)

    filepath = '/images/' + filename

    return {
        "code": 0, "msg": "gif converted.", "data": {
            "src": filepath
        }
    }


@app.route('/images/<filename>')
def download_image(filename):
    return send_from_directory(IMG_ROOT, filename)


@app.route('/assets/<filename>')
def static_file(filename):
    return send_from_directory(STATIC_ROOT, filename)


@app.route('/layui/<path:filepath>')
def layui_file(filepath):
    return send_from_directory(LAYUI_ROOT, filepath)


if __name__ == "__main__":
    app.run()
