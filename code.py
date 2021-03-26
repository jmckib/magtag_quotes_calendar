import alarm
import board
import time
from adafruit_magtag.magtag import MagTag

import magtag_weather
import quotes_calendar

# After A button is pressed.
if isinstance(alarm.wake_alarm, alarm.pin.PinAlarm) and alarm.wake_alarm.pin == board.BUTTON_A:
    # Tell user it's time to press D button with blue flash.
    magtag = MagTag()
    magtag.peripherals.neopixel_disable = False
    magtag.peripherals.neopixels.fill((0, 0, 128))
    time.sleep(0.01)
    magtag.peripherals.deinit()

    pin_alarms = [
        alarm.pin.PinAlarm(pin=board.BUTTON_C, value=False, pull=True),
        alarm.pin.PinAlarm(pin=board.BUTTON_D, value=False, pull=True),
    ]

    alarm.exit_and_deep_sleep_until_alarms(*pin_alarms)

# Catch at least one wrong button press to make entering correct code a little harder.
elif isinstance(alarm.wake_alarm, alarm.pin.PinAlarm) and alarm.wake_alarm.pin == board.BUTTON_C:
    pin_alarm = alarm.pin.PinAlarm(pin=board.BUTTON_A, value=False, pull=True)
    alarm.exit_and_deep_sleep_until_alarms(pin_alarm)

# If D is pressed after A, flash green three times and show the secret quotes calendar.
elif isinstance(alarm.wake_alarm, alarm.pin.PinAlarm) and alarm.wake_alarm.pin == board.BUTTON_D:
    magtag = MagTag()
    magtag.peripherals.neopixel_disable = False
    magtag.peripherals.neopixels.fill((0, 128, 0))
    time.sleep(0.1)
    magtag.peripherals.neopixels.fill((0, 0, 0))
    time.sleep(0.1)
    magtag.peripherals.neopixels.fill((0, 128, 0))
    time.sleep(0.1)
    magtag.peripherals.neopixels.fill((0, 0, 0))
    time.sleep(0.1)
    magtag.peripherals.neopixels.fill((0, 128, 0))
    time.sleep(0.1)
    magtag.peripherals.deinit()

    quotes_calendar.main()

    # Go back to weather app after 60 seconds or B button press.
    pin_alarm = alarm.pin.PinAlarm(pin=board.BUTTON_B, value=False, pull=True)
    time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60)
    alarm.exit_and_deep_sleep_until_alarms(pin_alarm, time_alarm)

# On startup show the weather app, then go to deep sleep and wait for A button press, or refresh at 6am.
else:
    magtag_weather.main()

    pin_alarm = alarm.pin.PinAlarm(pin=board.BUTTON_A, value=False, pull=True)

    # Refresh daily at 6am.
    now = time.localtime() # magtag.get_local_time() is called at the end of magtag_weather.py, so we can avoid wasting time on it here.
    tomorrow = time.localtime(time.mktime(now) + 60 * 60 * 24)
    tomorrow_six_am = time.struct_time((tomorrow.tm_year, tomorrow.tm_mon, tomorrow.tm_mday, 6, 0, 0, tomorrow.tm_wday, tomorrow.tm_yday, tomorrow.tm_isdst))
    tomorrow_six_am_alarm = alarm.time.TimeAlarm(epoch_time=time.mktime(tomorrow_six_am))

    alarm.exit_and_deep_sleep_until_alarms(pin_alarm, tomorrow_six_am_alarm)