FROM python:3.8

WORKDIR /usr/src/app



##COPY requirements.txt ./
RUN pip3 install virtualenv
RUN virtualenv new-env
RUN source new-env/bin/activate
RUN new-env/bin/pip install traveltimepy

COPY . .

CMD [ "python", "./commuter/commuter_main.py" ]