foods = {}
total_cal = 0

for i in range(3):
    # รับชื่ออาหาร (ห้ามว่าง)
    while True:
        food = input(f"อาหารรายการที่ {i+1}: ").strip()
        if food != "":
            break
        print(" ห้ามใส่ค่าว่าง")

    # รับแคลอรี่ (ต้องเป็นตัวเลขเท่านั้น)
    while True:
        try:
            cal = input("แคลอรี่: ").strip()
            if cal == "":
                print(" ห้ามใส่ค่าว่าง")
                continue

            cal = int(cal)  # แปลงเป็นตัวเลข
            break
        except ValueError:
            print(" แคลอรี่ต้องเป็นตัวเลขเท่านั้น")

    foods[food] = cal
    total_cal += cal

print("แคลอรี่รวมทั้งวัน =", total_cal)