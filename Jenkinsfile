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
      parallel {
        stage('test') {
          steps {
            sh 'echo $B'
          }
        }
        stage('error') {
          steps {
            git(url: 'https://github.com/kevin807210561/DailyPractice.git', branch: '54', credentialsId: '541', poll: true)
          }
        }
      }
    }
  }
  environment {
    B = '2'
  }
}