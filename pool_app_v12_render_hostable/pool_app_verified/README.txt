SayF Pool App - v11 Admin-Only Reports Tab

How to run:
1. Extract this ZIP.
2. Open the folder.
3. Run:
   python run_pool.py
4. The app opens locally in a browser window.

Passwords:
- AM shift: am or AM
- PM shift: pm or PM
- Admin: admin
- Custom rate override: pool

Main v11 change:
- The Reports tab beside Tables is now visible only when logged in as Admin.
- AM and PM staff only see the Tables tab and the Close & Report button.
- Close & Report still shows the current shift/session sales and then logs the shift out when closed.

Kept from v10:
- Deterministic player IDs: T3P1, T3P2, etc.
- 4 players maximum per table.
- Live running total per player.
- Player cashout anytime.
- Player cashout is deducted from the remaining table bill.
- Automatic pricing rules.
- Custom rate protected by password: pool.
- Built-in PDF writer, no reportlab dependency.
- JSON / JSONL local storage only.

Important:
This is a local-first app. Runtime data is stored in pool_runtime/.
Back up pool_runtime/ regularly if using this for real operations.


V12 update:
- Physical table-map layout: top row 4 / 6 / 8, bottom row 3 / 5 / 7.
- Fluid tablet-native responsive layout for landscape, portrait, and desktop screens.
- Table cards now carry deterministic table classes/data-table markers for future hardware mapping.
