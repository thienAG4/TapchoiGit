from Home_Interaction.Charts import Charts
from Home_Interaction.Elements import Element
from Home import Ui_MainWindow

class HomeExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Khởi tạo module biểu đồ
        self.charts = Charts(incomme="D:\\Do_An_KTLT\\Modules\\Home\\data\\incomes.json",expense="D:\\Do_An_KTLT\\Modules\\Home\\data\\expenses.json")
        self.elements=Element(incomes="D:\\Do_An_KTLT\\Modules\\Home\\data\\incomes.json",expenses="D:\\Do_An_KTLT\\Modules\\Home\\data\\expenses.json")

        # Giả sử frameWeeklyActivity và frameExpensesStatistics là các QWidget trong giao diện của bạn
        # Tạo layout cho các widget placeholder này
        self.layoutWeekly = self.Columnchart
        self.layoutExpenses = self.Piechart

        # Gọi hàm show chart, truyền đúng QVBoxLayout
        self.charts.ColumnChart(self.layoutWeekly)  # hiển thị biểu đồ cột ở ô màu đỏ thứ nhất
        self.charts.PieChart(self.layoutExpenses)  # hiển thị biểu đồ tròn ở ô màu đỏ thứ hai
        # self.showElements()
    def showElements(self): #k sài dc
        total_expenses =Element.total_expenses(self.elements)
        total_incomes =Element.total_incomes(self.elements)
        self.lineEdit_mybalance.setText(total_incomes-total_expenses)
        self.lineEdit_income.setText(total_incomes)
        self.lineEdit_expenses.setText(total_expenses)
