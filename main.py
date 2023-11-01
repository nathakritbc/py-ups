import nut2

# กำหนดข้อมูลเชื่อมต่อไปยัง NUT
hostname = 'localhost'
port = 3493
username = 'admin'
password = 'admin@123'
ups_name = 'myups'  # ชื่อของเครื่อง UPS ของคุณ

# เชื่อมต่อกับ NUT
connection = nut2.PyNUT(hostname, port)
connection.login(username, password)

# ดึงข้อมูลจากเครื่อง UPS
data = connection.GetUPSVars(ups_name)
print(data)

# ยกเลิกการเชื่อมต่อ
connection.logout()
