FROM python:3.7
ENV PYTHONBUFFERED 1
RUN mkdir /H2O_Social_Tool
WORKDIR /H2O_Social_Tool
COPY . /H2O_Social_Tool/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD exec gunicorn H2O_Social_Tool.wsgi:application — bind 0.0.0.0:8000 — workers 3
