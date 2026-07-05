import sys
import termuxgui as tg

with tg.Connection() as c:

    # Create activity
    activity = tg.Activity(c)

    # Vertical layout
    layout = tg.LinearLayout(activity, vertical=True)

    # Title
    tg.TextView(activity, "Simple Calculator", layout)

    # First number
    tg.TextView(activity, "First Number:", layout)
    num1 = tg.EditText(activity, "", layout)

    # Second number
    tg.TextView(activity, "Second Number:", layout)
    num2 = tg.EditText(activity, "", layout)

    # Buttons
    add_btn = tg.Button(activity, "Add (+)", layout)
    sub_btn = tg.Button(activity, "Subtract (-)", layout)
    mul_btn = tg.Button(activity, "Multiply (*)", layout)
    div_btn = tg.Button(activity, "Divide (/)", layout)

    # Result
    result = tg.TextView(activity, "Result: ", layout)

    # Event loop
    for event in c.events():

        if event.type == tg.Event.click:

            try:
                a = float(num1.gettext())
                b = float(num2.gettext())

                if event.value["id"] == add_btn.id:
                    result.settext(f"Result: {a + b}")

                elif event.value["id"] == sub_btn.id:
                    result.settext(f"Result: {a - b}")

                elif event.value["id"] == mul_btn.id:
                    result.settext(f"Result: {a * b}")

                elif event.value["id"] == div_btn.id:
                    if b == 0:
                        result.settext("Error: Cannot divide by zero")
                    else:
                        result.settext(f"Result: {a / b}")

            except ValueError:
                result.settext("Please enter valid numbers.")

        elif event.type == tg.Event.destroy and event.value["finishing"]:
            sys.exit()