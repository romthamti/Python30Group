# ตรวจสอบความดันโลหิต

sys = int(input("Systolic: "))    # ค่าตัวบน
dia = int(input("Diastolic: "))   # ค่าตัวล่าง

if sys > 140 or dia > 90:
    print("ความดันสูง")
else:
    print("ปกติ")