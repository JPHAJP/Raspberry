from PyQt6.QtWidgets import *

global count_clicks
count_clicks = 1

app = QApplication([])
button = QPushButton('Click')

def on_button_clicked():
    global count_clicks
    alert = QMessageBox()
    alert.setText(f'clicked {count_clicks} times!')
    alert.exec()
    count_clicks += 1
      
button.clicked.connect(on_button_clicked)
button.show()
app.exec()
