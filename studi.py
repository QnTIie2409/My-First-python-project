# --- File: studi.py (hoặc main.py) ---

# 1. "Nhập khẩu" nhà bếp của bạn
import diary

print("--- CHƯƠNG TRÌNH NHẬT KÝ ---")

# 2. "Ra lệnh" cho nhà bếp tải dữ liệu
#    File này không cần biết 'try...except' hay 'json' là gì
all_my_tasks = diary.load_all_task()

# 3. Lấy thông tin từ người dùng (Phần giao diện)
new_entry = input("Bạn đang nghĩ gì?, Ghi ra: ")

# 4. "Ra lệnh" cho nhà bếp chuẩn bị món ăn (tạo dict)
new_task_object = diary.create_new_task_content(new_entry)

# 5. Quyết định của "Phòng ăn" (Thêm vào list)
all_my_tasks.append(new_task_object)

# 6. "Ra lệnh" cho nhà bếp lưu lạis
diary.writeinfile(all_my_tasks)

print(f"\nĐã lưu thành công! Tổng số mục nhật ký: {len(all_my_tasks)}")
print("--- KẾT THÚC ---")