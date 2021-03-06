pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install --user -r requirements.txt'
            }
        }

        stage('Lint Python Code') {
            steps {
                sh 'pylint --disable=R,C,W1203,W1309,E0401 app.py'
            }
        }

        stage('Local Build') {
            steps {
                sh 'docker-compose -f docker-compose.yaml up -d'
            }
        }

        stage('API Tests') {
            steps {
                sh 'pytest tests/test_std.py'
            }
        }

        stage('Tag and Push') {
            environment {
                DOCKER_USER = credentials('docker-username')
                DOCKER_PASSWORD = credentials('docker-password')
            }
            steps {
                sh '''
                    docker login -u $DOCKER_USER -p $DOCKER_PASSWORD
                    docker tag std-app:latest vinothramesh/std-app:latest
                    docker push vinothramesh/std-app:latest
                '''
            }
        }
        
        stage('Stop and Remove Containers') {
            steps {
                sh'''
                    docker stop $(docker ps -aq)
                    docker rm $(docker ps -aq)
                '''
            }
        }

        stage('Deploy to EKSCluster') {
            when {
                branch "master"
            }
            steps {
                withAWS(region: 'us-east-1', credentials: 'aws-credentials') {
                    sh '''
                        aws eks --region us-east-1 update-kubeconfig --name EKSCluster
                        kubectl --kubeconfig ~/.kube/config apply -f kube/deployment.yaml
                        kubectl --kubeconfig ~/.kube/config apply -f kube/loadbalancer.yaml
                    '''
                }
            }
        }

        stage( 'Rolling Restart') {
            when {
                branch "master"
            }
            steps {
                withAWS(region: 'us-east-1', credentials: 'aws-credentials') {
                    sh 'kubectl --kubeconfig ~/.kube/config rollout restart deployment std-app'
                }
            }
        }
    }
}