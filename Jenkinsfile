pipeline {
    agent { docker { image 'CPython3.7.6' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}