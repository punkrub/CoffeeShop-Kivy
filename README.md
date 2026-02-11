# CoffeeShop-Kivy
Project for 241-152 - Coffee Shop Application

โปรแกรมจำลองระบบร้านกาแฟ พัฒนาด้วยภาษา Python และ Kivy Framework ออกแบบมาให้ใช้งานง่าย รองรับการสั่งเครื่องดื่ม คำนวณเงิน และออกใบเสร็จ

สมาชิกกลุ่ม (Group Members)
1. 6810110638 นายปัณณ์ สุวรรณแสง

Responsibilities
- ออกแบบโครงสร้างหลักของโปรแกรม
- เขียนโค้ดส่วนการทำงานหลัก
- จัดการระบบเปลี่ยนหน้าจอ
- แก้ไขบั๊กและการทำงานของฟังก์ชันต่างๆ

2. 6810110109 ดาราชัย เดชะพันธุ์ 

Responsibilities
- ออกแบบหน้าจอและการจัดวาง
- ตกแต่งความสวยงาม เลือกโทนสี
- สร้างและจัดเตรียม Mock Data สำหรับเมนูเครื่องดื่ม
- จัดการ Version Control และตรวจสอบความเรียบร้อยก่อนส่ง


การติดตั้งและรันโปรแกรม (Installation & Run)
1. Clone Project
   ```bash
   git clone [https://github.com/punkrub/CoffeeShop-Kivy.git](https://github.com/punkrub/CoffeeShop-Kivy.git)

2. ติดตั้ง Library ที่จำเป็น:
pip install kivy

3. รันโปรแกรม:
python main.py


ฟีเจอร์หลัก (Key Features)
ตามข้อกำหนดของโจทย์ (Requirements):

GUI Elements: ใช้งาน Widgets มากกว่า 30 ชิ้น (ประกอบด้วย Labels, Buttons, TextInputs, Layouts, ScrollView)

Interactivity: มี Callbacks Function มากกว่า 10 จุด สำหรับโต้ตอบกับผู้ใช้

Data Management: มีการส่งผ่านข้อมูลระหว่างหน้าจอ (Screen Manager)

Calculation: ระบบคำนวณราคาสินค้าและรวมยอดเงินแบบ Real-time


อธิบายโครงสร้างโค้ด (Code Explanation)
โปรแกรมแบ่งการทำงานออกเป็น 3 หน้าจอหลัก (Screens):

1. LoginScreen (หน้าเข้าสู่ระบบ)
-รับค่า Username ผ่าน TextInput
-มีปุ่ม Button เพื่อตรวจสอบและเปลี่ยนหน้าไปยังเมนู

2. MenuScreen (หน้าเลือกเมนู)
-Dynamic UI: ใช้ Loop วนสร้างปุ่มเมนูเครื่องดื่มจาก List ข้อมูล (Dictionary)
-ScrollView: รองรับรายการเครื่องดื่มจำนวนมาก เลื่อนขึ้น-ลงได้
-Logic:
   ฟังก์ชัน add_item(): คำนวณราคาสะสมและเก็บชื่อเมนูลงตะกร้า
   ฟังก์ชัน clear_order(): ล้างข้อมูลรายการทั้งหมด
   ฟังก์ชัน go_pay(): ส่งยอดรวมไปยังหน้าใบเสร็จ

3. ReceiptScreen (หน้าใบเสร็จ)
รับข้อมูลยอดเงินและจำนวนแก้วมาจากหน้า MenuScreen

แสดงข้อความขอบคุณและยอดเงินที่ต้องชำระ

ปุ่ม Back เพื่อกลับไปเริ่มรายการใหม่ (Reset ค่า)

