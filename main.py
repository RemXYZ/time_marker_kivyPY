import sys
import os

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


Builder.load_file(resource_path('design.kv'))

if __name__ != '__main__':
    exit()

class MyLayout(Widget):
    pass

class TimeMarkerApp(App):
    def build(self):
        # Window.clearcolor = (1,1,1,1)
        return MyLayout()

# Set size of window
Window.size = (500,700)

TimeMarkerApp().run()