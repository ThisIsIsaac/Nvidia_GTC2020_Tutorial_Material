

# GTC Example Repo

[source](https://gitlab.com/joshwyatt/gtc_example_repo/-/tree/master)

This repo gives a simple example of what a contributor would provide to the DLI so that DLI can port the content to the DLI Platform.

# Docker Instructions

Use `Dockerfile` to build a docker image with `docker build -t gtc_example_repo .`.

Run a container from this image with `docker run -p 8888:8888 --runtime=nvidia gtc_example_repo`.

If your docker is running from remote, use ssh port forwarding: `ssh -N -f -L localhost:16006:localhost:8888 usr@ip`

Once the container is running, visit the content in your browser at `localhost:8888`.

