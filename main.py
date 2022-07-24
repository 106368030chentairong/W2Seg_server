import os, sys

from lib.CkipWordSegmenter import w2seq
from lib.aws_nosql import consql

from flask import Flask, abort, request

app = Flask(__name__)

import re

def drop_punctuation(text):
    punc = '~`!#$%^&*()_+-=|\';"＂:/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》{《}】【\n\]\[ 「」'
    new_text=re.sub(r"[%s]+" %punc, "",text)
    return new_text

@app.route("/api/w2seq", methods=["POST"])
def callback():
    content_type = request.headers.get('Content-Type')
    print(content_type)
    if (content_type == 'application/json'):
        json = request.json
        #sentence = drop_punctuation(json["word"])
        sentence = json["word"]
        sentence = drop_punctuation(sentence)
        sentence = w2seq_mode.run([sentence])
        print(sentence)
        consql().put_word(json["userid"], sentence)
        #print(str(sentence))
        return str(sentence)

@app.route("/api/getnum", methods=["POST"])
def gettopnum():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        num = consql().get_word_num(json["userid"],json["word"])

        return str(num)

if __name__ == '__main__':
    w2seq_mode = w2seq()
    w2seq_mode.setup()
    app.debug = True
    app.run(host= "0.0.0.0" , port=8090)