#!/bin/bash
set -e
cd /home/ubuntu/Database

# Ensure branch matches what GH pushes (update the branch name as needed)
BRANCH="lab-4-5-ec2-instance"

# --- Step 1: Backup app.yml if it exists ---
if [ -f "Lab_4-5/flask_project/app/config/app_ec2.yml" ]; then
  echo "Backing up app_ec2.yml..."
  cp Lab_4-5/flask_project/app/config/app_ec2.yml /tmp/app_ec2.yml.backup
fi

# --- Step 2: Pull latest code safely ---
echo "Updating code..."
git fetch origin
git stash || true
git checkout $BRANCH
git pull origin $BRANCH

# --- Step 3: Restore app.yml if needed ---
if [ -f "/tmp/app_ec2.yml.backup" ]; then
  echo "Restoring app_ec2.yml..."
  mv /tmp/app_ec2.yml.backup Lab_4-5/flask_project/app/config/app_ec2.yml
fi

# --- Step 4: Ensure virtual environment and dependencies ---
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install --upgrade pip
pip install -r all_requirements.txt

# --- Step 5: Restart Flask app ---
# echo "Restarting Flask app..."
# pkill -f "python3 app.py" || true
# nohup python3 app.py > app.log 2>&1 &

echo "✅ Deployment complete!"
