pipeline {
    agent agent { docker { image 'python:3.7.6' } }

    stages {
        stage ('test stage'){

            steps {

                    sh 'python manage.py test polls'

            }
        }

    }
}

