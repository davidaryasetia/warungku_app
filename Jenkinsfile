pipeline {
    agent any 

    environment {
        APP_DIR = '/var/www/warungku_app'
    }

    stages {
        stage ('Pulling From Github'){
            steps {
                sh ''' 
                cd ${APP_DIR}
                git config --global --add safe.directory '/var/www/warungku_app'
                git pull origin main
                '''
            }
        }
        stage('Stop and remove container'){
            steps {
                sh """ 
                cd ${APP_DIR}
                docker compose down --remove-orphans
                """
            }
        }
        stage('Rebuild the Docker images'){
            steps { 
                sh """ 
                cd ${APP_DIR}
                docker compose build
                """
            }
        }
        stage("Running the container"){
            steps {
                sh """ 
                cd ${APP_DIR}
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