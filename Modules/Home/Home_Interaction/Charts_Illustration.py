from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QVBoxLayout
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import json

class ChartsIllustration:
    def showPieChart(self, layout: QVBoxLayout):
        #Đọc file json
        with open("D:\\DoAnCki\\Home_Interaction\\data\\expenses.json", "r", encoding="utf-8") as f:
            expenses_list=json.load(f)
        # Tạo Figeure và Axes để vẽ biểu đồ tròn
        fig, ax = plt.subplots(figsize=(5, 4))
        labels_and_sizes = []
        total_expenses = 0
        for i in range(len(expenses_list)):
            total_expenses += float(expenses_list[i]["amount"])
            if expenses_list[i]["category"] not in labels_and_sizes:
                labels_and_sizes.append({expenses_list[i]["category"]: float(expenses_list[i]["amount"])})
                #labels_and_sizes=[{"Transport":42.3}]
            elif expenses_list[i]["category"] in labels_and_sizes:
                labels_and_sizes[expenses_list[i]["category"]] += float(expenses_list[i]["amount"])
        # {labels:sizes}={categories:(total_category_amount/total_expenses)}
        labels = []
        for d in labels_and_sizes:
            labels.append(str(*d.keys()))
        sizes = []
        for i in labels_and_sizes:
            sizes.append(i[str(*i.keys())] / total_expenses)
        # Màu sắc cho mỗi lát bánh (tham khảo Bootstrap 5 colors)
        colors = ["#20c997", "#ffc107", "#fd7e14", "#0d6efd", "#6f42c1"]
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        # Đảm bảo biểu đồ là hình tròn (thay vì hình elip)
        ax.axis("equal")
        # Chuyển Figure thành widget Canvas
        canvas = FigureCanvas(fig)
        # Thêm Canvas vào layout đã truyền vào
        layout.addWidget(canvas)

    def showColumnChart(self, layout: QVBoxLayout):
        # 1) Dữ liệu chuẩn: 7 phần tử, mỗi phần tử là 1 chuỗi ngày
        days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        expense = [400, 300, 250, 500, 350, 200, 450]
        income = [200, 150, 180, 400, 230, 150, 280]

        # Kiểm tra độ dài (phải đều là 7)
        print("days:", days, "len:", len(days))
        print("expense:", expense, "len:", len(expense))
        print("income:", income, "len:", len(income))

        # 2) Tạo index và bar_width
        n_groups = len(days)  # = 7
        index = np.arange(n_groups)  # [0,1,2,3,4,5,6]
        bar_width = 0.3  # Độ rộng mỗi cột

        # 3) Tạo Figure, Axes
        plt.close('all')  # Đóng mọi figure cũ, tránh vẽ chồng
        fig, ax = plt.subplots(figsize=(6, 4))

        # 4) Vẽ cột Expense (x = index) và Income (x = index + bar_width)
        ax.bar(index, expense, bar_width, color='blue', label='Expense')
        ax.bar(index + bar_width, income, bar_width, color='orange', label='Income')

        # 5) Cài đặt trục X
        ax.set_xticks(index + bar_width / 2)  # Đặt nhãn ngày ở giữa 2 cột
        ax.set_xticklabels(days)
        ax.set_ylabel('Amount')
        ax.set_ylim(0, 550)
        ax.set_xlabel('Day')
        ax.set_title('Expense vs Income')
        ax.legend()

        # Chuyển Figure thành widget Canvas
        plt.tight_layout()
        canvas = FigureCanvas(fig)
        # Thêm Canvas vào layout đã truyền vào

        layout.addWidget(canvas)