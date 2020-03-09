pipeline {
    agent any

    stages {
        stage ('test stage'){

            steps {

            withMaven(maven : 'M3_6_3'){
                    sh 'python manage.py test polls'
                }
            }
        }

    }
}

