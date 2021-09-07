pipeline {
    agent any
    
    environment {
      PATH = "/usr/local/opt/openjdk/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${env.PATH}"
    }

    stages {
        stage('PATH checking') {
            steps {
                sh 'echo $PATH'
                sh 'echo $WORKSPACE'
                echo 'Started project 3: CI/CD pipeline for django app'
            }
        }
      
        stage("SCM Checkout") {
            steps {
                git branch: 'prometheus', credentialsId: 'jenkins-webhook', url: 'https://github.com/abhisheksaran/django-todo-app'
            }
        }
    
        stage("Ansible Playbook: Build the docker image of the app") {
            steps {
                sh 'ansible-playbook -i ${WORKSPACE}/host ${WORKSPACE}/ansible/imageBuild.yml;'
            }
        }
        
        stage("Ansible Playbook: Deploy the app as pod in kubernetes along with prometheus service") {
            steps {
                sh 'cd prometheus-djangoapp; ansible-playbook -i ${WORKSPACE}/host deploymentPrometheus.yml;'
            }
        }

        stage("Zoom chat connection webhook") {
            steps {
                zoomSend authToken: 'VkVSU046MDAw_Y0FlnIZQmyg4Gsy3jkW4QRd8p1Ynbejb0BHoKmHsOUcoDD219psvGTaRJyko0symkY', jenkinsProxyUsed: true, message: 'Trying the Django CICD...', webhookUrl: 'https://applications.zoom.us/addon/v2/jenkins/webhooks/CcnlmEa3TbSgEXnceCkd1Q'
            }
        }
    }
}

