FROM python:3.8.3-alpine3.11
COPY . .     
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]