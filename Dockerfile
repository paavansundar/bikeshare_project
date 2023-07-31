FROM python:3.10

ADD ./bikeshare_model /bikeshare_model
WORKDIR /bikeshare_model

COPY ./requirements/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "./api/main.py", "-d" ]
