pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Git에서 코드 가져오기
                git url: 'https://github.com/your-repo-url.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // 필요한 라이브러리 설치
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Robot Tests') {
            steps {
                // Robot Framework 테스트 실행
                sh 'robot -d results tests/'
            }
        }
    }

    post {
        always {
            // 테스트 결과를 아카이브
            archiveArtifacts artifacts: 'results/*.xml', allowEmptyArchive: true

            // Robot Framework 플러그인을 사용하여 결과 출력
            robot outputPath: 'results'
        }
    }
}
