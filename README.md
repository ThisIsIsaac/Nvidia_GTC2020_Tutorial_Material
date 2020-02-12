# GTC Example Repo

[source](https://gitlab.com/joshwyatt/gtc_example_repo/-/tree/master)

# Docker Instructions

1. Use `Dockerfile` to build a docker image: `sudo docker build -t isaac2313/gtc2020_tutorial_content:v1 .`.

2. Run a container from this image: `sudo docker run -p 8888:8888 isaac2313/gtc2020_tutorial_content:v1`.

3. If your docker is running from remote, use ssh port forwarding: `ssh -N -f -L localhost:16006:localhost:8888 usr@ip`

4. Once the container is running, visit the content in your browser at `localhost:16006`.

