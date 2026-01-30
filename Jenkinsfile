pipeline {
    agent any 

    environment {
        APP_DIR = '/var/www/warungku_app'
        DOCKER_FILE_NAME = "Dockerfile"
        DOCKER_HUB_CREDENTIAL = "DOCKER_HUB_CREDENTIAL"

        BACKEND_IMAGE = "davidaryasetia/warungku-backend:latest"
        FRONTEND_IMAGE = "davidaryasetia/warungku-frontend:latest"
    }

    stages {
        stage ("Checkout Source Code"){
            steps {
                dir("${APP_DIR}"){
                    sh """ 
                    git config --global --add safe.directory ${APP_DIR}
                    git pull origin main
                    """
                }
            }
        }
        stage ("Build Backend Image"){
            steps {
                script {
                    backendImage = docker.build("${BACKEND_IMAGE}", "${APP_DIR}/backend")
                }
            }
        }
        stage ("Build Frontend Image"){
            steps {
                script {
                    frontendImage = docker.build("${FRONTEND_IMAGE}", "${APP_DIR}/frontend")
                }
            }
        }
        stage ("Push Image to Dockerhub"){
            steps {
                script {
                    docker.withRegistry("https://registry.hub.docker.com", DOCKER_HUB_CREDENTIAL){
                        backendImage.push("latest")
                        frontendImage.push("latest")

                        backendImage.push("${BUILD_NUMBER}")
                        frontendImage.push("${BUILD_NUMBER}")
                    }
                }
            }
        }
        stage ("Deploy Pull Image + Up images"){
            steps {
                sh """ 
                docker compose down
                docker compose pull
                docker compose up -d  
                """
            }
        }
    }

    post {
        success {
            echo "Success running the container"
        }
        failure {
            echo "Deploy failed"
        }
    }
}