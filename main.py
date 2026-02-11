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
            height=50,
                background_color=(1, 0.7, 0, 1)  # สีส้ม
        )

        btn.bind(on_press=self.go_menu)  # ← callback
        layout.add_widget(btn)

        self.add_widget(layout)

    def go_menu(self, instance):
        self.manager.current = 'menu'

# --- พื้นที่งาน นาย A (Menu Screen & Logic) ---
# --- พื้นที่งาน นาย A (Menu Screen & Logic) ---
# แก้ไขโดย นาย A: เพิ่ม Loop สร้างปุ่มและระบบคิดเงิน
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
        
        # 3. ScrollView & Grid (ส่วนเมนูที่เลื่อนได้)
        # นี่คือหัวใจสำคัญ! วนลูปสร้างปุ่มจากข้อมูลของนาย B
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
        
        # ปุ่ม Pay (สีน้ำเงิน)
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
