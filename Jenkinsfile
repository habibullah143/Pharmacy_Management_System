pipeline {
    agent any
 
    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('habibullah143/pharmacy-management-system:latest')
                }
            }
        }
        
        stage('Review') {
            steps {
                script {
                    // Perform any code review tasks here
                }
            }
        }
        
        stage('Testing') {
            steps {
                script {
                    docker.image('habibullah143/pharmacy-management-system:latest').run('python', 'manage.py', 'test')
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image('habibullah143/pharmacy-management-system:latest').push()
                    }
                    // Perform deployment steps here (e.g., Kubernetes deployment, SSH to server, etc.)
                }
            }
        }
    }
}
