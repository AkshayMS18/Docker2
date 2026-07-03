pipeline {
    agent any

    environment {
        IMAGE_NAME = "microdegreee"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('git checkout'){
            steps {
                echo "Checking out the code for git repository"
            }
        }
        stage("building docker images"){
            steps {
                echo "Building docker image using Dockerfile"
                sh "docker build -t $IMAGE_NAME:latest ."
            }
        }
        stage("pushing docker image to dockerhub"){
            steps {
                withCredentials([usernamePassword(credentialsId: 'creds-of-dockerhub', passwordVariable: 'DOCKER_USER', usernameVariable: 'DOCKER_PASS')]) {
                 sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                 sh "docker tag $IMAGE_NAME:$IMAGE_TAG $DOCKER_USER/$IMAGE_NAME:$IMAGE_TAG"
                 sh "docker push $DOCKER_USER/$IMAGE_NAME:$IMAGE_TAG"
                }
            }
        }
        stage("Deploy Docker containers"){
            steps {
                echo "Deploying docker containers using docker-compose"
            }
        }
    }
}