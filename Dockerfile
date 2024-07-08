FROM python:3.12.2

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=myproject.settings

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]