from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
#from kivy.properties import ObjectProperty
#import math
#import os
#from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.uix.image import AsyncImage
from kivy.core.window import Window
#from kivy.app import runTouchApp
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols
from kivy.uix.togglebutton import ToggleButton


class Toggle_btn(GridLayout): 
    def __init__(self, **kwargs):
        super(Toggle_btn, self).__init__(**kwargs)
        self.cols = 2
        
        self.tb1 = ToggleButton(text = 'DOWN', group = 'dir',state = 'down')
        self.add_widget(self.tb1)
        
        self.tb2 = ToggleButton(text = 'UP', group = 'dir')
        self.add_widget(self.tb2)
        
    def get_state(self):
        return [self.tb1.state, self.tb2.state]
    
    
class Toggle_btn_moment(GridLayout): 
    def __init__(self, **kwargs):
        super(Toggle_btn_moment, self).__init__(**kwargs)
        self.cols = 2
        
        self.tb1 = ToggleButton(text = 'CLOCK', group = 'dir',state = 'down')
        self.add_widget(self.tb1)
        
        self.tb2 = ToggleButton(text = 'ANTI-CLOCK', group = 'dir')
        self.add_widget(self.tb2)
        
    def get_state(self):
        return [self.tb1.state, self.tb2.state]


class Panel(FloatLayout):
    
    def __init__(self, **kwargs):
        super(Panel, self).__init__(**kwargs)
        
        self.E = "210E9"
        self.I = "1.71E-6"
        self.Len = '10'
        self.reaction_vars = []
        self.BEAM = Beam(self.Len, self.E, self.I)
        
        self.add_widget(Label(text = 'BEAM SOLVER', size_hint = (1, 0.1), pos_hint = {'x' : 0, 'y' : 0.9}, color = (0, 0, 0, 1)))
        self.add_widget(Label(text = 'MAKE BEAM', size_hint = (.3, 0.1), pos_hint = {'x' : 0, 'y' : 0.8}, color = (0, 255, 0, 1)))
        
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None, size_hint_x = 1)
        
        layout.bind(minimum_height=layout.setter('height'))
        
        #Button which upon clicking show default values of E, I and length and allows user to change them
        default_val = Button(text = 'SET E, I, L', size_hint_y=None, height=40)
        layout.add_widget(default_val)
        default_val.bind(on_press = self.popup_default_value)
        
        """Len = Button(text = 'LENGTH', size_hint_y=None, height=40)
        layout.add_widget(Len)
        Len.bind(on_press = self.popup_len)
        """
        layout.add_widget(Label(text = 'SUPPORTS', size_hint_y=None, height=40, color = (0, 255, 0, 1)))
        
        Fix = Button(text = 'FIX', size_hint_y=None, height=40)
        layout.add_widget(Fix)
        Fix.bind(on_press = self.popup_fix)
        
        Roller = Button(text = 'ROLLER', size_hint_y=None, height=40)
        layout.add_widget(Roller)
        Roller.bind(on_press = self.popup_roller)
        
        Pin = Button(text = 'PIN', size_hint_y=None, height=40)
        layout.add_widget(Pin)
        Pin.bind(on_press = self.popup_pin)
        
        layout.add_widget(Label(text = 'LOADS', size_hint_y=None, height=40, color = (0, 255, 0, 1)))
        
        layout.add_widget(Label(text = 'CONCENTRATED', size_hint_y=None, height=40,color = (0, 255, 0, 1)))
        
        Vertical = Button(text = 'VERTICAL', size_hint_y=None, height=40)
        layout.add_widget(Vertical)
        Vertical.bind(on_press = self.popup_vertical)
        
        Moment = Button(text = 'MOMENT', size_hint_y=None, height=40)
        layout.add_widget(Moment)
        Moment.bind(on_press = self.popup_moment)
        
        layout.add_widget(Label(text = 'DISTRIBUTED', size_hint_y=None, height=40, color = (0, 255, 0, 1)))
        
        Linear = Button(text = 'LINEAR', size_hint_y=None, height=40)
        layout.add_widget(Linear)
        Linear.bind(on_press = self.popup_linear)
        
        NewBeam = Button(text = 'NEW BEAM', size_hint_y=None, height=40)
        layout.add_widget(NewBeam)
        NewBeam.bind(on_press = self.popup_newbeam)
        
        MakeBeam = ScrollView(size_hint=(.3, .8))
        MakeBeam.add_widget(layout)
        self.add_widget(MakeBeam)
        
        layoutSol1 = GridLayout(cols=1, spacing=10, size_hint_y=None, size_hint_x = 1)
        self.add_widget(Label(text = 'PLOT GRAPH', size_hint = (.35, .1), pos_hint = {'x' : 0.3, 'y' : .8}, color = (0, 255, 0, 1)))
        self.add_widget(Label(text = 'FIND VALUES', size_hint = (.35, .1), pos_hint = {'x' : .65, 'y' : .8}, color = (0, 255, 0, 1)))
        layoutSol1.bind(minimum_height=layoutSol1.setter('height'))
        
        Shear = Button(text = 'SHEAR FORCE DIAGRAM', size_hint_y=None, height=20)
        layoutSol1.add_widget(Shear)
        Shear.bind(on_press = self.popup_shear)
        
        Bending = Button(text = 'BENDING MOMENT DIAGRAM', size_hint_y=None, height=20)
        layoutSol1.add_widget(Bending)
        Bending.bind(on_press = self.popup_bending)
        
        Slope = Button(text = 'SLOPE DIAGRAM', size_hint_y=None, height=20)
        layoutSol1.add_widget(Slope)
        Slope.bind(on_press = self.popup_slope)
        
        Deflection = Button(text = 'DEFLECTION DIAGRAM', size_hint_y=None, height=20)
        layoutSol1.add_widget(Deflection)
        Deflection.bind(on_press = self.popup_deflection)
        
        PlotAll = Button(text = 'PLOT ALL OF THE ABOVE', size_hint_y=None, height=20)
        layoutSol1.add_widget(PlotAll)
        PlotAll.bind(on_press = self.popup_plotall)
        
        Plot = ScrollView(size_hint=(.35, .2), pos_hint = {'x' : .3, 'y' : .6})
        Plot.add_widget(layoutSol1)
        self.add_widget(Plot)
        
        layoutSol2 = GridLayout(cols=1, spacing=10, size_hint_y=None, size_hint_x = 1)
        layoutSol2.bind(minimum_height=layoutSol1.setter('height'))
        Reaction = Button(text = 'REACTION LOADS', size_hint_y=None, height=15)
        layoutSol2.add_widget(Reaction )
        Reaction.bind(on_press = self.popup_reaction)
        
        #Cflexure = Button(text = 'CFLEXURE', size_hint_y=None, height=15)
        #layoutSol2.add_widget(Cflexure)
        #Cflexure.bind(on_press = self.popup_cflexure)
        
        Fvalue = ScrollView(size_hint = (.35, .2), pos_hint = {'x' : .65, 'y' : .6})
        Fvalue.add_widget(layoutSol2)
        self.add_widget(Fvalue)
        
    def popup_default_value(self, instance):
        #layout = BoxLayout(orientation = 'vertical')
        
        #layout1 is our child wiget of layout and is GridLayout with coloumn = 2
        layout1 = GridLayout(cols = 2)
        
        #layout1's child widget Label
        layout1.add_widget(Label(text = 'E () = '))
        
        #layout1's child widget having value of E
        self.E_text = TextInput(text = self.E,multiline = False)
        layout1.add_widget(self.E_text)
        
        #layout1's child widget Label
        layout1.add_widget(Label(text = 'I () = '))
         
        #layout1's another child widget having value of E
        self.I_text = TextInput(text = self.I,multiline = False)
        layout1.add_widget(self.I_text)
        
        #layout1's child widget Label
        layout1.add_widget(Label(text = 'LENGTH (m) = '))
         
        #layout1's another child widget having value of length of beam
        self.len_text = TextInput(text = self.Len,multiline = False)
        layout1.add_widget(self.len_text)
        
        #Button to save the changes done
        btn = Button(text = 'SAVE')
        layout1.add_widget(btn)
        btn.bind(on_press = self.set_E_I_Len)
        
        #Button to accept the default values and close the popup
        btn2 = Button(text = 'CLOSE')
        layout1.add_widget(btn2)
        btn2.bind(on_press = self.popup_dismiss)
        
        #layout.add_widget(layout1)
        
        #Instantiating the Popup 
        self.popup = Popup(title = 'SET E, I  AND LENGTH FOR BEAM', content = layout1, size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
        self.popup.open()
        
        
    """def popup_len(self, instance):
         #Popup has layout which is a Box Layout as the main layout
         layout = BoxLayout(orientation = 'vertical')
         
         #layout's child widget -- a TextInput widget
         self.len_text = TextInput(multiline = False)
         layout.add_widget(self.len_text)
         
         #layout's  another child widget -- a Button to save the lenth and Button binding with a function self.len_of_beam 
         self.btn = Button(text = 'SAVE')
         self.btn.bind(on_press = self.len_of_beam)
         layout.add_widget(self.btn)
         
         #layout's  another child widget -- a Button to dismiss the Popup and Button binding with a function self.len_of_beam 
         self.btn2 = Button(text = 'SAVE')
         self.btn2.bind(on_press = self.popup_dismiss)
         layout.add_widget(self.btn2)
         
         #Instantiating the Popup 
         self.popup = Popup(title = 'LENTH (m)', content = layout, size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
         
         self.popup.open() 
    """     
         
      
    def popup_fix(self, instance):
        
         layout = GridLayout(cols = 2)
         
         layout.add_widget(Label(text = 'X (m) = '))
         
         self.fix_text = TextInput(multiline = False)
         layout.add_widget(self.fix_text)
         
         
         btn = Button(text = 'SAVE')
         layout.add_widget(btn)
         btn.bind(on_press = self.add_fix)
         
         btn2 = Button(text = 'CLOSE')
         layout.add_widget(btn2)
         btn2.bind(on_press = self.popup_dismiss)
         
         self.popup = Popup(title = 'FIX SUPPPORT (m)', content = layout, size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
         self.popup.open() 
         
    def popup_roller(self, instance):
        
         
         layout = GridLayout(cols = 2)
         
         layout.add_widget(Label(text = 'X (m) = '))
         
         self.roller_text = TextInput(multiline = False)
         layout.add_widget(self.roller_text)
         
         btn = Button(text = 'SAVE')
         layout.add_widget(btn)
         btn.bind(on_press = self.add_roller)
         
         btn2 = Button(text = 'CLOSE')
         layout.add_widget(btn2)
         btn2.bind(on_press = self.popup_dismiss)
         
         self.popup = Popup(title = 'ROLLER SUPPORT (m)', content = layout, size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
         self.popup.open() 
         
    def popup_pin(self, instance):
         
         layout = GridLayout(cols = 2)
         
         layout.add_widget(Label(text = 'X (m) = '))
         
         self.pin_text = TextInput(multiline = False)
         layout.add_widget(self.pin_text)
         
         btn = Button(text = 'SAVE')
         layout.add_widget(btn)
         btn.bind(on_press = self.add_pin)
         
         btn2 = Button(text = 'CLOSE')
         layout.add_widget(btn2)
         btn2.bind(on_press = self.popup_dismiss)
         
         self.popup = Popup(title = 'PIN SUPPORT ', content = layout, size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
         self.popup.open() 
         
    def popup_vertical(self, instance):
         
         layout = BoxLayout(orientation = 'vertical')
        
         layout1 = GridLayout(cols = 2)
         
         layout1.add_widget(Label(text = 'X(m) = '))
         
         self.vertical_load_pos_text = TextInput(multiline = False)
         layout1.add_widget(self.vertical_load_pos_text)
         
         layout1.add_widget(Label(text = 'LOAD(kN) = '))
         
         self.vertical_load_mag_text = TextInput(multiline = False)
         layout1.add_widget(self.vertical_load_mag_text)
         
         layout.add_widget(layout1)
         
         self.load_dir = Toggle_btn()
         layout.add_widget(self.load_dir)
         
         layout2 = GridLayout(cols = 2)
         
         btn = Button(text = 'SAVE')
         layout2.add_widget(btn)         
         btn.bind(on_press = self.add_vertical_load)
         
         btn2 = Button(text = 'CLOSE')
         layout2.add_widget(btn2)         
         btn2.bind(on_press = self.popup_dismiss)
         
         layout.add_widget(layout2)
         
         self.popup = Popup(title = 'POINT LOAD ', content = layout, size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
         
         self.popup.open() 
         
    def popup_moment(self, instance):
         layout = BoxLayout(orientation = 'vertical')
         
         layout1 = GridLayout(cols = 2)
         
         layout1.add_widget(Label(text = 'X(m) = '))
         
         self.moment_pos_text = TextInput(multiline = False)
         layout1.add_widget(self.moment_pos_text)
         
         layout1.add_widget(Label(text = 'MOMENT (kN * m)= '))
         
         self.moment_mag_text = TextInput(multiline = False)
         layout1.add_widget(self.moment_mag_text)
         
         layout.add_widget(layout1)
         
         self.moment_dir = Toggle_btn_moment()
         layout.add_widget(self.moment_dir)
         
         layout2 = GridLayout(cols = 2)
         
         btn = Button(text = 'SAVE')
         layout2.add_widget(btn)
         btn.bind(on_press = self.add_moment)
         
         btn2 = Button(text = 'CLOSE')
         layout2.add_widget(btn2)
         btn2.bind(on_press = self.popup_dismiss)
         
         layout.add_widget(layout2)
         
         self.popup = Popup(title = 'MOMENT MAG. ', content = layout, size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
         self.popup.open() 
         
    def popup_linear(self, instance):
         layout = BoxLayout(orientation = 'vertical')
        
         layout1 = GridLayout(cols = 2)
         
         layout1.add_widget(Label(text = 'X1 (m) = '))
         
         self.starting_pos_text = TextInput(multiline = False)
         layout1.add_widget(self.starting_pos_text)
         
         layout1.add_widget(Label(text = 'X2 (m) = '))
         
         self.ending_pos_text = TextInput(multiline = False)
         layout1.add_widget(self.ending_pos_text)
         
         layout1.add_widget(Label(text = 'LOAD(kN) = '))
         
         self.load_per_m_text = TextInput(multiline = False)
         layout1.add_widget(self.load_per_m_text)
         
         layout.add_widget(layout1)
         
         self.load_dir_linear = Toggle_btn()
         layout.add_widget(self.load_dir_linear)
         
         layout2 = GridLayout(cols = 2)
         
         btn = Button(text = 'SAVE')
         layout2.add_widget(btn)         
         btn.bind(on_press = self.add_linear_load)
         
         btn2 = Button(text = 'CLOSE')
         layout2.add_widget(btn2)         
         btn2.bind(on_press = self.popup_dismiss)
         
         layout.add_widget(layout2)
         
         self.popup = Popup(title = 'DISTRIBUTED LINEAR LOAD ', content = layout, size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
         
         self.popup.open() 
         
         
    def popup_shear(self, instance):
        pass
    
    def popup_bending(self, instance):
        pass
    
    def popup_slope(self, instance):
        pass
    
    def popup_deflection(self, instance):
        pass
    
    def popup_plotall(self, instance):
        pass
        
    
    def popup_reaction(self, instance):
        self.BEAM.solve_for_reaction_loads(*self.reaction_vars)
        graph = self.BEAM.plot_slope
        
        #print(self.BEAM.applied_loads)
        print(self.BEAM.reaction_loads)
        pass
    
    def popup_cflexure(self, instance):
        
        pass
    
    def popup_newbeam(self, instance):
        del self.BEAM
        self.E = "210E9"
        self.I = "1.71E-6"
        self.Len = '10'
        self.reaction_vars = []
        self.BEAM = Beam(self.Len, self.E, self.I)
        layout = BoxLayout(orientation = 'vertical')
        layout.add_widget(Label(text = "ANALYSE A NEW BEAM NOW!!!"))
        btn = Button(text = 'CLOSE')
        layout.add_widget(btn)
        btn.bind(on_press = self.popup_in_popup_dismiss)
        self.popup_in_popup = Popup(title = "!!NEW!!",content = layout , size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
        self.popup_in_popup.open()
        
    
    """def len_of_beam(self, instance):
        
        self.BEAM = Beam(self.len_text.text, self.E, self.I)
        self.popup.dismiss()
        
        print(type(self.len_text.text))
        print(self.E)
        print(self.I)
    """
    
    def set_E_I_Len(self, instance):
        
        #print(self.E_text.text, "\n", self.I_text.text, "\n",self.len_text.text)
        self.E = self.E_text.text
        self.I = self.I_text.text
        self.Len = self.len_text.text
        
        self.BEAM = Beam(self.Len, self.E, self.I)
        
        self.popup.dismiss()
    
    def add_fix(self, instance):
        if self.fix_text.text:
            
            self.reaction_vars.append(symbols('R_{}'.format(self.fix_text.text)))
            self.reaction_vars.append(symbols('M_{}'.format(self.fix_text.text)))
            self.BEAM.apply_support(self.fix_text.text, 'fixed')
            self.BEAM.bc_deflection.append((self.fix_text.text, 0))
            self.BEAM.bc_slope.append((self.fix_text.text, 0))
            self.popup.dismiss()
        else:
            layout = BoxLayout(orientation = 'vertical')
            layout.add_widget(Label(text = "YOU HAVEN'T ENTERED POSITION"))
            btn = Button(text = 'CLOSE')
            layout.add_widget(btn)
            btn.bind(on_press = self.popup_in_popup_dismiss)
            self.popup_in_popup = Popup(title = "NOTHING TO SAVE",content = layout , size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
            self.popup_in_popup.open()
    
    def add_roller(self, instance):
        
        if self.roller_text.text:
            
            self.reaction_vars.append(symbols('R_{}'.format(self.roller_text.text)))
            self.BEAM.apply_support(self.roller_text.text, 'roller')
            self.BEAM.bc_deflection.append((self.roller_text.text, 0))
            self.popup.dismiss()
        else:
            layout = BoxLayout(orientation = 'vertical')
            layout.add_widget(Label(text = "YOU HAVEN'T ENTERED POSITION"))
            btn = Button(text = 'CLOSE')
            layout.add_widget(btn)
            btn.bind(on_press = self.popup_in_popup_dismiss)
            self.popup_in_popup = Popup(title = "NOTHING TO SAVE",content = layout , size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
            self.popup_in_popup.open()
    
    
    def add_pin(self, instance):
        
        if self.pin_text.text:
            
            self.reaction_vars.append(symbols('R_{}'.format(self.pin_text.text)))
            self.BEAM.apply_support(self.pin_text.text, 'pin')
            self.BEAM.bc_deflection.append((self.pin_text.text, 0))
            self.popup.dismiss()
        else:
            layout = BoxLayout(orientation = 'vertical')
            layout.add_widget(Label(text = "YOU HAVEN'T ENTERED POSITION"))
            btn = Button(text = 'CLOSE')
            layout.add_widget(btn)
            btn.bind(on_press = self.popup_in_popup_dismiss)
            self.popup_in_popup = Popup(title = "NOTHING TO SAVE",content = layout , size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
            self.popup_in_popup.open()
    
    
    def add_vertical_load(self, instance):
        if self.vertical_load_mag_text.text != '' and self.vertical_load_pos_text.text != '':
            states = self.load_dir.get_state()
            print(states)
            if (states[0] == 'normal' and states[1] == 'down') or (states[0] == 'down' and states[1] == 'normal'):
                
                if states[0] == 'normal' and states[1] == 'down':
            
                    self.BEAM.apply_load(self.vertical_load_mag_text.text, self.vertical_load_pos_text.text, -1)
                    self.popup.dismiss()
                else:
                    self.BEAM.apply_load('-' + self.vertical_load_mag_text.text, self.vertical_load_pos_text.text, -1)
                    self.popup.dismiss()
                
                
            else:
                layout = BoxLayout(orientation = 'vertical')
                layout.add_widget(Label(text = "YOU MUST CHOOSE ONE DIRECTION"))
                btn = Button(text = 'CLOSE')
                layout.add_widget(btn)
                btn.bind(on_press = self.popup_in_popup_dismiss)
                self.popup_in_popup = Popup(title = "IN WHICH DIR. DO I APPLY LOAD ?",content = layout , size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
                self.popup_in_popup.open()
                
            
        else:
            layout = BoxLayout(orientation = 'vertical')
            layout.add_widget(Label(text = "ENTER BOTH LOAD MAG. AND POS."))
            btn = Button(text = 'CLOSE')
            layout.add_widget(btn)
            btn.bind(on_press = self.popup_in_popup_dismiss)
            self.popup_in_popup = Popup(title = "INSUFFICIENT INFO !",content = layout , size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
            self.popup_in_popup.open()
        
    def add_moment(self, instance):
        
        if self.moment_pos_text.text != '' and self.moment_mag_text.text != '':
            states = self.moment_dir.get_state()
            print(states)
            if (states[0] == 'normal' and states[1] == 'down') or (states[0] == 'down' and states[1] == 'normal'):
                
                if states[0] == 'normal' and states[1] == 'down':
            
                    self.BEAM.apply_load(self.moment_mag_text.text, self.moment_pos_text.text, -2)
                    self.popup.dismiss()
                else:
                    self.BEAM.apply_load('-' + self.moment_mag_text.text, self.moment_pos_text.text, -2)
                    self.popup.dismiss()
                
                
            else:
                layout = BoxLayout(orientation = 'vertical')
                layout.add_widget(Label(text = "YOU MUST CHOOSE ONE DIRECTION"))
                btn = Button(text = 'CLOSE')
                layout.add_widget(btn)
                btn.bind(on_press = self.popup_in_popup_dismiss)
                self.popup_in_popup = Popup(title = "IN WHICH DIR. DO I APPLY MOMENT ?",content = layout , size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
                self.popup_in_popup.open()
                
            
        else:
            layout = BoxLayout(orientation = 'vertical')
            layout.add_widget(Label(text = "ENTER BOTH MOMENT MAG. AND POS."))
            btn = Button(text = 'CLOSE')
            layout.add_widget(btn)
            btn.bind(on_press = self.popup_in_popup_dismiss)
            self.popup_in_popup = Popup(title = "INSUFFICIENT INFO !",content = layout , size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
            self.popup_in_popup.open()
        
        
    def add_linear_load(self, instance):
        
        if self.starting_pos_text.text != '' and self.ending_pos_text.text != '' and self.load_per_m_text.text != '':
            states = self.load_dir_linear.get_state()
            print(states)
            if (states[0] == 'normal' and states[1] == 'down') or (states[0] == 'down' and states[1] == 'normal'):
                
                if states[0] == 'normal' and states[1] == 'down':
            
                    self.BEAM.apply_load(self.load_per_m_text.text, self.starting_pos_text.text, 0, self.ending_pos_text.text)
                    self.popup.dismiss()
                else:
                    self.BEAM.apply_load('-' + self.load_per_m_text.text, self.starting_pos_text.text, 0, int(self.ending_pos_text.text))
                    self.popup.dismiss()
                
                
            else:
                layout = BoxLayout(orientation = 'vertical')
                layout.add_widget(Label(text = "YOU MUST CHOOSE ONE DIRECTION"))
                btn = Button(text = 'CLOSE')
                layout.add_widget(btn)
                btn.bind(on_press = self.popup_in_popup_dismiss)
                self.popup_in_popup = Popup(title = "IN WHICH DIR. DO I APPLY THE LOAD ?",content = layout , size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
                self.popup_in_popup.open()
                
            
        else:
            layout = BoxLayout(orientation = 'vertical')
            layout.add_widget(Label(text = "ENTER ALL START, END AND LOAD"))
            btn = Button(text = 'CLOSE')
            layout.add_widget(btn)
            btn.bind(on_press = self.popup_in_popup_dismiss)
            self.popup_in_popup = Popup(title = "INSUFFICIENT INFO !",content = layout , size_hint = (.4, .4), pos_hint = {'center_x' : .5, 'center_y' : .5})
            self.popup_in_popup.open()
        
    def popup_dismiss(self, instance):
        self.popup.dismiss()
    
    
    def popup_in_popup_dismiss(self, instance):
        self.popup_in_popup.dismiss()
    
class BApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        root = Panel()
        return root
        
        
if __name__ == "__main__":
    
    beam = BApp()
    beam.run()