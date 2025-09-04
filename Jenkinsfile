pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Rakesh-7881/spellcorrectionProjecy.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest test_spell.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Spelling Correction Script...'
                // Run the script with input/output redirection
                bat '''
                if exist output.txt del output.txt
                python spell_corrector.py < input.txt > output.txt
                '''
            }
        }
    }
}
