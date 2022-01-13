# 醫療助理 
This is the repoitory for the linebot server.

Discuss here: https//

## How to Build / 怎麼把它 Build 起來

To start up the dev server, you will need Python poetry ^1.1

After poetry installed, run following commands:

    poetry install
    poetry shell
    python3 app.py

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
...
...


## LICENSE

MIT License

## **套件**

`python` = "^3.6.2-"
`Flask` = "^2.0.2"
`line-bot-sdk` = "^2.0.1"
`Flask-Cors` = "^3.0.10"
`pandas` = "1.1.5"
`mysql-connector-python` = "8.0.26"
`torch` = "1.10.1"
`scikit-learn` = "0.24.2"
`transformers` = "4.12.5"
`torchvision` = "0.11.2"
`plotly` = "5.4.0"
`SQLAlchemy` = "1.4.28"
`matplotlib` = "3.3.4"

**包裝套件**
poetry = "^1.1.12"
