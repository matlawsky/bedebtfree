from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_ui import Ui_MainWindow
from edit_ui import Ui_EditDebt
from editp_ui import Ui_EditPayment
from add_ui import Ui_AddDebt
from addp_ui import Ui_AddPayment
from delete_ui import Ui_Dialog
from api import get_all

class AddDebtDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super(AddDebtDialog, self).__init__(parent)
        self.ui = Ui_AddDebt()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

class AddPaymentDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super(AddPaymentDialog, self).__init__(parent)
        self.ui = Ui_AddPayment()
        self.ui.setupUi(self)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("BeDebtFree")
        self.newDebtButton.pressed.connect(self.show_add_debt_dialog)
        self.newPaymentButton.clicked.connect(self.show_add_payment_dialog)
        self.all = get_all()
        self.wise.setText(f"Wise man {self.all[0]} \n said: {self.all[1]} \n")

    def show_add_debt_dialog(self):
        input_dlg = AddDebtDialog()
        input_dlg.exec()

    def show_add_payment_dialog(self):
        input_dlg = AddPaymentDialog()
        input_dlg.exec()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
