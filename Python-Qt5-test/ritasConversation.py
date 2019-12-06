from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QBoxLayout, QPushButton, QVBoxLayout, QHBoxLayout

app = QApplication([])
window = QWidget()

title = QLabel("Rita's conversation")

pathChooser = QHBoxLayout()
pathChooser.addWidget(QLabel('Choose path'))
pathChooser.addWidget(QPushButton('Choose'))

path = QHBoxLayout()
path.addWidget(QLabel('Path:'))
path.addWidget(QLabel('here is choosed path'))

optionsText = QLabel('Options')


layout = QVBoxLayout()
layout.addWidget(title)
layout.addLayout(pathChooser)
layout.addLayout(path)
layout.addWidget(optionsText)
#layout.addWidget(QLabel('Test app'))
#layout.addWidget(QPushButton('Button1'))
#layout.addWidget(QPushButton('Button2'))
window.setLayout(layout)
window.show()
app.exec_()
