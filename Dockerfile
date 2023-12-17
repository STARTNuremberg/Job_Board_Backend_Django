FROM  python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system

COPY . /code/

EXPOSE 8000

CMD gunicorn --bind :8000 --workers 2 job_board_backend.wsgi