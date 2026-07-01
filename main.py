print("Hey, this is from microdegree")

# FROM nginx:latest
# RUN apt update && apt install -y nginx
# WORKDIR /app
# COPY main.py .
# ADD https://com-com-bucket.s3.ap-south-1.amazonaws.com/image.PNG .
# ADD https://com-com-bucket.s3.ap-south-1.amazonaws.com/s3.png .
# ARG NAME=MicroDegree
# ENV NAME=${NAME}
# ENV server_port=80
# EXPOSE ${servser_port}
# VOLUME ['/data']
# CMD ["nginx", "-g", "daemon off;"]