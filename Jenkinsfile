pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git url: 'https://github.com/shensyuan/pytest-ci-demo.git'
            }
        }

        stage('Setup') {
            steps {
                sh '''
                python3 -m venv venv
                '''
            }
        }

        stage('Install') {
            steps {
                sh '''
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                ./venv/bin/python -m pytest -v --junitxml=report.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
    }
}