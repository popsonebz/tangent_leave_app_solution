FROM python:2.7.14-jessie

WORKDIR /usr/src/app

COPY . .

#COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

#COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]
