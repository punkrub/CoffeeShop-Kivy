from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# ตั้งขนาดจอเหมือนมือถือ
Window.size = (360, 640)

# --- พื้นที่งาน นาย B (Menu Data) ---
DRINK_MENU = [] 

# --- พื้นที่งาน นาย B (Login Screen) ---
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ใส่ข้อความจะได้รู้ว่าหน้านี้คือ Login
        self.add_widget(Label(text="Login Screen\n(Waiting for Mr. B)", font_size=30)) 

# --- พื้นที่งาน นาย A (Menu Screen & Logic) ---
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = 0
        self.cart_items = []
        
        # Layout หลัก
        self.layout = BoxLayout(orientation='vertical')
        
        # ส่วนแสดงผล (นาย A เขียน Logic ไว้ก่อน)
        self.lbl_total = Label(text="Total: 0 THB", size_hint_y=0.1)
        self.layout.add_widget(self.lbl_total)
        
        self.add_widget(self.layout)

    def add_item(self, price, name):
        # นาย A: เขียน Logic คำนวณเงิน
        self.total += price
        self.cart_items.append(name)
        self.lbl_total.text = f"Total: {self.total} THB"

# --- พื้นที่งาน นาย C (Receipt Screen) ---
class ReceiptScreen(Screen):
    pass 

# --- Main App ---
class CoffeeShopApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login')) 
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ReceiptScreen(name='receipt'))
        return sm

if __name__ == '__main__':
    CoffeeShopApp().run()