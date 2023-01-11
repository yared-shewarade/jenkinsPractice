pipeline {
    environment {
        imagename = "yared-shewarade/jenkinsPractice"
        registryCredential = "yared-shewarade"
        dockerimage = ''
    }
    agent any
    stages {
        stage('Cloning Git') {
            steps {
                git([url: 'https://github.com/yared-shewarade/jenkinsPractice.git', branch:'main', credentialsId: 'yared-shewarade'])
            }
        }
        stages('Building image') {
            steps{
                script {
                    dockerImage = docker.build imagename
                }
            }
        }
        stage('Deploy Image'){
            steps{
                script {
                    docker.withRegistry('', registryCredential ) {
                        dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Remove Unused docker image') {
            steps{
                sh "docker rmi $imagename:$BUILD_NUMBER"
                sh "docker rmi $imagename:latest"
            }
        }
    }
}