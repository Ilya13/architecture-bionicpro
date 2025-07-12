FROM python:3.9

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY ./app /api/app


CMD ["fastapi", "run", "app/main.py", "--port", "80"]



WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

COPY ./ /app

EXPOSE 8080

CMD ["python", "./run.py"]