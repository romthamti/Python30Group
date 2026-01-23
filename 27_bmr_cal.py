# โปรแกรมคำนวณค่า BMR

gender = input("กรุณาใส่เพศ (ชาย/หญิง): ")
weight = float(input("กรุณาใส่น้ำหนัก (กิโลกรัม): "))
height = float(input("กรุณาใส่ส่วนสูง (เซนติเมตร): "))
age = int(input("กรุณาใส่อายุ (ปี): "))

if gender == "ชาย":
    bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
elif gender == "หญิง":
    bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
else:
    print("กรุณาใส่เพศให้ถูกต้อง")
    exit()

print(f"ค่า BMR ของคุณคือ: {bmr:.2f} กิโลแคลอรี/วัน")