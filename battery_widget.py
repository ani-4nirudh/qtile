from libqtile import widget
from libqtile.widget.battery import thunderbolt_smart_charge

def create_battery_widget(font, fontsize, foreground=None, background=None):
    return widget.Battery(
            charge_controller=lambda: (40, 80),
            fmt="{}",
            format="{char} {percent:2.0%}",
            battery=0,
            charge_char = '󰂄',
            discharge_char = '󱟞',
            not_charging_char='󰂁',
            full_char='󰁹',
            low_percentage=0.25,
            low_foreground='FF0000',
            low_background=None,
            update_interval=60,
            padding=10,
            font=font,
            fontsize=fontsize,
            foreground=foreground,
            background=background
        )
