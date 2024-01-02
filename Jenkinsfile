pipeline {
    agent any

    
    stages {
        stage('Stop Running Containers') {
            steps {
                script {
                    // Stop all running Docker containers
                    sh 'docker stop $(docker ps -q)'
                }
            }
        }
        stage('Cleanup') {
            steps {
                script {
                    // Clean up unused Docker images to free up space
                    sh "docker system prune -af"
                }
            }
        }
        stage('Deploy Containers') {
            steps {
                script {
                    // Deploy using docker-compose
                    sh 'docker-compose up -d'
                }
            }
        }
        
    }
    post {
        always {
            // Log out from Docker Hub and bring down services
            sh 'docker system prune -af'
        }
    }
}
