import json
import tkinter as tk
from tkinter import scrolledtext
import re
from datetime import datetime

# File JSON để lưu dữ liệu
DATA_FILE = "data/database.json"

# Đọc dữ liệu từ file JSON
def read_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Ghi dữ liệu vào file JSON
def write_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Thêm giao dịch vào file JSON
def add_transaction(categories, details, amount):
    data = read_data()
    transaction = {
        "Categories": categories,
        "Details": details,
        "Amount": int(amount),
        "Date": datetime.now().strftime("%Y-%m-%d")
    }
    data.append(transaction)
    write_data(data)

# Danh sách tất cả giao dịch
def get_transactions():
    return read_data()

# Tính tổng số tiền đã chi tiêu
def get_total_expense():
    transactions = get_transactions()
    return sum([int(t["Amount"]) for t in transactions if isinstance(t["Amount"], (int, float, str)) and str(t["Amount"]).isdigit()])

# Xử lý câu lệnh nhập vào từ người dùng
def parse_input(user_input):
    user_input = user_input.lower()

    # Nhận dạng câu nhập vào dạng: "Mình đã chi 200k cho ăn uống"
    match = re.search(r'chi (\d+)k cho (.+)', user_input)
    if match:
        amount = int(match.group(1)) * 1000
        categories = match.group(2)
        details = match.group(2)
        add_transaction(categories, details, amount)
        total = get_total_expense()
        return f"Đã ghi nhận chi tiêu {amount:,} VND cho {categories}. Tổng chi tiêu của bạn là {total:,} VND."

    if "xem giao dịch" in user_input:
        transactions = get_transactions()
        if not transactions:
            return "Bạn chưa có giao dịch nào."
        response = "Danh sách giao dịch:\n"
        for t in transactions[-5:]:  # Hiển thị 5 giao dịch gần nhất
            response += f"- {t['Categories']}: {t['Amount']:,} VND ({t['Date']})\n"
        return response

    return "Mình chưa hiểu ý bạn, vui lòng nhập lại!"

# Hàm gửi tin nhắn
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chatbox.insert(tk.END, f"Bạn: {user_input}\n", "user")
    response = parse_input(user_input)
    chatbox.insert(tk.END, f"Bot: {response}\n", "bot")

    entry.delete(0, tk.END)

# Giao diện với Tkinter
root = tk.Tk()
root.title("Chatbot Quản lý Chi tiêu")
root.geometry("400x500")

chatbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chatbox.pack(pady=10)
chatbox.tag_configure("user", background="light blue", foreground="black", font=("Times New Roman", 15, "bold"), justify="right")
chatbox.tag_configure("bot", foreground="blue", font=("Times New Roman", 15, "bold"))

frame = tk.Frame(root, bg="#F0F0F0")
frame.pack(pady=5)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(frame, text="Gửi", command=send_message)
send_button.pack(side=tk.RIGHT)

root.mainloop()
