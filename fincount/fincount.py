import sys
import termuxgui as tg

camera = "None"
running = False

with tg.Connection() as c:

    activity = tg.Activity(c)

    layout = tg.LinearLayout(activity, vertical=True)

    title = tg.TextView(activity, "Finget Counter", layout)
    title.settextsize(24)

    status = tg.TextView(activity, "Status Idle", layout)
    status.settextsize(18)

    camera_label = tg.TextView(activity, "Camera: None", layout)
    camera_label.settextsize(18)

    preview = tg.TextView(activity, "\n\nCamera Preview\n(Coming in Part 3)\n", layout)
    preview.settextsize(20)

    finger_count = tg.TextView(activity, "Fingers: 0", layout)
    finger_count.settextsize(30)

    front_btn = tg.Button(activity, "Front Camera", layout)
    rear_btn = tg.Button(activity, "Rear Camera"          , layout)
    start_btn = tg.Button(activity, "Start Camera"          , layout)
    stop_btn = tg.Button(activity, "Stop Camera"          , layout)
    exit_btn = tg.Button(activity, "Exit"                    , layout)
