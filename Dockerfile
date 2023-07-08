FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements/requirements.txt

COPY . .

CMD [ "python", "./api/main.py" ]
