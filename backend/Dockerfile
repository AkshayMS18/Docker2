FROM python:3.8-slim
WORKDIR /app
COPY main.py .
ADD https://com-prac-bucket.s3.ap-south-1.amazonaws.com/image.PNG .
ADD https://com-prac-bucket.s3.ap-south-1.amazonaws.com/s3.png .
ARG NAME=MicroDegree
ENV NAME=${NAME}
ARG server_port=80
ENV server_port=${server_port}
EXPOSE ${servser_port}
# VOLUME ['/data']
CMD ["python3", "main.py"]