[tool.poetry]
name = "medicalassistant"
version = "0.1.0"
description = "tfi101"
authors = ["tfi101-1"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.6.2-"
Flask = "^2.0.2"
line-bot-sdk = "^2.0.1"
Flask-Cors = "^3.0.10"
pandas = "1.1.5"
mysql-connector-python = "8.0.26"
torch = "1.10.1"
scikit-learn = "0.24.2"
transformers = "4.12.5"
torchvision = "0.11.2"
plotly = "5.4.0"
SQLAlchemy = "1.4.28"
matplotlib = "3.3.4"

[tool.poetry.dev-dependencies]
poetry = "^1.1.12"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"


**套件**
flask 2.0.2 A simple framework for building complex web applications.
├── click >=7.1.2
│   ├── colorama * 
│   └── importlib-metadata * 
│       └── zipp >=0.5 
├── itsdangerous >=2.0
├── jinja2 >=3.0
│   └── markupsafe >=2.0 
└── werkzeug >=2.0
    └── dataclasses * 
flask-cors 3.0.10 A Flask extension adding a decorator for CORS support
├── flask >=0.9
│   ├── click >=7.1.2 
│   │   ├── colorama * 
│   │   └── importlib-metadata * 
│   │       └── zipp >=0.5 
│   ├── itsdangerous >=2.0 
│   ├── jinja2 >=3.0 
│   │   └── markupsafe >=2.0 
│   └── werkzeug >=2.0 
│       └── dataclasses * 
└── six *
line-bot-sdk 2.0.1 LINE Messaging API SDK for Python
├── aiohttp >=3.7.4
│   ├── aiosignal >=1.1.2 
│   │   └── frozenlist >=1.1.0 
│   ├── async-timeout >=4.0.0a3,<5.0 
│   │   └── typing-extensions >=3.6.5 
│   ├── asynctest 0.13.0 
│   ├── attrs >=17.3.0 
│   ├── charset-normalizer >=2.0,<3.0 
│   ├── frozenlist >=1.1.1 (circular dependency aborted here)
│   ├── idna-ssl >=1.0 
│   │   └── idna >=2.0 
│   ├── multidict >=4.5,<7.0 
│   ├── typing-extensions >=3.7.4 (circular dependency aborted here)
│   └── yarl >=1.0,<2.0 
│       ├── idna >=2.0 (circular dependency aborted here)
│       ├── multidict >=4.0 (circular dependency aborted here)
│       └── typing-extensions >=3.7.4 (circular dependency aborted here)
├── future *
└── requests >=2.0
    ├── certifi >=2017.4.17 
    ├── charset-normalizer >=2.0.0,<2.1.0 
    ├── idna >=2.5,<4 
    └── urllib3 >=1.21.1,<1.27 
matplotlib 3.3.4 Python plotting package
├── cycler >=0.10
├── kiwisolver >=1.0.1
├── numpy >=1.15
├── pillow >=6.2.0
├── pyparsing >=2.0.3,<2.0.4 || >2.0.4,<2.1.2 || >2.1.2,<2.1.6 || >2.1.6
└── python-dateutil >=2.1
    └── six >=1.5 
mysql-connector-python 8.0.26 MySQL driver written in Python
└── protobuf >=3.0.0
pandas 1.1.5 Powerful data structures for data analysis, time series, and statistics
├── numpy >=1.15.4
├── python-dateutil >=2.7.3
│   └── six >=1.5 
└── pytz >=2017.2
plotly 5.4.0 An open-source, interactive data visualization library for Python
├── six *
└── tenacity >=6.2.0
poetry 1.1.12 Python dependency management and packaging made easy.
├── cachecontrol >=0.12.9,<0.13.0
│   ├── lockfile >=0.9 
│   ├── msgpack >=0.5.2 
│   └── requests * 
│       ├── certifi >=2017.4.17 
│       ├── charset-normalizer >=2.0.0,<2.1.0 
│       ├── idna >=2.5,<4 
│       └── urllib3 >=1.21.1,<1.27 
├── cachy >=0.3.0,<0.4.0
├── cleo >=0.8.1,<0.9.0
│   └── clikit >=0.6.0,<0.7.0 
│       ├── crashtest >=0.3.0,<0.4.0 
│       ├── pastel >=0.2.0,<0.3.0 
│       └── pylev >=1.3,<2.0 
├── clikit >=0.6.2,<0.7.0
│   ├── crashtest >=0.3.0,<0.4.0 
│   ├── pastel >=0.2.0,<0.3.0 
│   └── pylev >=1.3,<2.0 
├── crashtest >=0.3.0,<0.4.0
├── html5lib >=1.0,<2.0
│   ├── six >=1.9 
│   └── webencodings * 
├── importlib-metadata >=1.6.0,<2.0.0
│   └── zipp >=0.5 
├── keyring >=21.2.0,<22.0.0
│   ├── importlib-metadata >=1 
│   │   └── zipp >=0.5 
│   ├── jeepney >=0.4.2 
│   ├── pywin32-ctypes <0.1.0 || >0.1.0,<0.1.1 || >0.1.1 
│   └── secretstorage >=3.2 
│       ├── cryptography >=2.0 
│       │   └── cffi >=1.12 
│       │       └── pycparser * 
│       └── jeepney >=0.6 (circular dependency aborted here)
├── packaging >=20.4,<21.0
│   └── pyparsing >=2.0.2 
├── pexpect >=4.7.0,<5.0.0
│   └── ptyprocess >=0.5 
├── pkginfo >=1.4,<2.0
├── poetry-core >=1.0.7,<1.1.0
│   └── importlib-metadata >=1.7.0,<2.0.0 
│       └── zipp >=0.5 
├── requests >=2.18,<3.0
│   ├── certifi >=2017.4.17 
│   ├── charset-normalizer >=2.0.0,<2.1.0 
│   ├── idna >=2.5,<4 
│   └── urllib3 >=1.21.1,<1.27 
├── requests-toolbelt >=0.9.1,<0.10.0
│   └── requests >=2.0.1,<3.0.0 
│       ├── certifi >=2017.4.17 
│       ├── charset-normalizer >=2.0.0,<2.1.0 
│       ├── idna >=2.5,<4 
│       └── urllib3 >=1.21.1,<1.27 
├── shellingham >=1.1,<2.0
├── tomlkit >=0.7.0,<1.0.0
└── virtualenv >=20.0.26,<21.0.0
    ├── distlib >=0.3.1,<1 
    ├── filelock >=3.2,<4 
    ├── importlib-metadata >=0.12 
    │   └── zipp >=0.5 
    ├── importlib-resources >=1.0 
    │   └── zipp >=3.1.0 (circular dependency aborted here)
    ├── platformdirs >=2,<3 
    └── six >=1.9.0,<2 
scikit-learn 0.24.2 A set of python modules for machine learning and data mining
├── joblib >=0.11
├── numpy >=1.13.3
├── scipy >=0.19.1
│   └── numpy >=1.14.5 
└── threadpoolctl >=2.0.0
sqlalchemy 1.4.28 Database Abstraction Library
├── greenlet !=0.4.17
└── importlib-metadata *
    └── zipp >=0.5 
torch 1.10.1 Tensors and Dynamic neural networks in Python with strong GPU acceleration
├── dataclasses *
└── typing-extensions *
torchvision 0.11.2 image and video datasets and models for torch deep learning
├── numpy *
├── pillow >=5.3.0,<8.3.0 || >8.3.0
└── torch 1.10.1
    ├── dataclasses * 
    └── typing-extensions * 
transformers 4.12.5 State-of-the-art Natural Language Processing for TensorFlow 2.0 and PyTorch
├── dataclasses *
├── filelock *
├── huggingface-hub >=0.1.0,<1.0
│   ├── filelock * 
│   ├── importlib-metadata * 
│   │   └── zipp >=0.5 
│   ├── packaging >=20.9 
│   │   └── pyparsing >=2.0.2 
│   ├── pyyaml * 
│   ├── requests * 
│   │   ├── certifi >=2017.4.17 
│   │   ├── charset-normalizer >=2.0.0,<2.1.0 
│   │   ├── idna >=2.5,<4 
│   │   └── urllib3 >=1.21.1,<1.27 
│   ├── tqdm * 
│   │   └── colorama * 
│   └── typing-extensions >=3.7.4.3 
├── importlib-metadata *
│   └── zipp >=0.5 
├── numpy >=1.17
├── packaging >=20.0
│   └── pyparsing >=2.0.2 
├── pyyaml >=5.1
├── regex !=2019.12.17
├── requests *
│   ├── certifi >=2017.4.17 
│   ├── charset-normalizer >=2.0.0,<2.1.0 
│   ├── idna >=2.5,<4 
│   └── urllib3 >=1.21.1,<1.27 
├── sacremoses *
│   ├── click * 
│   │   ├── colorama * 
│   │   └── importlib-metadata * 
│   │       └── zipp >=0.5 
│   ├── joblib * 
│   ├── regex * 
│   ├── six * 
│   └── tqdm * 
│       └── colorama * (circular dependency aborted here)
├── tokenizers >=0.10.1,<0.11
└── tqdm >=4.27
    └── colorama * 
