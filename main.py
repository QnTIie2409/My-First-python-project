import calories_manager

print("--- CHƯƠNG TRÌNH THEO DÕI CALORIE ---")
print("1. Thêm bữa ăn")
print("2. Xem tất cả bữa ăn đã lưu")
print("3. Xem lượng calo đã ăn trong ngày hôm nay")
print("4. Thoát")

while True:
    choice = input("vui lòng lựa chọn 1/2/3/4:")
    if choice == '1':

        a = input("vui lòng nhập món bạn đã ăn: ")
        b = input("vui lòng nhập lượng calo của món ăn đó: ")
        try:
            b_int = int(b)
            calories_manager.log_data(a,b_int)
        except ValueError:
            print(f"vui lòng nhập calo là một con số!!")
    elif choice == '2':
        calories_manager.view_all_data()
    elif choice == '3':
        calories_manager.view_today_data()
    elif choice == '4':
        print("Bạn đã lựa chọn thoát. Dừng ngay lập tức!!")
        break
    else:
        print("Vui lòng nhập đúng giá trị 1/2/3/4!!!")