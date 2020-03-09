pipeline {
    agent any
    stages {
        stage('test stage') {
            withPythonEnv('python') {
                sh 'python manage.py test polls'
            }
        }
    }
}

