FROM python:alpine
RUN apk update && apk add build-base postgresql-dev
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "main.py"]
COPY . .