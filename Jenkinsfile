pipeline {
    agent any
    stages {
        stage('test stage') {
            steps {
                withPythonEnv('python'){
                    sh 'python manage.py test polls'
                    }
            }
        }
    }
}

