import os, sys
from lib.CkipWordSegmenter import w2seq

from flask import Flask, abort, request

app = Flask(__name__)


@app.route("/api/w2seq", methods=["POST"])
def callback():
    content_type = request.headers.get('Content-Type')
    print(content_type)
    if (content_type == 'application/json'):
        json = request.json
        return str(socep.run([json["word"]]))

if __name__ == '__main__':
    socep = w2seq()
    socep.setup()
    app.debug = True
    app.run()