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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_spell.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Spelling Correction Script...'
                // For demo, just run the script
                sh 'python spell_corrector.py < input.txt > output.txt || true'
            }
        }
    }
}
