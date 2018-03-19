FROM python:latest

WORKDIR /Dockerfile
ADD . /Dockerfile
RUN pip install -r requirements.txt
EXPOSE 80
ENV NAME="Marvin"

CMD ["python", "app.py"]
