pipeline {
    agent { docker { image 'python:3.7.6' } }
    stages {
        stage('Check version') {
            steps {
                sh 'python --version'
            }
        }
        stage('test') {
                    steps {
                        sh 'pip install Django'
                        sh 'python manage.py test polls'
                    }


    }
}
}