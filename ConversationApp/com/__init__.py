from kivy.uix.label import Label
from kivy.app import App

class FirstKivy(App):
    def build(self):
        return Label(text="Hello World")

if __name__ == '__main__':
    FirstKivy().run()
