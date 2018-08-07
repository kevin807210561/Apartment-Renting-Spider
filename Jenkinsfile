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
        sh 'echo $B'
      }
    }
    stage('fileIO') {
      steps {
        readFile(file: 'testFile', encoding: 'utf-8')
        writeFile(file: 'testFile', text: 'hello world', encoding: 'utf-8')
      }
    }
  }
  environment {
    B = '2'
  }
}