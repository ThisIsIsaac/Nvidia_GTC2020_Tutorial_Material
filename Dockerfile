FROM isaac2313/frameworks:tf2.1_torch1.3_cuda10.1

# Create working directory to add repo.
WORKDIR /workshop

# Load contents into student working directory.
ADD . .

# Create working directory for students.
WORKDIR /workshop/content

# Jupyter listens on 8888.
EXPOSE 8888

# Please see `entrypoint.sh` for details on how this content
# is launched.
ADD entrypoint.sh /opt/project
ENTRYPOINT ["/opt/project/entrypoint.sh"]
