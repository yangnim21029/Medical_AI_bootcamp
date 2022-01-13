from __future__ import unicode_literals  #terminal裡面用utf-8

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

from model_qa.textpredict import predicttext, DataDic
from model_skin.skinpredict import predict


@app.route("/", methods=["GET"])
def predict2():

    # a = predict("https://discuss.pytorch.org/uploads/default/original/3X/d/4/d451014c9e1f345fb76c38a00cff527c6c2f4e4a.png")
    b = predicttext("123")
    return b

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1" , port ="3000")