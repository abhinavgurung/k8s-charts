FROM python:3.10.9-alpine3.16

RUN mkdir /app

WORKDIR /app

# Copy the project files to the container
COPY . .

# Install gcc + libffi
RUN apk add build-base libffi-dev

# Update OS package index and update packages to latest versions.
RUN apk update && apk upgrade

# COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv --no-cache-dir && pipenv install --system --deploy --ignore-pipfile

RUN pip install setuptools --upgrade
RUN pip install certifi --upgrade

EXPOSE 5000

# Flask environment variables
ENV FLASK_RUN_PORT="5000"
ENV FLASK_APP=run.py

RUN ["chmod", "+x", "entrypoint.sh"]

ENTRYPOINT ["/app/entrypoint.sh"]