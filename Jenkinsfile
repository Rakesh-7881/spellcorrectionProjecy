pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/Rakesh-7881/spellcorrectionProjecy.git'
      }
    }

    stage('Setup & Install') {
      steps {
        // Use one multi-line bat block so venv stays active inside the block
        bat '''
        python -m venv venv
        call venv\\Scripts\\activate
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt
        python -m pip install pytest
        '''
      }
    }

    stage('Run Tests') {
      steps {
        bat '''
        call venv\\Scripts\\activate
        python -m pytest test_spell.py
        '''
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying Spelling Correction Script...'
        bat '''
        call venv\\Scripts\\activate
        python spell_corrector.py < input.txt > output.txt
        '''
        archiveArtifacts artifacts: 'output.txt', onlyIfSuccessful: true
      }
    }
  }
}
