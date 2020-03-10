pipeline {
    agent any
    stages {
        stage('version check') {
            steps {
               withPythonEnv('python') {
                                   sh 'python --version'

                               }
            }
        }


    }


}



