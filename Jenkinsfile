env.BUILD_NUMBER=env.BUILD_NUMBER
def branch = env.BRANCH_NAME

node {
    //get latest change in code
    stage ("Get Latest Code") {
        checkout scm
    }
    //get build dockerfile
    stage ("build dockerfile") {
        sh "docker build -t tangent -f Dockerfile ."
    }
    //login,push to aws ecr
    stage ("login, tag, push and cleanup") {
        sh "eval \$(aws ecr get-login --region eu-west-1)"
        sh "docker tag tangent:latest 931871148456.dkr.ecr.eu-west-1.amazonaws.com/test:dev-$BUILD_NUMBER"
        sh "docker push 931871148456.dkr.ecr.eu-west-1.amazonaws.com/test:dev-$BUILD_NUMBER"
        sh "docker rmi 931871148456.dkr.ecr.eu-west-1.amazonaws.com/test:dev-$BUILD_NUMBER"
    }
    //deploy
    stage ("Deploy") {
        if ($branch == 'master') {
            echo 'I only execute on the master branch'
        } else {
            echo BRANCH_NAME
            sh "kubectl set image --namespace=test-jenkin-dev deployment/test-jenkin-dev test=931871148456.dkr.ecr.eu-west-1.amazonaws.com/test:dev-$BUILD_NUMBER"
        }
    }
 }
