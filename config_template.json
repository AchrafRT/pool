SayF Pool App - v13 AM/PM/Custom Timer Update

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

Main v13 changes:
- Original single-file architecture preserved in pool_app_verified/run_pool.py.
- AM / PM / Custom tariff tabs added to each table.
- AM flat bill split: P1 = 9$, added players = 7$ each.
- Close buttons simplified to Fermer PAYÉ / Fermer NON PAYÉ.
- Custom timer supports amount or minutes.
- Timer blinks the light at 3 minutes remaining and turns it off at expiry.
- Expired custom timers can resume at the current normal hourly rate.
- Admin report added for table opens, popular rates, manual ON/OFF, timers, and totals.
- Admin password can be changed from the Admin panel.

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
