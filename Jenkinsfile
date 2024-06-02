pipeline {
    agent any
    
    environment {
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials'
        DOCKER_IMAGE_NAME = 'your-docker-image-name'
        DOCKER_IMAGE_TAG = 'latest'
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
        DOCKER_COMPOSE_DEPLOY_FILE = 'docker-compose.deploy.yml'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your/repository.git'
            }
        }

        stage('Testing') {
            steps {
                sh 'pip install -r requirements.txt' // Install dependencies
                sh 'pytest' // Run tests using pytest
            }
        }

        stage('Building') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}") // Build Docker image
                }
            }
        }

        stage('Pushing to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CREDENTIALS}", usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_USERNAME}", "${DOCKER_PASSWORD}") {
                            docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}").push() // Push image to Docker Hub
                        }
                    }
                }
            }
        }

        stage('Deploying') {
            steps {
                script {
                    // Update docker-compose.deploy.yml file with the new image tag
                    sh "sed -i 's|image: ${DOCKER_IMAGE_NAME}:.*|image: ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}|' ${DOCKER_COMPOSE_DEPLOY_FILE}"
                    // Deploy updated containers using Docker Compose
                    sh "docker-compose -f ${DOCKER_COMPOSE_FILE} -f ${DOCKER_COMPOSE_DEPLOY_FILE} up -d"
                }
            }
        }
    }

    post {
        success {
            echo 'Build and deployment successful!'
        }
        failure {
            echo 'Build or deployment failed.'
        }
    }
}