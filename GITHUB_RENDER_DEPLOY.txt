COPY-PASTE DEPLOY: GitHub + Render
==================================

1. Unzip this folder.

2. Open a terminal inside the unzipped pool-main folder.

3. Run these commands:

    git init
    git add .
    git commit -m "Deploy SayF Pool Control Render demo"
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    git push -u origin main

4. In Render:

    New +
    Web Service
    Connect your GitHub repo

5. Use these settings if Render does not auto-detect render.yaml:

    Environment: Python
    Build Command: pip install -r requirements.txt
    Start Command: bash start_render.sh

6. Default login passwords:

    AM: am
    PM: PM
    Admin: admin

Note:
This is the web demo version. Hardware relay control belongs on the local bar computer, not Render.
