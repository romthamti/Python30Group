import math

# รับค่าจากผู้ใช้
speed = float(input("ป้อนความเร็วในการวิ่ง (กม./ชม.): "))
time = float(input("ป้อนเวลาที่วิ่ง (นาที): "))

# สูตรคำนวณแคลอรี่ (ประมาณค่า)
calories = math.floor(speed * time * 0.1)

# แสดงผล
print(f"คุณเผาผลาญพลังงานประมาณ {calories} แคลอรี่")