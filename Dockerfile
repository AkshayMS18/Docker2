# FROM ubuntu:latest
# WORKDIR /app
# RUN apt update && apt install nginx -y
# EXPOSE 80
# ENTRYPOINT ["python"]
# CMD ["main.py"]

FROM python:3.12
WORKDIR /app
COPY main.py .
EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["main.py"]