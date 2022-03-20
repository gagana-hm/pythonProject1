import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class SpartanGrid(GridLayout):
    def __init__(self,**kwargs):
        super(SpartanGrid,self).__init__()

        self.add_widget(Label(text="student name:"))

        self.s_name = TextInput(multiline=False)
        self.add_widget(self.s_name)



class SpartanApp(App):
    def build(self):
        return SpartanGrid()


if __name__ == "__main__":
    SpartanApp().run()
