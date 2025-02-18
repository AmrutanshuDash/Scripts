#!/bin/bash

#APP_DIR="${ENV_NAME:0:3}_app"
TOMCAT_DIR="/svw/svw_app/apache/tomcat"
# Enter the specific tomcat directory
cd "$TOMCAT_DIR" || { echo "Directory not found"; exit 1; }

# Download the Tomcat tar.gz file
echo "Downloading Apache Tomcat..."
wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.95/bin/apache-tomcat-9.0.95.tar.gz --no-check-certificate

if [ $? -eq 0 ]; then
    echo "Download completed. Extracting the tar.gz file..."
    tar -zxvf apache-tomcat-9.0.95.tar.gz
    cd "$TOMCAT_DIR"
    unlink rel 2>/dev/null #if it exists

    # creating new symlink to the new version
    ln -sf "$TOMCAT_DIR"/apache-tomcat-9.0.95 rel
    echo "Tomcat installation completed successfully."
else
    echo "Error downloading Tomcat."
    exit 1
fi
