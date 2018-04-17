FROM python:2.7.14

EXPOSE 1234

RUN apt-get update
RUN apt-get install -y swig libssl-dev dpkg-dev netcat git

RUN mkdir /code

WORKDIR /code

COPY requirements.txt ./

RUN git clone https://github.com/popsonebz/tangent_leave_app_solution.git

RUN pip install --no-cache-dir -r requirements.txt

RUN cd tangent_leave_app_solution
#COPY . /code/

RUN python manage.py migrate

ENV DJANGO_ENV=prod

ENV DOCKER_CONTAINER=1

COPY entry_point.sh .

#RUN chmod u+x entry_point.sh

#CMD ["sh", "entry_point.sh"]

CMD ["python manage.py runserver localhost:1234"]
