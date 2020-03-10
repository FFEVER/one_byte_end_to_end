pipeline {
    agent any
    stages {
        stage('version check') {
            steps {
                sh 'python --version'
            }
        }

        stage('test') {
                    steps {
                        sh 'python manage.py test polls'
                    }
                }
    }


}



