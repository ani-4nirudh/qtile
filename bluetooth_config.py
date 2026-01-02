from libqtile import widget

def create_blt_widget(font, fontsize):
    return widget.Bluetooth(
            default_show_battery=True,
            device_battery_format='({battery}%)',
            font=font,
            fontsize=fontsize,
            fmt='{}',
            )
