pipeline {
    agent any
    
    environment {
      PATH = "/usr/local/opt/openjdk/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${env.PATH}"
      TAG = "operationalErrorDB"
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
        
        stage("The dynamic image tag") {
            steps {
              sh 'cd CICD; chmod +x changeTag.sh; ./changeTag.sh $TAG;'
            }
        }
        stage("Ansible Playbook: Build the docker image of the app") {
            steps {
                sh 'cd CICD; ansible-playbook -i ${WORKSPACE}/host playbook-image-build-dynamic-tag.yaml;'
            }
        }
        
        stage("Ansible Playbook: Deploy the Django, Prometheus, and Grafana as kubernetes pod") {
            steps {
                sh 'cd CICD; ansible-playbook -i ${WORKSPACE}/host playbook-deploy-django-prometheus-grafana.yaml;'
            }
        }
       
        stage("Zoom chat connection webhook") {
            steps {
                zoomSend authToken: 'VkVSU046MDAw_Y0FlnIZQmyg4Gsy3jkW4QRd8p1Ynbejb0BHoKmHsOUcoDD219psvGTaRJyko0symkY', jenkinsProxyUsed: true, message: 'Trying the Django CICD...', webhookUrl: 'https://applications.zoom.us/addon/v2/jenkins/webhooks/CcnlmEa3TbSgEXnceCkd1Q'
            }
        }
    }
}

