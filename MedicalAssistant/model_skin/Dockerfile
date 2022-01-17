# Pull base image
FROM python:3.6.15-slim-bullseye

WORKDIR /

# RUN apt update
# RUN apt install -qqy wget
RUN python3 -m pip install --no-cache-dir --upgrade pip && python3 -m pip install torch==1.10.1+cpu  torchaudio==0.10.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html && \
    pip install flask

# download model
RUN wget -P /model_skin/ https://storage.googleapis.com/tfi101linebot/densenetSkin.pt

COPY ./model_skin /

COPY app.py /


EXPOSE 5001
CMD python3 app.py
