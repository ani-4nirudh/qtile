from libqtile import widget
from libqtile.lazy import lazy

def create_screenshot():
    # Select area with mouse
    keys.append(
        Key([mod, "shift"], "s", 
        lazy.spawn("scrot -s ${HOME}/Pictures/screenshot_%Y_%m_%d-%H%M%S.png"), 
        desc="Screenshot selection"),
    )
