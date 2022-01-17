from model_skin.skinpredict import predict
from flask import Flask

app=Flask(__name__)
@app.route("/static/<imageId>.png", methods=['get'])
def predictskin(imageId):
    output = predict(text)
    return output

if __name__=="__main__":
    app.run(host="0.0.0.0", port="5000")
