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
    stage('error') {
      parallel {
        stage('error') {
          steps {
            git(url: 'https://github.com/kevin807210561/DailyPractice.git', branch: '54', credentialsId: '541', poll: true)
          }
        }
        stage('echo current build params') {
          steps {
            echo '$result'
          }
        }
      }
    }
  }
  environment {
    B = '2'
  }
}