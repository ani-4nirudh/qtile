from libqtile import widget

def create_keyboard_widget(font, fontsize, foreground=None, background=None):
    return widget.KeyboardLayout(
            configured_keyboards = ['us', 'de'],
            display_map = {'us':'us', 'de':'de'},
            name = 'keyboardlayout',
            fmt = '\uf11c  {}',
            font = font,
            fontsize = fontsize,
            foreground=foreground,
            padding=10
            )
