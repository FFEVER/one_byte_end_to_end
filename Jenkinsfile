pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python manage.py test polls'
            }
        }

    }
}