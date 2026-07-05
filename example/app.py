import sys
import termuxgui as tg

# 1. Establish connection to the Termux:GUI plugin framework
with tg.Connection() as c:
    
    # 2. Spin up a brand new Android native display activity view layer
    activity = tg.Activity(c)
    
    # 3. Create a vertical layout container
    layout = tg.LinearLayout(activity, vertical=True)
    
    # 4. Generate native widgets (Format: Activity, Text/Data, Parent Layout)
    label = tg.TextView(activity, "Enter your message:", layout)
    input_field = tg.EditText(activity, "", layout)
    button = tg.Button(activity, "Submit text", layout)
    output_label = tg.TextView(activity, "", layout)
    
    # 5. Core Event Loop to actively intercept touch inputs and close requests
    for event in c.events():
        
        # Intercept native click event instances tied to the push button
        if event.type == tg.Event.click and event.value["id"] == button.id:
            
            # FIX: In termuxgui, you pass a callback function to get the text asynchronously.
            # We use a lambda function to receive the string from Android and update the output label.
            input_field.get_text(lambda user_text: output_label.set_text(f"Resulting Output: {user_text}"))
            
        # Cleanly shut down execution if the terminal or window destroys
        if event.type == tg.Event.destroy and event.value["finishing"]:
            sys.exit()
