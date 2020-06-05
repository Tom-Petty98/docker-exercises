# Derived from official mysql image (our base image)
FROM mysql:latest
# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup
COPY ./CreateTable.sql /docker-entrypoint-initdb.d/
