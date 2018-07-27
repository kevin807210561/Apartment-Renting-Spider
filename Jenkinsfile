pipeline {
  agent {
    docker {
      image 'python:3.5.1'
    }

  }
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
        stage('') {
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