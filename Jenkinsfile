pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                echo 'Started project 3: CI/CD pipeline for django app'
                echo 'Does it automatically build after a new commit?'
                echo 'Demo to Sai'
            }
        }
    }
    post {
    success {
      mail to: abhishekbishnoi694@gmail.com, subject: ‘The Pipeline success :(‘
    }
  }
}
