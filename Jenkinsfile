pipeline {
    agent any
    stages {
        stage('version check') {
            steps {
               withPythonEnv('/usr/bin/python3.7') {
                                   sh 'python --version'

                               }
            }
        }


    }


}



