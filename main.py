from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics import Color, RoundedRectangle

Window.size = (360, 640)

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

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        welcome_label = Label(
            text="WELCOME CAFE", 
            font_size=45, 
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(300, 80),
            pos_hint={'center_x': 0.5},
            font_name='Lalezar-Regular.ttf'
        )

        with welcome_label.canvas.before:
            Color(0.6, 0.4, 0.2, 1)
            self.rect = RoundedRectangle(
                pos=welcome_label.pos, 
                size=welcome_label.size, 
                radius=[20,]
            )
        
        welcome_label.bind(pos=self.update_rect, size=self.update_rect)
        
        layout.add_widget(welcome_label)

        with self.canvas.before:
            self.bg_image = Rectangle(source='bg.png', pos=self.pos, size=self.size)
        
        self.bind(size=self._update_bg, pos=self._update_bg)

        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

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
            height=50,
                background_color=(1, 0.7, 0, 1)
        )

        btn.bind(on_press=self.go_menu)
        layout.add_widget(btn)

        self.add_widget(layout)

    def go_menu(self, instance):
        self.manager.current = 'menu'

    def _update_bg(self, *args):
        self.bg_image.pos = self.pos
        self.bg_image.size = self.size

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size



class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.92, 0.84, 0.72, 1)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self._update_bg, size=self._update_bg)

        self.total = 0
        self.cart_items = []
        
        # 1. Main Layout (แนวตั้ง)
        self.layout = BoxLayout(orientation='vertical')
        
        # 2. Header (ส่วนหัวแสดงปุ่ม Logout)
        header = BoxLayout(size_hint_y=0.1, padding=5)
        header.add_widget(Label(text="Select Drink", font_size=20, bold=True))
        btn_logout = Button(text="Logout", size_hint_x=0.3, background_color=(0.8, 0, 0, 1))
        btn_logout.bind(on_press=self.do_logout)
        header.add_widget(btn_logout)
        self.layout.add_widget(header)
        
        # 3. ScrollView & Grid
        scroll = ScrollView(size_hint_y=0.6)
        grid = GridLayout(cols=2, spacing=10, padding=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        for item in DRINK_MENU:
            # สร้างการ์ดสำหรับเมนูแต่ละอัน
            card = BoxLayout(orientation='vertical', size_hint_y=None, height=120)
            
            # ชื่อและราคา
            lbl = Label(text=f"{item['name']}\n{item['price']} THB")
            card.add_widget(lbl)
            
            # ปุ่มกดสั่ง (สีเขียว)
            btn_add = Button(text="ADD +", background_color=(0, 0.6, 0, 1))
            # ผูกฟังก์ชัน (ใช้ lambda เพื่อส่งราคาและชื่อเข้าไป)
            btn_add.bind(on_press=lambda x, p=item['price'], n=item['name']: self.add_item(p, n))
            card.add_widget(btn_add)
            
            grid.add_widget(card)

        scroll.add_widget(grid)
        self.layout.add_widget(scroll)

        # 4. Footer (ส่วนแสดงยอดเงินและปุ่ม Pay)
        footer = BoxLayout(orientation='vertical', size_hint_y=0.3, padding=10)
        
        self.lbl_total = Label(text="Total: 0 THB", font_size=24, color=(1, 1, 0, 1))
        footer.add_widget(self.lbl_total)
        
        btns = BoxLayout(spacing=10)
        # ปุ่ม Clear
        btn_clear = Button(text="Clear", background_color=(0.5, 0.5, 0.5, 1))
        btn_clear.bind(on_press=self.clear_order)
        btns.add_widget(btn_clear)
        
        # ปุ่ม Pay
        btn_pay = Button(text="PAY", background_color=(0, 0.4, 0.8, 1))
        btn_pay.bind(on_press=self.go_pay)
        btns.add_widget(btn_pay)
        
        footer.add_widget(btns)
        self.layout.add_widget(footer)
        
        self.add_widget(self.layout)

    def do_logout(self, instance):
        self.manager.current = 'login'

    def add_item(self, price, name):
        self.total += price
        self.cart_items.append(name)
        self.lbl_total.text = f"Total: {self.total} THB"

    def clear_order(self, instance):
        self.total = 0
        self.cart_items = []
        self.lbl_total.text = "Total: 0 THB"

    def go_pay(self, instance):
        # ส่งข้อมูลไปหน้าใบเสร็จ
        self.manager.get_screen('receipt').update_info(self.total, len(self.cart_items))
        # เคลียร์ค่าหน้าเมนูรอไว้เลย
        self.clear_order(None) 
        # เปลี่ยนหน้า
        self.manager.current = 'receipt'

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

class ReceiptScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.96, 0.94, 0.85, 1)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self._update_bg, size=self._update_bg)

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

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
 
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
