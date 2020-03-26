which ssh-agent || ( apk add --update openssh )
eval $(ssh-agent -s)
echo "$SSH_PRIVATE_KEY" | ssh-add - > /dev/null
ssh -tt -o "StrictHostKeyChecking=no" $DEPLOYMENT_SERVER_USER@$DEPLOYMENT_SERVER_IP << EOF
    docker login -u gitlab-ci-token -p $CI_JOB_TOKEN $CI_REGISTRY
    cd staging
    docker-compose stop
    docker-compose rm -f server
    docker pull $CONTAINER_RELEASE_IMAGE
    docker-compose up -d
    exit 0
EOF

