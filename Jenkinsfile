pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                withPythonEnv('python3.5') {
                     pysh 'python manage.py test polls'
                }

            }
        }

    }
}