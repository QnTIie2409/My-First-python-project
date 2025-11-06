import json
import  datetime


FILE_NAME = "calory.json"

def load_data():
    try:
        with open (FILE_NAME,"r",encoding="utf-8") as f:
            all_data = json.load(f)
            return all_data
    except FileNotFoundError:
        return []
    
def save_data(data):
    with open(FILE_NAME , "w", encoding="utf-8") as f:
        json.dump(data, f , indent= 4 , ensure_ascii= False)

def log_data(ten_mon_an,luong_calo):
    now = datetime.datetime.now()
    time_picked = now.strftime("%d/%m/%Y %H:%M:%S")

    meal = {
        "món ăn: ":ten_mon_an,
        "lượng calo trong món: ":luong_calo,
        "Thời gian ăn: ":time_picked
    }
    all_data = load_data()
    all_data.append(meal)
    save_data(all_data)
    print(f"Tên món ăn: {meal['món ăn: ']} - Lượng calo: {meal['lượng calo trong món: ']}")

def view_all_data():
    all_data = load_data()
    all_calories = 0

    if not all_data:
        print(f"Bạn chưa ăn gì cả!!!")
    else:
        for meal in all_data:
            print(f"Các món bạn đã ăn là: {meal['món ăn: ']} - Lượng calo của món đó: {meal['lượng calo trong món: ']}")
            all_calories += int(meal['lượng calo trong món: '])
        print(f"lượng calo bạn đã ăn từ trước đó tới giờ: {all_calories}")
def view_today_data():
    today = datetime.datetime.today().strftime("%d/%m/%Y")
    today_calo = 0
    all_data = load_data()
    found_any = False 

    print(f"--- CÁC BỮA ĂN HÔM NAY ({today}) ---") 
    for meal in all_data:
        if today in meal['Thời gian ăn: ']:
            
            found_any = True 
            print(f"  Món: {meal['món ăn: ']} - Calo: {meal['lượng calo trong món: ']}")
            
            today_calo += int(meal['lượng calo trong món: '])

    if found_any:
        print("---------------------------------")
        print(f"TỔNG HÔM NAY: {today_calo} kcal")
    else:
        print("Hôm nay bạn chưa ăn gì cả.")