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
    stage('echo current build params') {
      steps {
        echo '${currentBuild.result}'
      }
    }
    stage('write file') {
      parallel {
        stage('write file') {
          steps {
            writeFile(file: 'test.txt', text: 'hello')
          }
        }
        stage('pwd') {
          steps {
            pwd()
          }
        }
      }
    }
  }
  environment {
    B = '2'
  }
}