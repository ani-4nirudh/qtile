# ('connected_colour', '#4169e1'),
# ('disconnected_colour', '#ff6f00'),

from libqtile import widget, bar
from libqtile.utils import guess_terminal
import subprocess

class VPNStatus(widget.TextBox):
    defaults = [
        ('update_interval', 4),
        ('connected_text', '󰖂 '),
        ('disconnected_text', '󰖂 '),
        ('connected_colour', '#0096ff'),
        ('disconnected_colour', '#ff6f00'),
        ('width', bar.CALCULATED),
        ('padding', 5)
    ]

    def __init__(self, **config):
        widget.TextBox.__init__(self, text=" 󰖂 ", **config)  # Start with icon
        self.add_defaults(VPNStatus.defaults)
        self.add_callbacks({'Button1': self.toggle_vpn})

    def _configure(self, qtile, bar):
        widget.TextBox._configure(self, qtile, bar)
        self.poll()
        self.timeout_add(self.update_interval, self.poll)

    def poll(self):
        try:
            result = subprocess.run(
                ["ip", "link", "show", "nordlynx"],
                capture_output=True,
                timeout=2
            )
            connected = result.returncode == 0
            
            # Update text AND force layout update
            new_text = self.connected_text if connected else self.disconnected_text
            new_color = self.connected_colour if connected else self.disconnected_colour
            
            if self.text != new_text or self.foreground != new_color:
                self.foreground = new_color
                self.update(new_text)
            
        except Exception as e:
            self.update("?")
        
        return self.update_interval

    def _vpn_connected(self):
        try:
            result = subprocess.run(
                ["ip", "link", "show", "nordlynx"],
                capture_output=True,
                timeout=2
            )
            return result.returncode == 0
        except:
            return False

    def toggle_vpn(self):
        try:
            cmd = ['nordvpn', 'd'] if self._vpn_connected() else ['nordvpn', 'c', 'India', "Mumbai"]
            subprocess.run(cmd, check=True, capture_output=True, timeout=5)
            self.poll()
            self.bar.draw()
        except:
            pass
