FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install traveltimepy

COPY . .

CMD [ "python", "./commuter/commuter_main.py" ]