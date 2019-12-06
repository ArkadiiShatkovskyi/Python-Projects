from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QBoxLayout, QPushButton, QVBoxLayout, QHBoxLayout

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()

title = QHBoxLayout()
title.insertSpacing(60, 60)
title.addWidget(QLabel("Rita's conversation"))
title.insertSpacing(60, 60)

pathChooser = QHBoxLayout()
pathChooser.addWidget(QLabel('Choose path'))
pathChooser.addWidget(QPushButton('Choose'))

path = QHBoxLayout()
path.addWidget(QLabel('Path:'))
path.addWidget(QLabel('here is choosed path'))


optionsText = QHBoxLayout()
optionsText.insertSpacing(100, 100)
optionsText.addWidget(QLabel('Options'))
optionsText.insertSpacing(100, 100)

layout = QVBoxLayout()
layout.addLayout(title)
layout.addLayout(pathChooser)
layout.addLayout(path)
layout.addLayout(optionsText)
window.setLayout(layout)
window.show()
app.exec_()
