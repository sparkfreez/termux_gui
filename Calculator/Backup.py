import sys
import termuxgui as tg

with tg.Connection() as c:

    activity = tg.Activity(c)

    layout = tg.LinearLayout(activity, vertical=True)

    display = tg.TextView(activity, "0", layout)
    display.settextsize(28)

    grid = tg.GridLayout(activity, 5, 4, layout)

    # Row 1
    btn_c = tg.Button(activity, "C", grid)
    btn_back = tg.Button(activity, "⌫", grid)
    btn_div = tg.Button(activity, "/", grid)
    btn_mul = tg.Button(activity, "*", grid)

    # Row 2
    btn7 = tg.Button(activity, "7", grid)
    btn8 = tg.Button(activity, "8", grid)
    btn9 = tg.Button(activity, "9", grid)
    btn_sub = tg.Button(activity, "-", grid)

    # Row 3
    btn4 = tg.Button(activity, "4", grid)
    btn5 = tg.Button(activity, "5", grid)
    btn6 = tg.Button(activity, "6", grid)
    btn_add = tg.Button(activity, "+", grid)

    # Row 4
    btn1 = tg.Button(activity, "1", grid)
    btn2 = tg.Button(activity, "2", grid)
    btn3 = tg.Button(activity, "3", grid)
    btn_equal = tg.Button(activity, "=", grid)

    # Row 5
    btn0 = tg.Button(activity, "0", grid)
    btn_dot = tg.Button(activity, ".", grid)

    current = ""
    first = None
    operator = None

    #helper function:
    def update_display():
        if current == "":
            display.settext("0")
        else:
            display.settext(current)
          
    # Event loop (logic will be added in Part 2)
    for event in c.events():

        if event.type == tg.Event.click:

            button_map = {
                btn0.id: "0",
                btn1.id: "1",
                btn2.id: "2",
                btn3.id: "3",
                btn4.id: "4",
                btn5.id: "5",
                btn6.id: "6",
                btn7.id: "7",
                btn8.id: "8",
                btn9.id: "9",
                btn_dot.id: ".",
            }

            if event.value["id"] in button_map:
                value = button_map[event.value["id"]]

                if value == "." and "." in current:
                    continue

                current += value
                update_display()

            elif event.value["id"] == btn_c.id:
                current = ""
                first = None
                operator = None
                update_display()

        elif event.type == tg.Event.destroy and event.value["finishing"]:
            sys.exit()