# เก็บน้ำหนักย้อนหลัง 5 เดือน (หน่วย: กิโลกรัม)
weights = [65, 66, 65.5, 64.8, 64]

total_change = 0

# ใช้ for loop คำนวณความเปลี่ยนแปลงของน้ำหนัก
for i in range(1, len(weights)):
    change = weights[i] - weights[i - 1]
    total_change += change

# คำนวณค่าเฉลี่ยการเปลี่ยนแปลง
average_change = total_change / (len(weights) - 1)

# แสดงผล
if average_change > 0:
    print(f"น้ำหนักเพิ่มขึ้นเฉลี่ย {average_change:.2f} กก./เดือน")
elif average_change < 0:
    print(f"น้ำหนักลดลงเฉลี่ย {abs(average_change):.2f} กก./เดือน")
else:
    print("น้ำหนักคงที่")