# รับอายุจากผู้ใช้
age = int(input("กรุณาใส่อายุ: "))

# คำนวณอัตราการเต้นหัวใจสูงสุด
max_heart_rate = 220 - age

# คำนวณโซนออกกำลังกาย 60% - 80%
min_zone = max_heart_rate * 0.60
max_zone = max_heart_rate * 0.80

# แสดงผลลัพธ์
print("Max Heart Rate =", max_heart_rate)
print("โซนออกกำลังกายที่เหมาะสม:")
print(f"➡ {min_zone:.0f} - {max_zone:.0f} ครั้งต่อนาที")