import os
from libqtile.lazy import lazy

@lazy.function
def create_screenshot(qtile):
    pictures = os.path.expanduser("~/Pictures")
    
    # Create a directory if it does not exist
    if not os.path.exists(pictures):
        os.makedirs(pictures)

    # Save the screenshot with the timestamp
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = f"{pictures}/{filename}"

    # Execute the screenshot command
    qtile.spawn(f"scrot -s {filepath}")
