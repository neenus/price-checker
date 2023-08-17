pipeline {
    agent {
      docker {
        image 'python:3.8-buster'
      }
    }

    stages {
      stage('Version') {
        steps {
          sh 'python3 --version'
          sh 'pip3 --version'
        }
      }
      stage('Install dependencies') {
        steps {
          sh 'pip3 install -r requirements.txt'
        }
      }
      stage('Run Script') {
        // Run the script and return the printed output
        steps {
          script {
            def scriptOutput = sh(script: 'python3 main.py', returnStdout: true).trim()
            echo scriptOutput
            // Save scriptoutput to a variable to be used in the next stage
            env.SCRIPT_OUTPUT = scriptOutput
          }
        }
      }
      stage('Send Email') {
        steps {
          echo 'Script output: ' + env.SCRIPT_OUTPUT
          script {
            def price = env.SCRIPT_OUTPUT.toInteger()
            if (price < 1000) {
            echo 'Sending email'
            sendEmail()
            } else {
            echo 'Email notification not triggered'
            }
          }
        }
      }
    }
}

def sendEmail() {
    def buildStatus = currentBuild.currentResult
    emailext (
        to: ${DEFAULT_RECIPIENTS},
        from: ${DEFAULT_REPLYTO},
        subject: "${buildStatus}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
        body: "Build Status: ${buildStatus}",
        attachLog: true,
    )
}