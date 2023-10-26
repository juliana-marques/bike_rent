FROM python:3.9
WORKDIR /app
RUN pip install Flask gunicorn pytest
COPY . .
#EXPOSE 8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
