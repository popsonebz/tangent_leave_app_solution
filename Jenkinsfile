node {
    //get latest change in code
    stage ("Get Latest Code") {
        checkout scm
    }
    //get build dockerfile
    stage ("build dockerfile") {
        sh "docker build -t tangent -f Dockerfile ."
    }
 }
