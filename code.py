import alarm
import board
import json
import random
import time
from adafruit_magtag.magtag import MagTag

import magtag_weather

PINS = (board.BUTTON_A, board.BUTTON_B, board.BUTTON_C, board.BUTTON_D)

# if isinstance(alarm.wake_alarm, alarm.pin.PinAlarm) and alarm.wake_alarm.pin == board.BUTTON_D:
#     while True:
#         print("Say what??")
#         pin_alarms = [alarm.pin.PinAlarm(pin=pin, value=False, pull=True) for pin in PINS[1:]]
#         light_sleep = alarm.light_sleep_until_alarms(*pin_alarms)
#         print("Done sleeping!")
#         magtag = MagTag()
#         magtag.peripherals.neopixel_disable = False
#         magtag.peripherals.neopixels.fill((0, 0, 128))
#         time.sleep(0.01)
#         magtag.peripherals.deinit()
#         if light_sleep.pin == board.BUTTON_B:
#             break

# pin_alarm = alarm.pin.PinAlarm(pin=board.BUTTON_D, value=False, pull=True)
# alarm.exit_and_deep_sleep_until_alarms(pin_alarm)

weekdays = ("Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun")
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")



secret_code = b'\x01\x03\x02'

if isinstance(alarm.wake_alarm, alarm.pin.PinAlarm) and alarm.wake_alarm.pin == board.BUTTON_A:
    #             Tell user its time to enter code with blue flash.
    magtag = MagTag()
    magtag.peripherals.neopixel_disable = False
    magtag.peripherals.neopixels.fill((0, 0, 128))
    time.sleep(0.01)
    magtag.peripherals.deinit()

    pin_alarms = [
        alarm.pin.PinAlarm(pin=board.BUTTON_B, value=False, pull=True),
        alarm.pin.PinAlarm(pin=board.BUTTON_C, value=False, pull=True),
    ]

    alarm.exit_and_deep_sleep_until_alarms(*pin_alarms)
#             alarm.exit_and_deep_sleep_until_alarms(pin_alarm)
    # Someone is pressing buttons. Is it the right code?
#     alarm.sleep_memory[0] = 1
#     light_sleep = None
#     while True:
#         if light_sleep:
#             alarm.sleep_memory[alarm.sleep_memory[0]] = PINS.index(alarm.wake_alarm.pin)
#             alarm.sleep_memory[0] += 1
#         else:
#             Tell user its time to enter code with blue flash.
#             magtag = MagTag()
#             magtag.peripherals.neopixel_disable = False
#             magtag.peripherals.neopixels.fill((0, 0, 128))
#             time.sleep(0.01)
#             magtag.peripherals.deinit()

#         code_entered = alarm.sleep_memory[1: alarm.sleep_memory[0]]
#         print(code_entered)

#         if code_entered == secret_code:
#             magtag = MagTag()
#             magtag.peripherals.neopixel_disable = False
#             magtag.peripherals.neopixels.fill((0, 128, 0))
#             time.sleep(0.1)
#             magtag.peripherals.neopixels.fill((0, 0, 0))
#             time.sleep(0.1)
#             magtag.peripherals.neopixels.fill((0, 128, 0))
#             time.sleep(0.1)
#             magtag.peripherals.neopixels.fill((0, 0, 0))
#             time.sleep(0.1)
#             magtag.peripherals.neopixels.fill((0, 128, 0))
#             time.sleep(0.1)
#             magtag.peripherals.deinit()
#             print("Do secret stuff!")
#             break
#         elif len(code_entered) >= len(secret_code):
#             Tell user its wrong code with red flash.
#             magtag = MagTag()
#             magtag.peripherals.neopixel_disable = False
#             magtag.peripherals.neopixels.fill((128, 0, 0))
#             time.sleep(.01)
#             magtag.peripherals.deinit()

#             alarm.sleep_memory[0] = 1

#         pin_alarms = [alarm.pin.PinAlarm(pin=pin, value=False, pull=True) for pin in PINS[1:]]
#         pin_alarms.append(alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10))
#         light_sleep = alarm.light_sleep_until_alarms(*pin_alarms)
#         print(light_sleep)
#         If password times out, go back to deep sleep.
#         if isinstance(light_sleep, alarm.time.TimeAlarm):
#             pin_alarm = alarm.pin.PinAlarm(pin=board.BUTTON_A, value=False, pull=True)
#             alarm.exit_and_deep_sleep_until_alarms(pin_alarm)
    # Do secret stuff....
#     pass
elif isinstance(alarm.wake_alarm, alarm.pin.PinAlarm) and alarm.wake_alarm.pin == board.BUTTON_B:
    print("Wrong, try again")
    pin_alarm = alarm.pin.PinAlarm(pin=board.BUTTON_A, value=False, pull=True)
    alarm.exit_and_deep_sleep_until_alarms(pin_alarm)
elif isinstance(alarm.wake_alarm, alarm.pin.PinAlarm) and alarm.wake_alarm.pin == board.BUTTON_C:
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
    print("Do secret stuff!")
