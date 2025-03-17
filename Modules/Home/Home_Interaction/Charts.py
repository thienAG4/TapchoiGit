from Demos.win32ts_logoff_disconnected import username
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QVBoxLayout
import matplotlib.pyplot as plt
import numpy as np
import json
from datetime import datetime, timedelta

class Charts:
    def __init__(self, expense=None,incomme=None): #expense="./data/expenses"
        self.expense = expense #khi sử dụng class thì 2 cái này phải để địa chỉ file json
        self.incomme = incomme
    def PieChart(self, layout: QVBoxLayout):
        with open(self.expense,encoding="UTF-8") as f:
           inlist= json.load(f)
        labels_and_sizes=[]
        total_expenses=0
        # Gộp các mục cùng category
        temp = {}
        for i in inlist:
            category = i["category"]
            amount = float(i["amount"])  # Đảm bảo amount là số thực
            total_expenses += amount
            temp[category] = temp.get(category, 0) + amount  # Cộng dồn giá trị

        # Chuyển kết quả thành danh sách dict
        Piechart_data = [{key: value} for key, value in temp.items()]
        print(Piechart_data)
        labels = []
        for d in Piechart_data:
            labels.append(*d.keys())
        print(labels)
        sizes = []
        sizes = [list(d.values())[0] / total_expenses for d in Piechart_data]
        # Tạo Figure và Axes để vẽ biểu đồ tròn
        fig, ax = plt.subplots(figsize=(5, 4))
        # Màu sắc cho mỗi lát bánh (tham khảo Bootstrap 5 colors)
        colors = ["#20c997", "#ffc107", "#fd7e14", "#0d6efd", "#6f42c1"]
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        # Đảm bảo biểu đồ là hình tròn (thay vì hình elip)
        ax.axis("equal")
        # Chuyển Figure thành widget Canvas
        canvas = FigureCanvas(fig)
        # Thêm Canvas vào layout đã truyền vào
        layout.addWidget(canvas)
        print()

    def ColumnChart(self,layout: QVBoxLayout):
        with open(self.expense,encoding="UTF-8") as f:
            expenses_data=json.load(f)
        with open(self.incomme, encoding="UTF-8") as f:
            incomes_data = json.load(f)
        # Xác định khoảng thời gian 7 ngày gần nhất
        today = datetime.today()
        last_7_days = [(today - timedelta(days=i)).strftime("%d/%m/%Y") for i in range(7)][::-1]
        
        with open(self.incomme, encoding="UTF-8") as f:
        username=self

        # Trả về dạng {Ngày:Số tiền hôm đs}
        expenses = {str(date): 0 for date in last_7_days}
        incomes = {str(date): 0 for date in last_7_days}
        #Tìm ra số tiền chi theo ngày
        for i in expenses_data:
            date=i["date"] #định dạng str
            amount=abs(float(i["amount"]))
            expenses[username][date] += amount
        expenses_list=list(expenses.values())
        print(expenses_list)
        # Tìm ra số tiền thu theo ngày
        for i in incomes_data:
            date = i["date"]  # định dạng str
            amount = abs(float(i["amount"]))
            incomes[username][date] += amount
        incomes_list = list(incomes.values())
        print(incomes_list)

        # Danh sách chứa tên thứ
        weekdays = []

        # Ngày hiện tại
        today = datetime.today()

        # Lấy thứ từ hôm nay lùi dần về 7 ngày trước
        for i in range(7):
            day = today - timedelta(days=i)  # Lùi ngày
            weekdays.append(day.strftime("%A"))  # Lấy tên thứ
        weekdays=weekdays[::-1]

        #Vẽ Columnchart
        n_groups = len(weekdays)  # = 7
        index = np.arange(n_groups)  # [0,1,2,3,4,5,6]
        bar_width = 0.3  # Độ rộng mỗi cột

        # 3) Tạo Figure, Axes
        plt.close('all')  # Đóng mọi figure cũ, tránh vẽ chồng
        fig, ax = plt.subplots(figsize=(6, 4))

        # 4) Vẽ cột Expense (x = index) và Income (x = index + bar_width)
        ax.bar(index, expenses_list, bar_width, color='blue', label='Expense')
        ax.bar(index + bar_width, incomes_list, bar_width, color='orange', label='Income')

        # 5) Cài đặt trục X
        ax.set_xticks(index + bar_width / 2)  # Đặt nhãn ngày ở giữa 2 cột
        ax.set_xticklabels(weekdays)
        ax.set_ylabel('Amount')
        mix_list=incomes_list+expenses_list
        ax.set_ylim(0, max(tuple(mix_list))+50 )
        ax.legend()
        canvas = FigureCanvas(fig)
        ax.set_xlabel('Day')
        ax.set_title('Expense vs Income')
        ax.legend()

        # Chuyển Figure thành widget Canvas
        plt.tight_layout()
        canvas = FigureCanvas(fig)
        # Thêm Canvas vào layout đã truyền vào

        layout.addWidget(canvas)




