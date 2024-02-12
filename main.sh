#!/bin/zsh

result=$(docker images -q --filter "reference=hydrangea-sensiclean" | head -n 1)

# No Image Found
if [ "$result" = "" ]; then
    echo "Docker Image not Found"
    echo -n "Do you want to build the image now? (Y/N)"
    read option
    if [ "$option" = "Y" ] || [ "$option" = "y" ]; then
        docker build -t hydrangea-sensiclean .
    else
        echo "You have canceled to build the image."
    fi
# Image Exists    
else
    echo "Image Exists"
    docker_time=$(docker inspect --format='{{.Created}}' hydrangea-sensiclean | head -n 1)
    echo "Your image was created at $docker_time."
    echo -n "Do you want to run the image? (Y/N)"
    read option
    if [ "$option" = "Y" ] || [ "$option" = "y" ]; then
        docker run -i -t $result
    else
        echo "You have canceled image running."
    fi
fi