import sys
import termuxgui as tg

#---voice placeholder---
def speak_number(count):
    #In part three we will replace it with android text to speech
    print(f"speaking: {count}")

last_count = -1
with tg.Connection() as c:
    activity = tg.Activity(c)

    layout = tg.LinearLayout(activity, vertical=True)

    title = tg.TextView(activity, "Fingure Count", layout)
    title.settextsize(24)

    camera_status = tg.Textview(activity, "Cam not Started", layout)
    camera_status.settextsize(18)

