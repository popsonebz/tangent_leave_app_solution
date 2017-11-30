FROM python:2.7.14-jessie

WORKDIR /usr/src/app

COPY tangent_leave_app_solution ./

#COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

#COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]
