pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git(
                    branch: 'main',
                    url: 'https://github.com/shensyuan/pytest-ci-demo.git'
                )
            }
        }

        stage('Debug Python') {
            steps {
                sh '''
                echo "===== Current Directory ====="
                pwd

                echo "===== Python ====="
                which python3
                python3 --version

                echo "===== Create venv ====="
                python3 -m venv venv

                echo "===== Workspace ====="
                ls -la

                echo "===== venv/bin ====="
                ls -la venv/bin || true

                echo "===== Python in venv ====="
                ./venv/bin/python --version || true

                echo "===== Pip in venv ====="
                ./venv/bin/python -m pip --version || true
                '''
            }
        }

        stage('Install') {
            steps {
                sh '''
                ./venv/bin/python -m pip install --upgrade pip
                ./venv/bin/python -m pip install pytest
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