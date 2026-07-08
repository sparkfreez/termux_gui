import sys
import termuxgui as tg

with tg.Connection() as c:
    activity = tg.Activity(c)

    layout = tg.LinearLayout(activity, vertical=True)

    text = tg.TextView(activity, "Hello", layout)

    button = tg.Button(activity, "Click Me", layout)

    for ev in c.events():
        if ev.type == tg.Event.destroy and ev.value["finishing"]:
            sys.exit()