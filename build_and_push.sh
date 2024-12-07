#!/bin/bash

services=("user_service" "post_service" "follow_service" "notification_service")
username="bhavesh9876"

for service in "${services[@]}"; do
    echo "Building and pushing $service..."
    cd $service
    docker build -t $username/${service//_service/}-service:latest --no-cache .
    docker push $username/${service//_service/}-service:latest
    cd ..
done

echo "All images have been built and pushed!"
