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
DRINK_MENU = [
    {"name": "Espresso", "price": 40},
    {"name": "Americano", "price": 45},
    {"name": "Latte", "price": 50},
    {"name": "Cappuccino", "price": 50},
    {"name": "Mocha", "price": 55},
    {"name": "Cocoa", "price": 45},
    {"name": "Green Tea", "price": 50},
    {"name": "Thai Tea", "price": 45},

    {"name": "Caramel Latte", "price": 60},
    {"name": "Vanilla Latte", "price": 60},
    {"name": "Matcha Latte", "price": 65},
    {"name": "Honey Lemon", "price": 45},
    {"name": "Strawberry Soda", "price": 40},
    {"name": "Blueberry Smoothie", "price": 70},
]
# --- พื้นที่งาน นาย B (Login Screen) ---
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        layout.add_widget(Label(text="WELCOME CAFE", font_size=30))

        self.input_user = TextInput(
            hint_text="Username",
            size_hint_y=None,
            height=40
        )
        layout.add_widget(self.input_user)

        btn = Button(
            text="ENTER",
            size_hint_y=None,
            height=50
        )

        btn.bind(on_press=self.go_menu)  # ← callback
        layout.add_widget(btn)

        self.add_widget(layout)

    def go_menu(self, instance):
        self.manager.current = 'menu'

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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        layout.add_widget(Label(text="THANK YOU!", font_size=35))

        self.lbl_info = Label(text="Payment Success", font_size=20)
        layout.add_widget(self.lbl_info)

        btn_back = Button(
            text="Back to Menu",
            size_hint_y=None,
            height=50
        )

        btn_back.bind(on_press=self.go_back)  # callback
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def update_info(self, total, count):
        self.lbl_info.text = f"Items: {count}\nTotal Paid: {total} THB"

    def go_back(self, instance):
        self.manager.current = 'menu'
 
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
