pipeline {
    agent any
    stages {
        stage('git checkout'){
            steps {
                echo "Checking out the code for git repository"
            }
        }
        stage("building docker images"){
            steps {
                echo "Building docker image using Dockerfile"
            }
        }
        stage("pushing docker image to dockerhub"){
            steps {
                echo "Pushing docker image to dockerhub"
            }
        }
    }
}