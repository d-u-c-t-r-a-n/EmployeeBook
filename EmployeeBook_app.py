'''
Created Date: Saturday October 19th 2019
Author: Duc Tran (duc.tran3@carleton.ca)
Carleton ID: 101158742
'''

'''
This program tries to design a GUI for the nail salons operation. 
Since nail technicians share the revenue with owners, 
this program aims to create an interface for employees 
to enter what services they performed, and record into an excel file
for the owner bookkepping.
This program was written in Python because I was familiar with the language,
despite the fact that other languages have better performance on designing GUI.
This program was written without prior knowledge about GUI, and completed after 14 days
'''
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

import pandas as pd
import datetime
import ductran_gui_helper as hp

#global excel file
file_path = r'/Users/ductran/Documents/GUI/worktest.xlsx'
df_dict = hp.import_excel_return_dict(file_path)


current_employee = ''
current_service = ''
current_price = 0
today_date = str((datetime.datetime.now().date()))

class NamePage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #Main Layout
        self.cols = 1
        self.add_widget(Label(text="WELCOME TO EMPLOYEE BOOK"))
        self.name = TextInput(multiline=False)

        #defining more Layout
        self.front_layout = GridLayout()
        self.front_layout.cols = 2
        
        #add rows add a row 
        # self.add_widget(Label(text="Date:"))
        # self.date = TextInput(multiline=False)
        # self.add_widget(self.date)

        #add employee
        self.add_widget(self.front_layout) #putting another layout into main layout

            #button in the second layout put in main layout
        self.employee1 = Button (text="Trang")
        self.employee1.bind(on_press=self.employee1_button)        
        self.front_layout.add_widget(self.employee1)

        self.employee2 = Button (text="Quynh")
        self.employee2.bind(on_press=self.employee2_button)        
        self.front_layout.add_widget(self.employee2)

        self.employee3 = Button (text="Thao")
        self.employee3.bind(on_press=self.employee3_button)        
        self.front_layout.add_widget(self.employee3)

        self.employee4 = Button (text="Nghia")
        self.employee4.bind(on_press=self.employee4_button)        
        self.front_layout.add_widget(self.employee4)

    def employee1_button (self,instance):            
        print (f"{self.employee1.text} is selecting...")
        global current_employee
        current_employee = 'Trang'
        employeebook.pricing_page
        employeebook.screen_manager.current = "Pricing"

    def employee2_button (self,instance):            
        print (f"{self.employee2.text} is selecting...")
        global current_employee
        current_employee = 'Quynh'
        employeebook.pricing_page
        employeebook.screen_manager.current = "Pricing"

    def employee3_button (self,instance):              
        print (f"{self.employee3.text} is selecting...")
        global current_employee
        current_employee = 'Thao'
        employeebook.pricing_page
        employeebook.screen_manager.current = "Pricing"

    def employee4_button (self,instance):             
        print (f"{self.employee4.text} is selecting...")
        global current_employee
        current_employee = 'Nghia'
        employeebook.pricing_page
        employeebook.screen_manager.current = "Pricing"

class PricingPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Main Layout
        self.cols = 1
        self.add_widget(Label(text="PLEASE CHOOSE A SERVICE"))
        self.name = TextInput(multiline=False)

        #defining second layout
        self.front_layout = GridLayout()
        self.front_layout.cols = 3
        self.add_widget(self.front_layout) #putting another layout into main layout

        self.nails = Button(text="Nails")
        self.nails.bind(on_press=self.nails_button)
        self.front_layout.add_widget(self.nails)

        self.wax = Button(text="Wax")
        self.wax.bind(on_press=self.wax_button)
        self.front_layout.add_widget(self.wax)

        self.extra = Button(text="Extra")
        self.extra.bind(on_press=self.extra_button)
        self.front_layout.add_widget(self.extra)

    def nails_button (self,instance):
        print("Nails")
        employeebook.nails_page
        employeebook.screen_manager.current = "Nails"
    
    def wax_button (self,instance):
        print("Wax")
        employeebook.wax_page
        employeebook.screen_manager.current = "Wax"

    def extra_button (self,instance):
        print("Extra")
        employeebook.extra_page
        employeebook.screen_manager.current = "Extra"

class NailsPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="PLEASE CHOOSE A SERVICE"))
        self.name = TextInput(multiline=False)

        #defining second layout
        self.front_layout = GridLayout()
        self.front_layout.cols = 2
        self.add_widget(self.front_layout) #putting another layout into main layout

        self.nails_dippowder = Button(text="Dip Powder")
        self.nails_dippowder.bind(on_press=self.nails_dippowder_button)
        self.front_layout.add_widget(self.nails_dippowder)
        
        #rename nails services here
        self.nails_1 = Button(text="nails_1")
        self.nails_1.bind(on_press=self.nails_1_button)
        self.front_layout.add_widget(self.nails_1)

        self.nails_2 = Button(text="nails_2")
        self.nails_2.bind(on_press=self.nails_2_button)
        self.front_layout.add_widget(self.nails_2)

        self.nails_3 = Button(text="nails_3")
        self.nails_3.bind(on_press=self.nails_3_button)
        self.front_layout.add_widget(self.nails_3)

        self.nails_4 = Button(text="nails_4")
        self.nails_4.bind(on_press=self.nails_4_button)
        self.front_layout.add_widget(self.nails_4)
        
        self.nails_5 = Button(text="nails_5")
        self.nails_5.bind(on_press=self.nails_5_button)
        self.front_layout.add_widget(self.nails_5)

        self.nails_6 = Button(text="nails_6")
        self.nails_6.bind(on_press=self.nails_6_button)
        self.front_layout.add_widget(self.nails_6)

        self.nails_7 = Button(text="nails_7")
        self.nails_7.bind(on_press=self.nails_7_button)
        self.front_layout.add_widget(self.nails_7)

        self.nails_8 = Button(text="nails_8")
        self.nails_8.bind(on_press=self.nails_8_button)
        self.front_layout.add_widget(self.nails_8)

        self.nails_9 = Button(text="nails_9")
        self.nails_9.bind(on_press=self.nails_9_button)
        self.front_layout.add_widget(self.nails_9)

    def nails_dippowder_button(self,instance):
        print ("Dip Powder")
        global current_service
        current_service = 'Dip Powder'
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"
    
    def nails_1_button(self,instance):
        print ("Nails service #1")
        global current_service
        current_service = "Nails service #1"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"
    
    def nails_2_button(self,instance):
        print ("Nails service #2")
        global current_service
        current_service = "Nails service #2"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

    def nails_3_button(self,instance):
        print ("Nails service #3")
        global current_service
        current_service = "Nails service #3"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

    def nails_4_button(self,instance):
        print ("Nails service #4")
        global current_service
        current_service = "Nails service #4"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

    def nails_5_button(self,instance):
        print ("Nails service #5")
        global current_service
        current_service = "Nails service #5"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

    def nails_6_button(self,instance):
        print ("Nails service #6")
        global current_service
        current_service = "Nails service #6"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

    def nails_7_button(self,instance):
        print ("Nails service #7")
        global current_service
        current_service = "Nails service #7"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

    def nails_8_button(self,instance):
        print ("Nails service #8")
        global current_service
        current_service = "Nails service #8"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

    def nails_9_button(self,instance):
        print ("Nails service #9")
        global current_service
        current_service = "Nails service #9"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

class WaxPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="PLEASE CHOOSE A SERVICE"))
        self.name = TextInput(multiline=False)

        #defining second layout
        self.front_layout = GridLayout()
        self.front_layout.cols = 2
        self.add_widget(self.front_layout) #putting another layout into main layout

        self.wax_eyebrows = Button (text="Eyebrows")
        self.wax_eyebrows.bind(on_press=self.wax_eyebrows_button)
        self.front_layout.add_widget(self.wax_eyebrows)

        self.wax_chest = Button (text="Chest Wax")
        self.wax_chest.bind(on_press=self.wax_chest_button)
        self.front_layout.add_widget(self.wax_chest)

        self.wax_fullleg = Button (text="Full Leg Wax")
        self.wax_fullleg.bind(on_press=self.wax_fullleg_button)
        self.front_layout.add_widget(self.wax_fullleg)

        self.wax_halfleg = Button (text="Half Leg Wax")
        self.wax_halfleg.bind(on_press=self.wax_halfleg_button)
        self.front_layout.add_widget(self.wax_halfleg)

    def wax_eyebrows_button(self,instance):
        print ("Eyebrows")
        global current_service
        current_service = "Eyebrows Wax"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

    def wax_chest_button(self,instance):
        print ("Chest Wax")
        global current_service
        current_service = "Chest Wax"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

    def wax_fullleg_button(self,instance):
        print ("Full Leg")
        global current_service
        current_service = "Full Leg Wax"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

    def wax_halfleg_button(self,instance):
        print ("Half Leg")
        global current_service
        current_service = "Half Leg Wax"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

class ExtraPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Main Layout
        self.cols = 1
        self.add_widget(Label(text="PLEASE CHOOSE A SERVICE"))
        self.name = TextInput(multiline=False)

        #defining second layout
        self.front_layout = GridLayout()
        self.front_layout.cols = 1
        self.add_widget(self.front_layout) #putting another layout into main layout

        self.extra = Button(text="Extra")
        self.extra.bind(on_press=self.extra_button)
        self.front_layout.add_widget(self.extra)

    def extra_button(self,instance):
        print ("Extra")
        global current_service
        current_service = "Extra"
        employeebook.submit_page
        employeebook.screen_manager.current = "Submit"

class SubmitPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #Main Layout
        self.cols = 1
        self.add_widget(Label(text="ARE YOU SURE?"))
        self.name=TextInput(multiline=False)

        #defining for Layout
        self.front_layout = GridLayout()
        self.front_layout.cols = 2

        #add button in the second layout
        self.add_widget(self.front_layout)
        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.submit_button)
        self.front_layout.add_widget(self.submit)

        self.cancel = Button(text="Cancel")
        self.cancel.bind(on_press=self.cancel_button)
        self.front_layout.add_widget(self.cancel)
    
    def submit_button(self,instance):
        global df_dict, current_employee, current_service, file_path
        hp.add_new_service_to_df(df_dict,today_date,current_employee,current_service)
        hp.add_data_to_excel(df_dict,file_path)

        #reset global values        
        current_employee = ''
        current_service = ''

        employeebook.tryagain_page
        employeebook.screen_manager.current = "Tryagain"

    def cancel_button(self,instance):
        global current_employee, current_service
        #reset global values        
        current_employee = ''
        current_service = ''

        employeebook.cancelled_page
        employeebook.screen_manager.current = "Cancelled"

class TryagainPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.add_widget(Label(text="THANK YOU\nYour submission was recorded!\nWould you like to submit another service?"))
        self.name = TextInput(multiline=False)
        
        #defining second layout
        self.front_layout = GridLayout()
        self.front_layout.cols = 2
        self.add_widget(self.front_layout) #putting another layout into main layout

        self.tryagain = Button(text="Try again")
        self.tryagain.bind(on_press=self.tryagain_button)
        self.front_layout.add_widget(self.tryagain)

        self.quit = Button(text="Quit")
        self.quit.bind(on_press=self.quit_button)
        self.front_layout.add_widget(self.quit)
    
    def tryagain_button(self,instance):
        employeebook.name_page
        employeebook.screen_manager.current = "Name"
    
    def quit_button(self,instance):
        employeebook.stop()

class CancelledPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.add_widget(Label(text="Your submission was cancelled\nWould you like to submit another service?"))
        self.name = TextInput(multiline=False)
        
        #defining second layout
        self.front_layout = GridLayout()
        self.front_layout.cols = 2
        self.add_widget(self.front_layout) #putting another layout into main layout

        self.tryagain = Button(text="Try again")
        self.tryagain.bind(on_press=self.tryagain_button)
        self.front_layout.add_widget(self.tryagain)

        self.quit = Button(text="Quit")
        self.quit.bind(on_press=self.quit_button)
        self.front_layout.add_widget(self.quit)
    
    def tryagain_button(self,instance):
        employeebook.name_page
        employeebook.screen_manager.current = "Name"
    
    def quit_button(self,instance):
        employeebook.stop()

class EmployeeBook(App):
    def build(self):
        self.screen_manager = ScreenManager()

        #Main Page
        self.name_page = NamePage()
        screen = Screen(name="Name")
        screen.add_widget(self.name_page)
        self.screen_manager.add_widget(screen)

        #Pricing Page
        self.pricing_page = PricingPage()
        screen = Screen(name="Pricing")
        screen.add_widget(self.pricing_page)
        self.screen_manager.add_widget(screen)

        #Nails Page
        self.nails_page = NailsPage()
        screen = Screen(name="Nails")
        screen.add_widget(self.nails_page)
        self.screen_manager.add_widget(screen)

        #Wax Page
        self.wax_page = WaxPage()
        screen = Screen(name="Wax")
        screen.add_widget(self.wax_page)
        self.screen_manager.add_widget(screen)

        #Extra Page
        self.extra_page = ExtraPage()
        screen = Screen(name="Extra")
        screen.add_widget(self.extra_page)
        self.screen_manager.add_widget(screen)

        #Submit Page
        self.submit_page = SubmitPage()
        screen = Screen(name="Submit")
        screen.add_widget(self.submit_page)
        self.screen_manager.add_widget(screen)

        #Try again Page
        self.tryagain_page = TryagainPage()
        screen = Screen(name="Tryagain")
        screen.add_widget(self.tryagain_page)
        self.screen_manager.add_widget(screen)

        #Cancelled Page
        self.cancelled_page = CancelledPage()
        screen = Screen(name="Cancelled")
        screen.add_widget(self.cancelled_page)
        self.screen_manager.add_widget(screen)
        
        return self.screen_manager

if __name__ == "__main__":
    employeebook = EmployeeBook()
    employeebook.run()