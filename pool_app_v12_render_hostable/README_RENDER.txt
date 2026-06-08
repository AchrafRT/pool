POOL APP v12 - RENDER DEMO HOSTING
===================================

This ZIP keeps the v12 software source unchanged.
Only Render deployment files were added at the ZIP root:

- Procfile
- requirements.txt
- render.yaml
- README_RENDER.txt

Render settings:

Build command:
    pip install -r requirements.txt

Start command:
    python pool_app_verified/run_pool.py --host 0.0.0.0 --port $PORT --no-browser

Notes:
- This is for demo hosting only.
- Relay/USB hardware control should stay local at the bar.
- Demo runtime data is stored in pool_app_verified/pool_runtime.
- On Render free/demo hosting, this data can reset after redeploy/restart unless you add persistent storage.

Passwords:
- AM: am or AM
- PM: pm or PM
- Admin: admin
- Custom rate: pool
