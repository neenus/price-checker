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
          echo 'DEFAULT_REPLYTO: ' + env.DEFAULT_REPLYTO
          echo 'DEFAULT_RECIPIENTS: ' + env.DEFAULT_RECIPIENTS
          script {
            def price = env.SCRIPT_OUTPUT.toInteger()
            if (price < 1000) {
              echo 'Sending email'
              // Send email notification
              // emailext (
              //   subject: "Price dropped to ${price}",
              //   body: "Price dropped to ${price}",
              //   to: "",
              //   replyTo: "",
              //   mimeType: 'text/html',
              //   attachLog: true,
              // )
            } else {
              echo 'Email notification not triggered'
            }
          }
        }
      }
    }
}