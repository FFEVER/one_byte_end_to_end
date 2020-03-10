pipeline {
    agent any
    stages {
        stage('version check') {
            steps {
               withPythonEnv('CPython-3.7') {
                                   sh 'python --version'

                               }
            }
        }


    }


}



