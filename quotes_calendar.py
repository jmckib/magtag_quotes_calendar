import json
import random
import time
from adafruit_magtag.magtag import MagTag

weekdays = ("Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun")
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

def main():
    magtag = MagTag()

    # Date label
    magtag.add_text(
        text_font="/fonts/SUPERSCR-24.pcf",
        text_position=(130, 6),
        text_anchor_point=(0.5,0),
        is_data=False,
    )

    now = time.localtime()

    magtag.set_background("/images/months/background-" + months[now.tm_mon - 1].lower() + ".bmp")

    quotes = json.load(open("quotes.json"))
    SEED = 1
    random.seed(SEED)
    quotes = sorted(quotes, key=lambda i: random.random())

    # Start over every 6 months.
    quote = quotes[(now.tm_yday - 1) % 183]
    has_author = "author" in quote

    def suffix(d):
        return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

    magtag.set_text("%s, %s %s%s" % (weekdays[now.tm_wday], months[now.tm_mon - 1], now.tm_mday, suffix(now.tm_mday)), auto_refresh=False)

    position_no_author = (magtag.graphics.display.width // 2, magtag.graphics.display.height // 2 + 15 + quote.get("height-offset", 0))
    position_with_author = (magtag.graphics.display.width // 2, magtag.graphics.display.height // 2 + 8 + quote.get("height-offset", 0))

    # Quote label
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


    magtag.peripherals.deinit()