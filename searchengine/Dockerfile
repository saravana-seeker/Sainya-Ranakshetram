#https://dev.to/aymanemx/building-a-full-text-search-app-using-django-docker-and-elasticsearch-3bai
# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY req.txt req.txt
RUN pip install req.txt
#COPY Pipfile Pipfile.lock /code/
#RUN pipenv install --system

# Copy project
COPY . /code/