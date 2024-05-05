self.Articulo_ejemplo = QtWidgets.QWidget(self.scrollAreaWidgetContents)
self.Articulo_ejemplo.setMinimumSize(QtCore.QSize(380, 100))
self.Articulo_ejemplo.setMaximumSize(QtCore.QSize(16777215, 100))
self.Articulo_ejemplo.setObjectName("Articulo_ejemplo")
self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.Articulo_ejemplo)
self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
self.horizontalLayout_31.setObjectName("horizontalLayout_31")
self.img_ejemplo = QtWidgets.QWidget(self.Articulo_ejemplo)
self.img_ejemplo.setMinimumSize(QtCore.QSize(100, 100))
self.img_ejemplo.setMaximumSize(QtCore.QSize(100, 100))
self.img_ejemplo.setStyleSheet("background-image: url(:/Imagenes/bolillo.png);\n"
"border-radius: 30px;")

self.img_ejemplo.setObjectName("img_ejemplo")
self.horizontalLayout_31.addWidget(self.img_ejemplo)
self.widget_29_ejemplo = QtWidgets.QWidget(self.Articulo_ejemplo)
self.widget_29_ejemplo.setObjectName("widget_29_ejemplo")
self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_29_ejemplo)
self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
self.verticalLayout_15.setObjectName("verticalLayout_15")
self.widget_37_ejemplo = QtWidgets.QWidget(self.widget_29_ejemplo)
self.widget_37_ejemplo.setObjectName("widget_37_ejemplo")
self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.widget_37_ejemplo)
self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
self.horizontalLayout_32.setObjectName("horizontalLayout_32")
self.articulo_label_ejemplo = QtWidgets.QLabel(self.widget_37_ejemplo)
font = QtGui.QFont()
font.setFamily("Cascadia Mono")
font.setPointSize(25)
font.setBold(True)
font.setWeight(75)
self.articulo_label_ejemplo.setFont(font)
self.articulo_label_ejemplo.setAlignment(QtCore.Qt.AlignCenter)
self.articulo_label_ejemplo.setObjectName("articulo_label_ejemplo")
self.horizontalLayout_32.addWidget(self.articulo_label_ejemplo)
self.precio_label_ejemplo = QtWidgets.QLabel(self.widget_37_ejemplo)
font = QtGui.QFont()
font.setFamily("Cascadia Mono")
font.setPointSize(25)
font.setBold(True)
font.setWeight(75)
self.precio_label_ejemplo.setFont(font)
self.precio_label_ejemplo.setObjectName("precio_label_ejemplo")
self.horizontalLayout_32.addWidget(self.precio_label_ejemplo)
self.verticalLayout_15.addWidget(self.widget_37_ejemplo)
self.widget_33_ejemplo = QtWidgets.QWidget(self.widget_29_ejemplo)
font = QtGui.QFont()
font.setFamily("Cascadia Mono")
self.widget_33_ejemplo.setFont(font)
self.widget_33_ejemplo.setObjectName("widget_33_ejemplo")
self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.widget_33_ejemplo)
self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
self.horizontalLayout_30.setObjectName("horizontalLayout_30")
self.minus_button_ejemplo = QtWidgets.QPushButton(self.widget_33_ejemplo)
self.minus_button_ejemplo.setMinimumSize(QtCore.QSize(45, 45))
self.minus_button_ejemplo.setMaximumSize(QtCore.QSize(45, 45))
font = QtGui.QFont()
font.setFamily("Cascadia Mono")
font.setPointSize(30)
self.minus_button_ejemplo.setFont(font)
self.minus_button_ejemplo.setStyleSheet("QPushButton{\n"
"background-color: rgb(77, 45, 18);\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 5px;\n"
"border-radius: 22px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"border-width: 1px;\n"
"background-color: rgb(115, 67, 26);\n"
"color: white;\n"
"}")
self.minus_button_ejemplo.setObjectName("minus_button_ejemplo")
self.horizontalLayout_30.addWidget(self.minus_button_ejemplo)
self.label_16_ejemplo = QtWidgets.QLabel(self.widget_33_ejemplo)
self.label_16_ejemplo.setMinimumSize(QtCore.QSize(45, 45))
self.label_16_ejemplo.setMaximumSize(QtCore.QSize(45, 45))
font = QtGui.QFont()
font.setFamily("Cascadia Mono")
font.setPointSize(25)
font.setItalic(True)
self.label_16_ejemplo.setFont(font)
self.label_16_ejemplo.setAlignment(QtCore.Qt.AlignCenter)
self.label_16_ejemplo.setObjectName("label_16_ejemplo")
self.horizontalLayout_30.addWidget(self.label_16_ejemplo)
self.qty_label_ejemplo = QtWidgets.QLabel(self.widget_33_ejemplo)
font = QtGui.QFont()
font.setFamily("Cascadia Mono")
font.setPointSize(25)
font.setItalic(True)
self.qty_label_ejemplo.setFont(font)
self.qty_label_ejemplo.setObjectName("qty_label_ejemplo")
self.horizontalLayout_30.addWidget(self.qty_label_ejemplo)
self.plus_button_ejemplo = QtWidgets.QPushButton(self.widget_33_ejemplo)
self.plus_button_ejemplo.setMinimumSize(QtCore.QSize(45, 45))
self.plus_button_ejemplo.setMaximumSize(QtCore.QSize(45, 45))
font = QtGui.QFont()
font.setFamily("Cascadia Mono")
font.setPointSize(30)
self.plus_button_ejemplo.setFont(font)
self.plus_button_ejemplo.setStyleSheet("QPushButton{\n"
"background-color: rgb(77, 45, 18);\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 5px;\n"
"border-radius: 22px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"border-width: 1px;\n"
"background-color: rgb(115, 67, 26);\n"
"color: white;\n"
"}")
self.plus_button_ejemplo.setObjectName("plus_button_ejemplo")
self.horizontalLayout_30.addWidget(self.plus_button_ejemplo)
spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
self.horizontalLayout_30.addItem(spacerItem5)
self.trash_button_ejemplo = QtWidgets.QPushButton(self.widget_33_ejemplo)
self.trash_button_ejemplo.setMinimumSize(QtCore.QSize(45, 45))
self.trash_button_ejemplo.setMaximumSize(QtCore.QSize(45, 45))
self.trash_button_ejemplo.setStyleSheet("QPushButton{\n"
"background-color: rgb(77, 45, 18);\n"
"image: url(:/Logo/basura.png);\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 5px;\n"
"border-radius: 22px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"border-width: 1px;\n"
"background-color: rgb(115, 67, 26);\n"
"color: white;\n"
"}")
self.trash_button_ejemplo.setText("")
self.trash_button_ejemplo.setObjectName("trash_button_ejemplo")
self.horizontalLayout_30.addWidget(self.trash_button_ejemplo)
self.verticalLayout_15.addWidget(self.widget_33_ejemplo)
self.horizontalLayout_31.addWidget(self.widget_29_ejemplo)
self.verticalLayout_8.addWidget(self.Articulo_ejemplo)