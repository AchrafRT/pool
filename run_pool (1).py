{
  "language": "fr",
  "business_name": "Billard",
  "currency": "$",
  "tax_percent": 0.0,
  "tax_divisor": 1.15,
  "max_players_per_table": 4,
  "custom_rate_password": "pool",
  "rounding": 0.05,
  "timezone": "America/Toronto",
  "passwords": {
    "am": "am",
    "pm": "PM",
    "admin": "admin"
  },
  "pricing_options": [
    {
      "id": "am_hourly",
      "fr": "AM 11h-19h - 6$/h",
      "en": "AM 11am-7pm - $6/h",
      "kind": "hourly",
      "per_hour": 6.0,
      "flat_amount": 0.0,
      "extra_player_fee": 0.0,
      "included_players": 1,
      "shift": "am",
      "days": [
        0,
        1,
        2,
        3,
        4,
        5,
        6
      ],
      "staff_selectable": true
    },
    {
      "id": "am_flat",
      "fr": "AM 11h-19h - 9$ forfait",
      "en": "AM 11am-7pm - $9 flat",
      "kind": "flat",
      "per_hour": 0.0,
      "flat_amount": 9.0,
      "extra_player_fee": 7.0,
      "included_players": 1,
      "shift": "am",
      "days": [
        0,
        1,
        2,
        3,
        4,
        5,
        6
      ],
      "staff_selectable": true
    },
    {
      "id": "pm_12_hourly",
      "fr": "PM - 12$/h (dim, lun, mar, mer, jeu)",
      "en": "PM - $12/h (Sun, Mon, Tue, Wed, Thu)",
      "kind": "hourly",
      "per_hour": 12.0,
      "flat_amount": 0.0,
      "extra_player_fee": 0.0,
      "included_players": 1,
      "shift": "pm",
      "days": [
        0,
        1,
        2,
        3,
        6
      ],
      "staff_selectable": true
    },
    {
      "id": "pm_mon_tue_flat",
      "fr": "PM lundi/mardi - 20$ forfait 19h-3h",
      "en": "PM Monday/Tuesday - $20 flat 7pm-3am",
      "kind": "flat",
      "per_hour": 0.0,
      "flat_amount": 20.0,
      "extra_player_fee": 0.0,
      "included_players": 1,
      "shift": "pm",
      "days": [
        0,
        1
      ],
      "staff_selectable": true
    },
    {
      "id": "pm_fri_sat_hourly",
      "fr": "PM vendredi/samedi - 14$/h",
      "en": "PM Friday/Saturday - $14/h",
      "kind": "hourly",
      "per_hour": 14.0,
      "flat_amount": 0.0,
      "extra_player_fee": 0.0,
      "included_players": 1,
      "shift": "pm",
      "days": [
        4,
        5
      ],
      "staff_selectable": true
    }
  ],
  "tables": [
    {
      "number": 3,
      "name": "Table 3",
      "relay_channel": 1,
      "enabled": true
    },
    {
      "number": 4,
      "name": "Table 4",
      "relay_channel": 2,
      "enabled": true
    },
    {
      "number": 5,
      "name": "Table 5",
      "relay_channel": 3,
      "enabled": true
    },
    {
      "number": 6,
      "name": "Table 6",
      "relay_channel": 4,
      "enabled": true
    },
    {
      "number": 7,
      "name": "Table 7",
      "relay_channel": 5,
      "enabled": true
    },
    {
      "number": 8,
      "name": "Table 8",
      "relay_channel": 6,
      "enabled": true
    }
  ],
  "relay": {
    "enabled": false,
    "mode": "simulation",
    "port": "COM3",
    "baudrate": 9600,
    "protocol": "sainsmart_hex",
    "active_low": false,
    "ascii_on": "RELAY {channel} ON\n",
    "ascii_off": "RELAY {channel} OFF\n",
    "open_after_start": true,
    "close_after_stop": true,
    "close_after_pause": false
  }
}
