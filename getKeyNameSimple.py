import keyboard

print("Press any key... (Press Esc to exit)")


# Define a function to log key presses
def log_key_event(event):
    print(f"Key pressed: {event.name}")


# Hook the key press event to the log function
keyboard.on_press(log_key_event)

# Keep the script running until 'Esc' is pressed
keyboard.wait('esc')
