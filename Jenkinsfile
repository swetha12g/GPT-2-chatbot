pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'llama_s_chatbot'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    dockerImage.run('cpus="4" -it')
                }
            }
        }
    }
    
}
