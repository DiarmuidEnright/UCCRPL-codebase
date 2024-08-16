#!/bin/bash

SERVER_USER="your-username"
SERVER_IP="your-server-ip"
APP_DIR="/path/to/app"
SERVICE_NAME="rocket-dashboard"

echo "Packaging the application..."
tar -czvf rocket-dashboard.tar.gz src/ requirements.txt

echo "Uploading package to the server..."
scp rocket-dashboard.tar.gz $SERVER_USER@$SERVER_IP:$APP_DIR

echo "Deploying the application on the server..."
ssh $SERVER_USER@$SERVER_IP << EOF
    cd $APP_DIR
    tar -xzvf rocket-dashboard.tar.gz
    rm rocket-dashboard.tar.gz
    source venv/bin/activate
    pip install -r requirements.txt
    echo "Restarting the service..."
    sudo systemctl restart $SERVICE_NAME
    echo "Deployment completed."
EOF

rm rocket-dashboard.tar.gz

echo "Local cleanup completed."
