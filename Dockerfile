FROM python:3.10

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]

WORKDIR /code

RUN mkdir vol

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./app app

# ENTRYPOINT ["tail", "-f", "/dev/null"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]