FROM python:3.8

WORKDIR C/Users/alexb/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "commuter/commuter_main.py" ]