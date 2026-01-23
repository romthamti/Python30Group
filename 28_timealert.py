# โปรแกรมแสดงเวลาเตือนทานยา

meals = int(input("กรุณาใส่จำนวนมื้อยาที่ต้องทานต่อวัน: "))

start_hour = 8
end_hour = 20

interval = (end_hour - start_hour) // meals

print("เวลาที่ควรทานยา:")
for i in range(meals):
    hour = start_hour + (interval * i)
    print(f"{hour:02d}:00 น.")
