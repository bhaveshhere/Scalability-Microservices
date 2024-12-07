# #!/bin/bash

# services=("user_service" "post_service" "follow_service" "notification_service")
# username="bhavesh9876"

# for service in "${services[@]}"; do
#     echo "Building and pushing $service..."
#     cd $service
#     docker build -t $username/${service//_service/}-service:latest --no-cache .
#     docker push $username/${service//_service/}-service:latest
#     cd ..
# done

# echo "All images have been built and pushed!"

#!/bin/bash

# List of services (these should be the directory names of your services)
services=("user_service" "post_service" "follow_service" "notification_service")

# Define your Docker Hub username
username="bhavesh9876"

# Loop over the services array
for service in "${services[@]}"; do
    echo "Building and pushing $service..."

    # Navigate to the service directory
    cd $service

    # Build the Docker image and tag it correctly, using the service name
    # The ${service//_service/} part removes the '_service' from the directory name
    docker build -t $username/${service//_service/}-service:latest --no-cache .

    # Push the image to Docker Hub
    docker push $username/${service//_service/}-service:latest

    # Go back to the root directory to process the next service
    cd ..
done

# Final message after all services have been processed
echo "All images have been built and pushed!"

