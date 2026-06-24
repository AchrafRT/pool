SayF Pool Control - Render Demo Hosting
=======================================

This package is the same local pool-table software, prepared for GitHub + Render demo hosting.

Render settings
---------------

Build command:
    pip install -r requirements.txt

Start command:
    bash start_render.sh

Included deployment files
-------------------------

- render.yaml
- Procfile
- requirements.txt
- start_render.sh
- runtime.txt
- GITHUB_RENDER_DEPLOY.txt

Important notes
---------------

- Render hosting is for demo / remote testing.
- Real relay / USB / RS-485 hardware control should run locally at the bar computer.
- Runtime JSON data is stored in pool_app_verified/pool_runtime.
- Render free/demo storage can reset after restart/redeploy unless you add persistent storage.

Default passwords
-----------------

- AM: am or AM
- PM: pm or PM
- Admin: admin
