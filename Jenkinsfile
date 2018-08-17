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
      parallel {
        stage('echo current build params') {
          steps {
            echo '${currentBuild.result}'
          }
        }
        stage('test') {
          steps {
            sh '''echo "${currentBuild.currentResult}"
echo $B'''
          }
        }
      }
    }
  }
  environment {
    B = '2'
  }
}