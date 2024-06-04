pipeline {
    agent any
    
    environment {
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials'
        DOCKER_IMAGE_NAME = 'jenkins-session'
        DOCKER_IMAGE_TAG = 'latest'
        DOCKER_COMPOSE_FILE = 'docker-compose-prod.yml'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/printSANO/jenkins-practice.git'
            }
        }

        stage('Test') {
            steps {
                script {
                    sh "docker --version"
                    sh "docker compose --version"
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh "docker compose -f ${DOCKER_COMPOSE_FILE} build"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "docker compose -f ${DOCKER_COMPOSE_FILE} up -d"
                }
            }
        }

    //     stage('Building') {
    //         steps {
    //             script {
    //                 docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}") // Build Docker image
    //             }
    //         }
    //     }

    //     stage('Pushing to Docker Hub') {
    //         steps {
    //             script {
    //                 withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CREDENTIALS}", usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
    //                     docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_USERNAME}", "${DOCKER_PASSWORD}") {
    //                         docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}").push() // Push image to Docker Hub
    //                     }
    //                 }
    //             }
    //         }
    //     }

    //     stage('Deploying') {
    //         steps {
    //             script {
    //                 // Update docker-compose.deploy.yml file with the new image tag
    //                 sh "sed -i 's|image: ${DOCKER_IMAGE_NAME}:.*|image: ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}|' ${DOCKER_COMPOSE_DEPLOY_FILE}"
    //                 // Deploy updated containers using Docker Compose
    //                 sh "docker-compose -f ${DOCKER_COMPOSE_FILE} -f ${DOCKER_COMPOSE_DEPLOY_FILE} up -d"
    //             }
    //         }
    //     }
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