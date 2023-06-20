
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window 
import instructions
import ruffier
age = 31
name = 'None'
puls1 = 1
puls2 = 1
puls3 = 1

class UserData(Screen):
    def __init__(self,name='userdata'):
        super().__init__(name=name)
        global btn_continue
        vl = BoxLayout(orientation='vertical')
        age_hl= BoxLayout(size_hint=(1,0.3))
        name_hl= BoxLayout(size_hint=(1,0.3))
        btn_continue = Button(text='Начать',size_hint=(0.3,0.2),pos_hint={'center_x':0.5})
        btn_continue.on_press = self.next
        Info_Label = Label(text=instructions.txt_instruction,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5})
        label_age = Label(text='Ваш возраст:',size_hint=(None,None),width=200,height=30,pos_hint={'center_y':0.5})
        label_name = Label(text='Ваше имя:',size_hint=(None,None),width=200,height=30,pos_hint={'center_y':0.5})
        self.age_input = TextInput(multiline=False,focus=False,size_hint=(None,None),width=200,height=30,pos_hint={'center_y':0.5})
        self.name_input= TextInput(multiline=False,focus=False,size_hint=(None,None),width=200,height=30,pos_hint={'center_y':0.5})
        age_hl.add_widget(label_age)
        age_hl.add_widget(self.age_input)
        name_hl.add_widget(label_name)
        name_hl.add_widget(self.name_input)
        vl.add_widget(Info_Label)
        vl.add_widget(name_hl)
        vl.add_widget(age_hl)
        vl.add_widget(btn_continue)
        self.add_widget(vl)
        pink = (0.94140625,0.609375,0.73046875,1)
        dark_green = (0.1953125,0.80078125,0.1953125,1)
        Window.clearcolor = pink
        btn_continue.background_color = dark_green
    def next(self):
        green = (0,1,0,1)
        global age,name 
        btn_continue.background_color = green
        age = int(self.age_input.text)
        name = self.name_input.text
        print(age,name)
        self.manager.transition.direction = 'left'
        self.manager.current = 'userpuls'
       
class UserPuls(Screen):
    def __init__(self,name='userpuls'):
        super().__init__(name=name)
        vl = BoxLayout(orientation='vertical')
        btn_continue = Button(text='Продолжить',size_hint=(0.3,None),height=100,pos_hint={'center_x':0.5})
        btn_continue.on_press = self.next
        puls_label = Label(text=instructions.txt_test1,size_hint=(0.2,None),height=200,pos_hint={'center_x':0.5})
        self.puls_input = TextInput(multiline=False,focus=False,size_hint=(0.5,None),height=30,pos_hint={'center_y':0.5})
        res_label = Label(text='Введите результат',size_hint=(0.5,None),height= 30,pos_hint={'center_y':0.5})
        input_hl = BoxLayout(size_hint=(0.5,None),height=200)
        input_hl.add_widget(res_label)
        input_hl.add_widget(self.puls_input)
        vl.add_widget(puls_label)
        vl.add_widget(input_hl)
        vl.add_widget(btn_continue)
        self.add_widget(vl)
        dark_green = (0.1953125,0.80078125,0.1953125,1)
        btn_continue.background_color = dark_green
    def next(self):
        global puls1
        puls1 = int(self.puls_input.text)
        print(puls1)
        self.manager.transition.direction = 'left'
        self.manager.current = 'usersits'
class UserSits(Screen):
    def __init__(self,name='usersits'):
        super().__init__(name=name)
        text = Label(text=instructions.txt_sits)
        btn_continue = Button(text='Продолжить',size_hint=(0.3,0.2),pos_hint={'center_x':0.5})
        btn_continue.on_press = self.next
        vl = BoxLayout(orientation='vertical')
        vl.add_widget(text)
        vl.add_widget(btn_continue)
        self.add_widget(vl)
        dark_green = (0.1953125,0.80078125,0.1953125,1)
        btn_continue.background_color = dark_green
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'userpuls2'
class UserPuls2(Screen):
    def __init__(self,name='userpuls2'):
        super().__init__(name=name)
        btn_continue = Button(text='Закончить',size_hint=(0.3,0.5),pos_hint={'center_x':0.5})
        btn_continue.on_press = self.next
        vl = BoxLayout(orientation='vertical')
        text = Label(text=instructions.txt_test3)
        res_label = Label(text='Результат',size_hint=(None,None),height=30,width=250,pos_hint={'center_y':0.5})
        res2_label = Label(text='Результат после отдыха',size_hint=(None,None),height=30,width=250,pos_hint={'center_y':0.5})
        self.res_input = TextInput(multiline=False,focus=False,size_hint=(0.2,None),height=30,pos_hint={'center_y':0.5})
        self.res2_input = TextInput(multiline=False,focus=False,size_hint=(0.2,None),height=30,pos_hint={'center_y':0.5})
        res_l = BoxLayout(size_hint=(0.6,1))
        res2_l = BoxLayout(size_hint=(0.6,1))
        res_l.add_widget(res_label)
        res_l.add_widget(self.res_input)
        res2_l.add_widget(res2_label)
        res2_l.add_widget(self.res2_input)
        vl.add_widget(text)
        vl.add_widget(res_l)
        vl.add_widget(res2_l)
        vl.add_widget(btn_continue)
        self.add_widget(vl)
        dark_green = (0.1953125,0.80078125,0.1953125,1)
        btn_continue.background_color = dark_green
    def next(self):
        global puls2,puls3
        puls2 = int(self.res_input.text)
        puls3 = int(self.res2_input.text)
        print(name,age)
        self.manager.transition.direction = 'left'
        self.manager.current = 'result'
class Result(Screen):
    def __init__(self,name='result'):
        super().__init__(name=name)
        self.lb = Label(text='')
        self.add_widget(self.lb)
        self.printResult()
        
    def printResult(self):
        global puls1,puls2,puls3,age
        print(puls1,puls2,puls3,age)
        self.lb.text = text=str(ruffier.test(puls1,puls2,puls3,age))

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(UserData())
        sm.add_widget(UserPuls())
        sm.add_widget(UserSits())
        sm.add_widget(UserPuls2())
        sm.add_widget(Result())
        return sm
TestApp().run()
        
