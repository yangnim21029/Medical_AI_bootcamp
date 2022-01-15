# Pull base image
FROM python:3.7 AS base

WORKDIR /

RUN sudo apt update
RUN sudo apt install python3-pip3 unzip wget git
RUN git clone https://github.com/yangnim21029/tfi101_medicalAssistant.git/mode_qa
# poetry套件相依與管理
RUN pip3 install torch==1.10.1+cpu torchvision==0.11.2+cpu torchaudio==0.10.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
# download model
RUN wget https://storage.googleapis.com/tfi101_model/model1.zip
RUN unzip model1.zip && del mode1.zip

EXPOSE 3000
CMD python3 app.py
