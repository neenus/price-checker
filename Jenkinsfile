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

            // Convert the string to an integer if it's an integer-like value
            try {
                env.SCRIPT_OUTPUT = scriptOutput.toInteger()
            } catch (NumberFormatException e) {
                echo "Error converting scriptOutput to integer: ${e.message}"
                currentBuild.result = 'FAILURE'
                error("Script output is not a valid integer.")
            }
          }
        }
      }
      stage('Send Email') {
        steps {
          echo 'Script output: ' + env.SCRIPT_OUTPUT
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
