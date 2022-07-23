from PyQt5.QtWidgets import QLabel, QLineEdit, QWidget, QPushButton, \
    QMessageBox, QApplication
from PyQt5.QtGui import QFont
from Database import Database
import sys


class SignWindow(QWidget):
    def __init__(self):
        super(SignWindow, self).__init__()
        self.database = Database('./data.db')
        self.setWindowTitle("Sign up")  # setup title
        self.resize(1000, 800)  # size of window
        self.set_ui()

    def set_ui(self):  
        self.add_line_edit()
        self.add_button()
        self.add_label()

    def add_label(self):
        label_font = QFont()
        label_font.setFamily('Consolas')
        label_font.setPixelSize(35)

        self.username_label = QLabel(self)
        self.password_label = QLabel(self)
        self.confirm_label = QLabel(self)

        self.username_label.setText("username")
        self.password_label.setText("password")
        self.confirm_label.setText("confirmed")

        self.username_label.setFixedSize(240, 40)
        self.password_label.setFixedSize(240, 40)
        self.confirm_label.setFixedSize(240, 40)

        self.username_label.move(120, 530)
        self.password_label.move(120, 600)
        self.confirm_label.move(120, 670)

        # font
        self.username_label.setFont(label_font)
        self.password_label.setFont(label_font)
        self.confirm_label.setFont(label_font)

    def add_line_edit(self):
        line_edit_font = QFont()
        line_edit_font.setFamily('Consolas')
        line_edit_font.setPixelSize(30)

        self.username_edit = QLineEdit(self)
        self.password_edit = QLineEdit(self)
        self.confirm_edit = QLineEdit(self)

        self.password_edit.setEchoMode(QLineEdit.Password)
        self.confirm_edit.setEchoMode(QLineEdit.Password)

        #font
        self.username_edit.setFont(line_edit_font)
        self.password_edit.setFont(line_edit_font)
        self.confirm_edit.setFont(line_edit_font)

        self.username_edit.setPlaceholderText("username")
        self.password_edit.setPlaceholderText("password")
        self.confirm_edit.setPlaceholderText('password again')

        #size
        self.username_edit.setFixedSize(350, 40)
        self.password_edit.setFixedSize(350, 40)
        self.confirm_edit.setFixedSize(350, 40)

        self.username_edit.move(320, 530)
        self.password_edit.move(320, 600)
        self.confirm_edit.move(320, 670)

    def add_button(self):
        button_font = QFont()
        button_font.setFamily('Consolas')
        button_font.setPixelSize(30)

        self.sign_button = QPushButton(self)
        self.sign_button.setFixedSize(160, 50)
        self.sign_button.setFont(button_font)
        self.sign_button.move(750, 600)
        self.sign_button.setText("Sign up")

        self.sign_button.setShortcut('Return')

        self.sign_button.clicked.connect(self.sign_up)

    def sign_up(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        confirm = self.confirm_edit.text()

        if not password or not confirm:
            QMessageBox.information(self, 'Error', 'The password is empty',
                                    QMessageBox.Yes)
        elif self.database.is_has(username):  
            QMessageBox.information(self, 'Error',
                                    'The username already exists',
                                    QMessageBox.Yes)
        else:
            if password == confirm and password:  
                if len(username) < 5:
                    QMessageBox.information(self, 'Error',
                                            'The username is too short, change it for a long one, at least 5 words',
                                            QMessageBox.Yes, QMessageBox.Yes)
                    return
                if len(password) < 6:
                    QMessageBox.information(self, 'Error',
                                            'You password\'s length is less than 6, please input again',
                                            QMessageBox.Yes)
                    return
                else:
                    self.database.insert_table(username, password)  
                    QMessageBox.information(self, 'Successfully',
                                            'Sign up successfully'.format(
                                                username),
                                            QMessageBox.Yes)
                    self.close()  
            else:
                QMessageBox.information(self, 'Error',
                                        'The password is not equal',
                                        QMessageBox.Yes)

    def closeEvent(self, event):
        self.username_edit.setText('')
        self.confirm_edit.setText('')
        self.password_edit.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignWindow()
    window.show()

    sys.exit(app.exec_())
