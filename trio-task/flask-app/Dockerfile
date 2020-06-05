#Use Python Image
FROM python:latest
# Install apt dependencies
RUN apt-get update && apt install -y python3-pip
# Copy contents into image
COPY . .
# run pip dependencies       -r requirments.txt
RUN pip3 install flask flask_sqlalchemy pymysql
# Expose correct port
EXPOSE 5000
# Create an entrypoint
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]