<img src="https://user-images.githubusercontent.com/40525124/156202791-b9cf65ad-a02d-440c-bece-32e48f4d6147.png" alt="Tibame Logo" width="100"/>

# 醫療助理 
This is the repoitory for the linebot server.

require line-bot developer account <br>
get one here : [line console](https://developers.line.biz/zh-hant/)

model here :
[densenetSkin.pt](https://storage.googleapis.com/tfi101_model/densenetSkin.pt) / 
[model_qa.zip](https://storage.googleapis.com/tfi101_model/model1.zip)

## How to Build / 怎麼把它 Build 起來

To start up the dev server, you will need Python poetry = "^1.1.12"

After poetry installed, run following commands:

    poetry install
    cd tfi101_medicalAssistant/MedicalAssistant/   &&
    poetry run python3 -m flask run --port 5000

Which installs required packages and start the server for you at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## How to Edit / 如何編輯

The folder structure basically follows `g0v factory` dand the location for source files and resource files:

- `MedicalAssistant` - all backend server stuff
  - `model_qa` - source files
    - `model_1` - predict model
  - `model_skin` - predict model
  - `static` - generated file
  - `hos_csv` - resources
  - `templates` - html go here

## How to Deploy / 怎麼發佈更新
fork this

## project slide & sample
[展示影片連結](https://drive.google.com/file/d/163f_oElzQnApxLhG8cyWE3oS8Rxk0Rsw/view?usp=sharing)
