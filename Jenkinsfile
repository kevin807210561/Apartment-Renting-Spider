pipeline {
  agent any
  stages {
    stage('build') {
      environment {
        a = '1'
      }
      parallel {
        stage('build') {
          steps {
            sh 'python --version'
          }
        }
        stage('error') {
          steps {
            sleep 5
          }
        }
      }
    }
    stage('test') {
      steps {
        retry(count: 5)
      }
    }
  }
  environment {
    B = '2'
  }
}