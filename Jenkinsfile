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
        echo 'Script output: ' + env.SCRIPT_OUTPUT
        steps {
          script {
            if (env.SCRIPT_OUTPUT < 1000) {
            echo 'Sending email'

            mail(
                from: $DEFAULT_REPLYTO,
                to: $DEFAULT_RECIPEINTS_LIST,
                subject: $DEFAULT_SUBJECT,
                body: $DEFAULT_BODY
              )
            } else {
            echo 'Email notification not triggered'
            }
          }
        }
      }
    }
}
