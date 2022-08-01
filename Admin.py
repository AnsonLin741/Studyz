import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QAbstractItemView, QMessageBox, QTableWidgetItem, \
    QLineEdit, QPushButton, QHeaderView, QLabel, QCheckBox, QHBoxLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from Database import Database

# AdminWindow class
class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()  
        self.table = QTableWidget(self)  # table widget from pyqt5
        self.database = Database('./data.db') # Database 
        self.check_list = []  # check list
        self.show_password_flag = False  # Show password flag
        self.select_all_flag = False  # Select all
        self.main_window = None
        self.set_ui()

    # connect to main window
    def set_main_window(self, widget):
        self.main_window = widget

    # setting up ui
    def set_ui(self):
        self.setWindowTitle("Management page")
        self.setFixedSize(1200, 800)
        self.font = QFont("Consolas")
        self.setFont(self.font)
        self.setWindowIcon(QIcon("./IMG/studyz.png"))  # set window icon
        self.add_table()  # create table
        self.get_all_user()
        self.add_line_edit()  # add typing column
        self.add_label()
        self.add_button()

    # adding table
    def add_table(self):
        self.table.setFixedWidth(1000)  
        self.table.setFixedHeight(500)  
        self.table.move(10, 30)  
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  
        self.table.horizontalHeader().setFont(self.font)  # set font
        
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  
        self.table.setColumnCount(4)  
        self.table.setHorizontalHeaderLabels(["Choice", "username", "password", 'created_time'])  
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.table.verticalHeader().hide()  
        self.table.setSortingEnabled(False)  

    # getting all user information from database
    def get_all_user(self):
        data = self.database.read_table() 
        for user in data:
            self.add_row(user[0], user[1], user[2])

    # displaying all user information
    def add_row(self, username, password, created_time):
        row = self.table.rowCount()  
        self.table.setRowCount(row + 1)  
        self.table.setItem(row, 1, QTableWidgetItem(str(username)))  
        self.table.setItem(row, 2, QTableWidgetItem(str(password)))
        self.table.setItem(row, 3, QTableWidgetItem(str(created_time)))
        widget = QWidget()
        check = QCheckBox()
        self.check_list.append(check)  
        check_lay = QHBoxLayout()
        check_lay.addWidget(check)
        check_lay.setAlignment(Qt.AlignCenter)
        widget.setLayout(check_lay)
        self.table.setCellWidget(row, 0, widget)

    # editing typing columns 
    def add_line_edit(self):
        self.username_edit = QLineEdit(self)
        self.username_edit.setFixedSize(240, 40)
        self.username_edit.move(760, 600)
        self.username_edit.setPlaceholderText('username')

        self.password_edit = QLineEdit(self)
        self.password_edit.setFixedSize(240, 40)
        self.password_edit.move(760, 660)
        self.password_edit.setPlaceholderText('password')
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.update_username_edit = QLineEdit(self)
        self.update_username_edit.setFixedSize(240, 40)
        self.update_username_edit.move(160, 600)
        self.update_username_edit.setPlaceholderText('username')

        self.update_password_edit = QLineEdit(self)
        self.update_password_edit.setFixedSize(240, 40)
        self.update_password_edit.move(160, 660)
        self.update_password_edit.setPlaceholderText('new password')

    #function for show password
    def show_password(self):
        if self.show_password_flag:  
            self.password_edit.setEchoMode(QLineEdit.Password)
            self.show_password_flag = False
            self.show_password_button.setText('Show')
        else:  
            self.password_edit.setEchoMode(QLineEdit.Normal)
            self.show_password_flag = True
            self.show_password_button.setText("Hide")

    # add labels for typing columns
    def add_label(self):
        self.username_label = QLabel(self)
        self.username_label.setFixedSize(160, 40)
        self.username_label.move(640, 600)
        self.username_label.setText('username')

        self.password_label = QLabel(self)
        self.password_label.setFixedSize(160, 40)
        self.password_label.move(640, 660)
        self.password_label.setText('password')

        self.update_username_label = QLabel(self)
        self.update_username_label.setFixedSize(160, 40)
        self.update_username_label.move(40, 600)
        self.update_username_label.setText('username')

        self.update_password_label = QLabel(self)
        self.update_password_label.setFixedSize(160, 40)
        self.update_password_label.move(40, 660)
        self.update_password_label.setText('password')

    # adding all the buttons for the interface
    def add_button(self):
        self.delete_button = QPushButton(self)
        self.update_button = QPushButton(self)
        self.add_button_ = QPushButton(self)
        self.show_password_button = QPushButton(self)
        self.clear_button = QPushButton(self)
        self.select_all_button = QPushButton(self)
        self.refresh_button = QPushButton(self)
        self.main_window_button = QPushButton(self)

        self.delete_button.setText("Delete")
        self.update_button.setText("Update")
        self.add_button_.setText("Add")
        self.show_password_button.setText("Show")
        self.clear_button.setText("Clear")
        self.select_all_button.setText("Select All")
        self.refresh_button.setText("Refresh")
        self.main_window_button.setText("Main window")

        self.delete_button.setToolTip("Delete the selected user, you can choose multiple users")
        self.clear_button.setToolTip("Clear all the users, including the super user, but the super user will be "
                                     "created later by default")
        self.select_all_button.setToolTip("Select all the users, including the super user")
        self.show_password_button.setToolTip("Show or hide the password")
        self.add_button_.setToolTip("Add a new user with the username and password in the input box")
        self.update_button.setToolTip("Update the password with the chosen username")
        self.refresh_button.setToolTip("Click here to refresh the table")
        self.main_window_button.setToolTip("Click here and you will go to the user interface")

        self.delete_button.move(1040, 340)
        self.select_all_button.move(1040, 280)
        self.clear_button.move(1040, 400)
        self.refresh_button.move(1040, 460)

        self.update_button.move(430, 600)
        self.add_button_.move(1020, 600)
        self.show_password_button.move(1020, 660)

        self.main_window_button.move(500,720)

        self.delete_button.clicked.connect(self.delete_user)
        self.select_all_button.clicked.connect(self.select_all)
        self.clear_button.clicked.connect(self.clear)
        self.show_password_button.clicked.connect(self.show_password)
        self.add_button_.clicked.connect(self.add_user)
        self.update_button.clicked.connect(self.update_password)
        self.refresh_button.clicked.connect(self.refresh)
        self.main_window_button.clicked.connect(self.show_main_window)

        self.main_window_button.setFixedSize(200, 40)
    # show main window after clicking the button
    def show_main_window(self):
        self.main_window.show()

    # delete the selected user
    def delete_user(self):
        choose_list = []
        for i in self.check_list:
            if i.isChecked():
                username = self.table.item(self.check_list.index(i), 1).text()
                if username == 'admin':
                    answer = QMessageBox.critical(self, 'Error', 'You are going to delete the super user, but it will be created later with the default password',
                                                  QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
                    if answer == QMessageBox.Yes:
                        choose_list.append(i)
                    if answer == QMessageBox.Cancel:
                        return
                else:
                    choose_list.append(i)

        for i in choose_list:
            username = self.table.item(self.check_list.index(i), 1).text()
            self.database.delete_table_by_username(username)
            self.table.removeRow(self.check_list.index(i))
            self.check_list.remove(i)
        self.database.create_table()

    # select all users
    def select_all(self):
        try:
            if not self.select_all_flag:
                for check in self.check_list:
                    check.setCheckState(2) 
                self.select_all_button.setText("Unselect")
                self.select_all_flag = True
            else:
                for check in self.check_list:
                    check.setCheckState(0) 
                self.select_all_button.setText("Select All")
                self.select_all_flag = False
        except:
            pass

    # add new user
    def add_user(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        if all((username, password)):
            flag = self.database.insert_table(username, password)
            if flag:
                QMessageBox.critical(self, 'Error', 'Already exists the username {}, please use another username'.format(username))
            else:
                self.add_row(username, password, self.database.get_time())
            self.username_edit.setText('') 
            self.password_edit.setText('')
        else:
            QMessageBox.critical(self, 'Error', "Please fill in the blanks")

    # clear all data in table and database
    def clear(self):
        self.table.clearContents()  
        self.table.setRowCount(0)  
        self.database.clear()  

    def update_password(self):
        username = self.update_username_edit.text()
        password = self.update_password_edit.text()
        if len(password) >= 6:
            self.database.update_table(username, password)
            self.change_table(username, password)
            self.update_password_edit.setText('')
            self.update_username_edit.setText('')
        else:
            QMessageBox.information(self, 'Error', 'Password is too short, at least 6 words',  QMessageBox.Yes, QMessageBox.Yes)

    def change_table(self, username, password):
        find_flag = False
        for row in range(self.table.rowCount()):
            username_find = self.table.item(row, 1).text()
            if username_find == username:
                self.table.item(row, 2).setText(password)
                find_flag = True
                break
        if not find_flag: 
            QMessageBox.information(self, 'prompt', 'Can not find the username {}'.format(username))

    # refresh table
    def refresh(self):
        self.table.clearContents()
        self.check_list.clear()
        self.table.setRowCount(0)
        self.database.create_table()
        self.get_all_user()

#show admin window
if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = AdminWindow()
    admin.show()
    sys.exit(app.exec_())
