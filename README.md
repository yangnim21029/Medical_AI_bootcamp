# 醫療助理 
This is the repoitory for the linebot server.

Discuss here: https//

model here :
[densenetSkin.pt](https://storage.cloud.google.com/tfi101_model/densenetSkin.pt?_ga=2.268373638.-988426728.1642160054&_gac=1.260146815.1642178755.CjwKCAiA24SPBhB0EiwAjBgkhtXZsRIypI4tD_3T38gYX-uWnVg8rGhwgS7uTdVmHTMJjrz5EzoIoxoCiaEQAvD_BwE)
[model_qa.zip](https://storage.cloud.google.com/tfi101_model/model_qa.zip?_ga=2.30008887.-988426728.1642160054&_gac=1.228813678.1642178755.CjwKCAiA24SPBhB0EiwAjBgkhtXZsRIypI4tD_3T38gYX-uWnVg8rGhwgS7uTdVmHTMJjrz5EzoIoxoCiaEQAvD_BwE)

## How to Build / 怎麼把它 Build 起來

To start up the dev server, you will need Python poetry = "^1.1.12"

After poetry installed, run following commands:

    poetry install
    cd tfi101_medicalAssistant/MedicalAssistant/   &&
    poetry run python3 -m flask run --port 5001

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


