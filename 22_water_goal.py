# รับค่าน้ำหนักตัว
weight = float(input("น้ำหนักตัว (กิโลกรัม): "))

# คำนวณปริมาณน้ำที่ควรดื่ม (มล.)
water_ml = weight * 33

# แปลงจากมิลลิลิตรเป็นลิตร
water_liter = water_ml / 1000

# แสดงผล
print("ควรดื่มน้ำประมาณ {:.0f} มล. หรือ {:.2f} ลิตร/วัน".format(
    water_ml, water_liter
))