else:
#     magtag = MagTag()
#     magtag.set_background("/images/background.bmp")
#     magtag.refresh()
#     magtag.peripherals.deinit()
    magtag_weather.main()

    pin_alarm = alarm.pin.PinAlarm(pin=board.BUTTON_A, value=False, pull=True)

    # Refresh daily at 6am.
    now = time.localtime()
    tomorrow = time.localtime(time.mktime(now) + 60 * 60 * 24)
    tomorrow_six_am = time.struct_time((tomorrow.tm_year, tomorrow.tm_mon, tomorrow.tm_mday, 6, 0, 0, tomorrow.tm_wday, tomorrow.tm_yday, tomorrow.tm_isdst))
    tomorrow_six_am_alarm = alarm.time.TimeAlarm(epoch_time=time.mktime(tomorrow_six_am))

    alarm.exit_and_deep_sleep_until_alarms(pin_alarm, tomorrow_six_am_alarm)

magtag = MagTag()
# magtag.graphics.splash.append(Rect(0, 0, magtag.graphics.display.width, 35, outline=0x0))

# quote in bold text, with text wrapping
# magtag.add_text(
#     text_font="/fonts/Arial-Bold-12.pcf",
#     text_wrap=28,
#     text_maxlen=120,
#     text_position=(
#         (magtag.graphics.display.width // 2),
#         (magtag.graphics.display.height // 2) - 10,
#     ),
#     line_spacing=0.75,
#     text_anchor_point=(0.5, 0),  # center the text on x & y
# )

# author in italic text, no wrapping
# magtag.add_text(
#     text_font="/fonts/Arial-Bold-12.pcf",
#     text_position=(magtag.graphics.display.width // 2, 118),
#     text_anchor_point=(0.5, 0.5),  # center it in the nice scrolly thing
# )

# Top label
magtag.add_text(
    text_font="/fonts/SUPERSCR-24.pcf",
    text_position=(130, 6),
    text_anchor_point=(0.5,0),
    is_data=False,
)

# try:
#     magtag.get_local_time()
# except:
#     pass

now = time.localtime()

magtag.set_background("/images/months/background-" + months[now.tm_mon - 1].lower() + ".bmp")

quotes = json.load(open("quotes.json"))
SEED = 1
random.seed(SEED)
quotes = sorted(quotes, key=lambda i: random.random())

# quote_index = max(0, ((now.tm_yday - now.tm_wday) - 1)) // 7
# Start over every 6 months.
quote = quotes[(now.tm_yday - 1) % 183]
#quote = quotes[-1]
has_author = "author" in quote

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

# magtag.set_text("Friday, Oct. 31" + suffix(31), auto_refresh=False)
magtag.set_text("%s, %s %s%s" % (weekdays[now.tm_wday], months[now.tm_mon - 1], now.tm_mday, suffix(now.tm_mday)), auto_refresh=False)

position_no_author = (magtag.graphics.display.width // 2, magtag.graphics.display.height // 2 + 15 + quote.get("height-offset", 0))
position_with_author = (magtag.graphics.display.width // 2, magtag.graphics.display.height // 2 + 8 + quote.get("height-offset", 0))

magtag.add_text(
    text_font="/fonts/hellovetica-8.pcf",
    text_wrap=0 if "no-text-wrap" in quote else quote.get("text-wrap", 46),
    line_spacing=1.2,
    text_position=position_with_author if has_author else position_no_author,
    text_anchor_point=(0.5, 0.5),
    is_data=False,
)

magtag.set_text(quote["quote"], index=1, auto_refresh=False)

if has_author:
    magtag.add_text(
        text_font="/fonts/Arial-Italic-12.pcf",
        line_spacing=1.2,
        text_position=(magtag.graphics.display.width // 2 - 5, magtag.graphics.display.height - 10),
        text_anchor_point=(0.5, 0.5),
        is_data=False,
    )
    magtag.set_text("- " + quote["author"], index=2, auto_refresh=False)

magtag.refresh()

# magtag.set_text("""I practically worship your breasts.
# In my defense, though, I didn't notice how large.
# In my defense, though, I didn't notice how large
# they were until way after I'd developed
# a huge crush on you. You concealed them well.
# - Jack""", index=1)

# Set timer until midnight + 10 seconds of next day.
# Add 10 seconds as a buffer in case the clock drifts during the day,
# otherwise we might end up having to refresh multiple times.
# one_second_before_midnight = time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, 23, 59, 59, now.tm_wday, now.tm_yday, now.tm_isdst))
# ten_seconds_after_midnight_epoch = time.mktime(one_second_before_midnight) + 11
# midnight_alarm = alarm.time.TimeAlarm(epoch_time=ten_seconds_after_midnight_epoch)
# alarm.exit_and_deep_sleep_until_alarms(midnight_alarm)

# Go back to non-secret app after 20 seconds or button press.
magtag.peripherals.deinit()
pin_alarm = alarm.pin.PinAlarm(pin=board.BUTTON_D, value=False, pull=True)
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 20)
alarm.exit_and_deep_sleep_until_alarms(pin_alarm, time_alarm)