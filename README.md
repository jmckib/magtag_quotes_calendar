# magtag_quotes_calendar

A secret calendar that displays a daily quote for the Adafruit MagTag.

When the app first starts up, you'll see the [MagTag weather project](https://learn.adafruit.com/magtag-weather/project-code), which will refresh itself daily at 6am.

To access the secret quotes calendar, press the A/D15 button, wait for the blue LED flash, then press the D/D11 button. There will be three green flashes, and then the quotes calendar will appear. It can be dismissed with the B/D14 button, or it will disappear on its own in 60 seconds, reverting back to the weather app.

To run this you'll need your own secrets.py and quotes.json (see the examples provided). The code assumes there are 183 quotes, enough for six months. After that, they repeat themselves.
