import os
import sys
from Sign_Up import SignWindow 
from Admin import AdminWindow
from Database import Database
from Main import Studyz
try:
    import PyQt5
except ModuleNotFoundError:
    os.system("pip install PyQt5")
    from PyQt5.Qt import *
else:
    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QFrame, QMessageBox, QComboBox
    from PyQt5.QtGui import QIcon, QFont
    from PyQt5.QtCore import Qt


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = QIcon("./IMG/studyz.png")
        self.database = Database('./data.db')
        self.sign_up_win = SignWindow()  # create a sign up window
        self.admin_win = AdminWindow()  # create a admin window
        self.main_win = Studyz()  # goes to main after login
        self.admin_win.set_main_window(self.main_win)
        self.setWindowTitle("Login")
        self.setFixedSize(1000, 800)
        self.set_ui()

    def change_icon(self):
        self.setWindowIcon(self.icon)

    def set_ui(self):
        self.set_background_image()  # background image
        self.change_icon()
        self.add_label()
        self.add_line_edit()
        self.add_button()

    def add_label(self):
        # set font
        label_font = QFont()
        label_font.setFamily('Consolas')
        label_font.setPixelSize(30)

        # create text label
        self.username_label = QLabel(self)
        self.password_label = QLabel(self)

        # set text
        self.username_label.setText("username")
        self.password_label.setText("password")

        # label size
        self.username_label.setFixedSize(240, 40)
        self.password_label.setFixedSize(240, 40)

        # label position
        self.username_label.move(120, 530)
        self.password_label.move(120, 600)

        self.username_label.setFont(label_font)
        self.password_label.setFont(label_font)

    def add_line_edit(self):
        line_edit_font = QFont()
        line_edit_font.setFamily('Consolas')
        line_edit_font.setPixelSize(30)

        # create line edit
        self.username_edit = QLineEdit(self)
        self.password_edit = QLineEdit(self)

        # set password format
        self.password_edit.setEchoMode(QLineEdit.Password)

        # set font
        self.username_edit.setFont(line_edit_font)
        self.password_edit.setFont(line_edit_font)

        # place holder text
        self.username_edit.setPlaceholderText("username")
        self.password_edit.setPlaceholderText("password")

        # set size
        self.username_edit.setFixedSize(350, 40)
        self.password_edit.setFixedSize(350, 40)

        # set position
        self.username_edit.move(320, 530)
        self.password_edit.move(320, 600)

    #add button
    def add_button(self):
        button_font = QFont()
        button_font.setFamily('Consolas')
        button_font.setPixelSize(30)

        self.login_button = QPushButton("Login", self)
        self.sign_button = QPushButton(self)

        self.login_button.setFixedSize(160, 50)
        self.sign_button.setFixedSize(160, 50)

        self.login_button.setFont(button_font)
        self.sign_button.setFont(button_font)

        self.login_button.move(750, 530)
        self.sign_button.move(750, 600)

        self.login_button.setText("Login")
        self.sign_button.setText("Sign up")
        self.login_button.setToolTip('If you are the admin, please login in with the specific account')

        # button function
        self.login_button.clicked.connect(self.login)
        self.sign_button.clicked.connect(self.sign_up_window)

        self.login_button.setShortcut("Return")  # set shortcut keys

    def set_background_image(self):
        self.frame = QFrame(self)
        self.frame.resize(1000, 520)
        self.frame.move(400, 200)
        self.frame.setStyleSheet('background-image: url("./IMG/studyz.png"); background-repeat: no-repeat; text-align:center;')

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        data = self.database.find_password_by_username(username)  # search data in data base
        if username and password:  
            if data:
                if str(data[0][0]) == password:
                    QMessageBox.information(self, 'Successfully', 'Login in successful \n Welcome {}'.format(username),
                                            QMessageBox.Yes)
                    self.password_edit.setText('')
                    self.username_edit.setText('')
                    self.close()
                    if username == 'admin':  # if admin, directs to admin page
                        self.admin_win.show()
                    else:
                        self.main_win.show()

                else:
                    QMessageBox.information(self, 'Failed', 'Password is wrong, try again',
                                            QMessageBox.Yes)
            else:
                QMessageBox.information(self, 'Error', 'No such username', QMessageBox.Yes)
        elif username:  #
            QMessageBox.information(self, 'Error', 'Input your password', QMessageBox.Yes)
        else:
            QMessageBox.information(self, 'Error', 'Fill in the blank', QMessageBox.Yes)
    #programme display sign up window
    def sign_up_window(self):
        self.sign_up_win.setWindowIcon(self.icon)
        self.sign_up_win.move(self.x() + 100, self.y() + 100)
        frame = QFrame(self.sign_up_win)
        self.sign_up_win.setWindowFlag(Qt.Dialog)
        frame.resize(1000, 300)
        frame.setStyleSheet('background-image: url("./IMG/studyz.png"); background-repeat: no-repeat; text-align:center;')
        frame.move(400, 200)
        #when open sign up window, clear the old information
        self.password_edit.setText('')
        self.username_edit.setText('')
        self.sign_up_win.show()

    def closeEvent(self, event):
        self.sign_up_win.close()  #if close login window, close sign up window too

#show the login window
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())
