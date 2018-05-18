import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from re import findall, MULTILINE, sub

heading = []
date = []
id_ref = []



class ScreenOne(Screen):

    def __init__ (self,**kwargs):
        lista = [15, 12, 23 ,63]
        super (ScreenOne, self).__init__(**kwargs)
        Buttonlayout = GridLayout(orientation='vertical',cols=1, spacing=2, size_hint_y=None)
        Buttonlayout.bind(minimum_height=Buttonlayout.setter('height'))
        for i in range(len(id_ref)):
            btn = Button(text=str( lista[i]), size_hint_y=None, height=80,text_size=(350,None),font_size='12sp')
            btn.bind(on_press=(lambda a:self.changer()))
            Buttonlayout.add_widget(btn)
        root = ScrollView()
        root.add_widget(Buttonlayout)
        self.add_widget(root)

    def changer(self,*args):
        self.manager.current = 'story_screen'

class ScreenTwo(Screen):

    def __init__(self,**kwargs):
        super (ScreenTwo,self).__init__(**kwargs)
        story_box = BoxLayout(orientation='vertical')
        story_heading = Label(text="testing")
        back = Button(text="Back",size_hint_y=None, size_y=50)
        back.bind(on_press=self.changer)
        story_box.add_widget(story_heading)
        story_box.add_widget(back)
        self.add_widget(story_box)

    def changer(self,*args):
        self.manager.current = 'but_screen'

class TestApp(App):

    def build(self):
        my_screenmanager = ScreenManager()
        screen1 = ScreenOne(name='but_screen')
        screen2 = ScreenTwo(name='story_screen')
        my_screenmanager.add_widget(but_screen)
        my_screenmanager.add_widget(story_screen)
        return my_screenmanager

if __name__ == '__main__':
    TestApp().run()