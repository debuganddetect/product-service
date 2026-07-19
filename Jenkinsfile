pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout info') {
            steps {
                script {
                    def commit = env.GIT_COMMIT ?: sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
                    def shortCommit = commit.take(7)
                    def author = sh(
                        script: "git log -1 --pretty=format:'%an'",
                        returnStdout: true
                    ).trim()
                    def message = sh(
                        script: "git log -1 --pretty=format:'%s'",
                        returnStdout: true
                    ).trim()
                    def when = sh(
                        script: "git log -1 --pretty=format:'%ci'",
                        returnStdout: true
                    ).trim()
                    def repo = env.GIT_URL ?: 'product-service'
                    def branch = env.BRANCH_NAME ?: env.GIT_BRANCH ?: 'unknown'

                    echo "============================================================"
                    echo "Auto-triggered because ${author} committed ${shortCommit}"
                    echo "in repo ${repo} on branch ${branch} at ${when}"
                    echo "Commit message: ${message}"
                    echo "============================================================"
                }
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Unit tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    export PYTHONPATH=.
                    pytest -q
                '''
            }
        }

        stage('Security scan (basic)') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pip install pip-audit
                    pip-audit -r requirements.txt || true
                '''
            }
        }
    }

    post {
        success {
            echo "CI PASSED for product-service"
        }
        failure {
            echo "CI FAILED for product-service"
        }
    }
}
