from skinpredict import predict
from flask import Flask
import request

app=Flask(__name__)
@app.route("<Urlimage>", methods=['get'])
def predictskin(imageId):    
    output = predict(<Urlimage>)
    return output

if __name__=="__main__":
    app.run(host="0.0.0.0", port="5000")
