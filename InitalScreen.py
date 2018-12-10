from PyQt5 import QtWidgets, QtGui, QtCore

import pickle
import sys
import OMDB
import os

class InitalWindow(QtWidgets.QWidget):
	
	def __init__(self):
		super(InitalWindow, self).__init__()
		
		self.init_ui()

	def init_ui(self):
		self.setWindowTitle("Movie database Search Tool")
		self.setGeometry(450, 130, 550, 450)

		#Used to define all of the text that is displayed on the screen
		self.LTitle = QtWidgets.QLabel("Group B2 Movie Search Tool")
		self.LQuestion = QtWidgets.QLabel("Please pick an API to use")

		#Used to load the image in
		image = QtWidgets.QLabel(self)
		pixmap = QtGui.QPixmap('UOL_logo.png')
		image.setPixmap(pixmap)

		OMDB = QtWidgets.QPushButton("OMDB")
		themoviedb = QtWidgets.QPushButton("The Movie DB")

		#Used to define the layout type as a grid layout
		grid = QtWidgets.QGridLayout()
		grid.setSpacing(10)

		#Used to display all of the widgets. First value is the row, second value is the column, third is the number of rows that the widget spans across, fourth is the number of columns that the widget spans across
		grid.addWidget(self.LTitle, 0, 0)
		grid.addWidget(image, 0, 2)
		grid.addWidget(self.LQuestion, 1, 0, 2, 0)
		grid.addWidget(OMDB, 2, 0, 3, 1)
		grid.addWidget(themoviedb, 2, 1, 3, 2)

		OMDB.clicked.connect(self.OMDB_click)
		themoviedb.clicked.connect(self.themoviedb)

		self.LQuestion.setAlignment(QtCore.Qt.AlignCenter)

		#Makes some of the text bold and a bigger size
		self.myFont = QtGui.QFont()
		self.myFont.setBold(True)
		self.myFont.setPointSize(20)
		self.LTitle.setFont(self.myFont)

		#Places the uni of lincoln logo on the far right of the screen
		image.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

		#Uses grid layou
		self.setLayout(grid) 

	def OMDB_click(self):
		os.system('python OMDB.py')
		self.close();

	def themoviedb(self):
		os.system('python themoviedb.py')
		self.close();


if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	intial_window = InitalWindow()
	intial_window.show()
	sys.exit(app.exec_())
