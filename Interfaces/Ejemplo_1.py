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

# from PyQt6.QtWidgets import *

# count_clicks = [0]  # Usamos una lista para almacenar el conteo de clics

# app = QApplication([])
# button = QPushButton('Click')

# button.clicked.connect(lambda: (QMessageBox().setText(f'clicked {count_clicks[0]} times!').exec(), count_clicks.__setitem__(0, count_clicks[0] + 1)))
# button.show()
# app.exec()