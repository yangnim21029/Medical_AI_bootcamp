from __future__ import unicode_literals  #terminal裡面用utf-8
from flask import Flask
from MedicalAssistant.model_qa.textpredict import predicttext, DataDic
from MedicalAssistant.model_skin.skinpredict import predict
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

app = Flask(__name__)

#test
@app.route("/", methods=["GET"])
def predict2():
  
        a = predict("https://img.ltn.com.tw/Upload/3c/page/2019/08/08/190808-37645-1.jpg")
        b = predicttext("123")
        return b

if __name__ == '__main__':
    app.run(debug=True, port=3000)


    