from libqtile import widget
from libqtile.lazy import lazy

def create_volume_widget(font, fontsize, foreground=None, background=None):
    return widget.Volume(
            volume_app="pamixer",
            step=2,
            font=font,
            fontsize=fontsize,
            foreground=foreground,
            background=background,
            mouse_callbacks={'Button1':lazy.spawn("pamixer --toggle-mute")},
            update_interval=0.2,
            emoji=True,
            emoji_list=["\ueee8","\uf026","\uf027","\uf028"],
            # fmt="{emoji} {volume}%",
            unmute_format='{volume}%',
            padding=5,
            get_volume_command="pamixer --get-volume-human"
            )
