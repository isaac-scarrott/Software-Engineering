import simplejson as json
import os
from selenium import webdriver
import time
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys
import subprocess
from sys import platform as _platform
		


class Window(QtWidgets.QWidget):
	
	def __init__(self):
		super(Window, self).__init__()
		
		self.init_ui()

	def init_ui(self):
		self.setWindowTitle("Movie self.database Search Tool")
		self.setGeometry(300, 200, 800, 500)

		# self.setStyleSheet("background-color:white;");

		data = {"Title":"","Year":"","Rated":"","Released":"","Runtime":"","Genre":"","Director":"","Writer":"","Actors":"","Plot":"","Language":"","Country":"","Awards":"","Poster":"","Ratings":[{"Source":"","Value":""},{"Source":"","Value":""},{"Source":"","Value":""}],"Metascore":"","imdbRating":"","imdbVotes":"","imdbID":"","Type":"","DVD":"","BoxOffice":"","Production":"","Website":"","Response":""}


		self.LTitle = QtWidgets.QLabel("Group 2C Movie Search Tool")
		self.LMovieTitle = QtWidgets.QLabel("<b>Movie Title:</b> " + data.get("Title"))
		self.LMovieRelease = QtWidgets.QLabel("<b>Release Date: " + data.get("Released"))
		self.LMovieAge = QtWidgets.QLabel("<b>Age Rating: " + data.get("Rated"))
		self.LMovieRunTime = QtWidgets.QLabel("<b>Runtime: " + data.get("Runtime"))
		self.LMovieGenre = QtWidgets.QLabel("<b>Genre: " + data.get("Genre"))
		self.LMovieDirector = QtWidgets.QLabel("<b>Director(s): " + data.get("Director"))
		self.LMovieWriter = QtWidgets.QLabel("<b>Writer(s): " + data.get("Writer"))
		self.LMovieimdbRating = QtWidgets.QLabel("<b>IMDB Rating: " + data.get("imdbRating"))
		self.LMovieProduction = QtWidgets.QLabel("<b>Production Company: " + data.get("Production"))

		
		image = QtWidgets.QLabel(self)
		pixmap = QtGui.QPixmap('UOL_logo.png')
		image.setPixmap(pixmap)

		button = QtWidgets.QPushButton("Click to search for a movie")

		button.clicked.connect(self.btn_click)

		grid = QtWidgets.QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(self.LTitle, 1, 0)
		grid.addWidget(image, 1, 1)
		grid.addWidget(self.LMovieTitle, 3, 0, 1, 2)
		grid.addWidget(self.LMovieRelease, 4, 0, 1, 2)
		grid.addWidget(self.LMovieAge, 5, 0, 1, 2)
		grid.addWidget(self.LMovieRunTime, 6, 0, 1, 2)
		grid.addWidget(self.LMovieDirector, 7, 0, 1, 2)
		grid.addWidget(self.LMovieWriter, 8, 0, 1, 2)
		grid.addWidget(self.LMovieimdbRating, 9, 0, 1, 2)
		grid.addWidget(self.LMovieProduction, 10, 0, 1, 2)

		self.LMovieTitle.setWordWrap(True)
		self.LMovieRelease.setWordWrap(True)
		self.LMovieAge.setWordWrap(True)
		self.LMovieRunTime.setWordWrap(True)
		self.LMovieGenre.setWordWrap(True)
		self.LMovieDirector.setWordWrap(True)
		self.LMovieWriter.setWordWrap(True)
		self.LMovieimdbRating.setWordWrap(True)
		self.LMovieProduction.setWordWrap(True)

		self.myFont = QtGui.QFont()
		self.myFont.setBold(True)
		self.myFont.setPointSize(20)

		self.LTitle.setFont(self.myFont)


		image.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

		grid.addWidget(button, 2, 0, 1, 2)

		self.setLayout(grid) 

		# self.LMovieWriter.setMaximumWidth(300)

		

	def btn_click(self, input):

		text, okPressed = QtWidgets.QInputDialog.getText(self, "Movie Search","Movie Title:", QtWidgets.QLineEdit.Normal, "")
		if okPressed and text != '':
			
			data = {"Title":"","Year":"","Rated":"","Released":"","Runtime":"","Genre":"","Director":"","Writer":"","Actors":"","Plot":"","Language":"","Country":"","Awards":"","Poster":"","Ratings":[{"Source":"","Value":""},{"Source":"","Value":""},{"Source":"","Value":""}],"Metascore":"","imdbRating":"","imdbVotes":"","imdbID":"","Type":"","DVD":"","BoxOffice":"","Production":"","Website":"","Response":""}

			if _platform == "darwin":
			   br = webdriver.Firefox(executable_path="Firefox Webdrivers/geckodriver")
			elif _platform == "win32":
			   br = webdriver.Firefox(executable_path="Firefox Webdrivers/geckodriver32.exe")
			elif _platform == "win64":
				br = webdriver.Firefox(executable_path="Firefox Webdrivers/geckodriver64.exe")

			br.implicitly_wait(15) 
			br.get('http://www.omdbapi.com/')

			search = br.find_element_by_name('t')
			search.send_keys(text)
			search_button = br.find_element_by_id('search-by-title-button')
			search_button.click()
			search_return = br.find_element_by_class_name('alert-success').text
			data = json.loads(search_return)

			self.LMovieTitle.setText("<b>Release Date: </b>" + data.get("Title"))
			self.LMovieRelease.setText("<b>Release Date: </b>" + data.get("Released"))
			self.LMovieAge.setText("<b>Release Date: </b>" + data.get("Released"))
			self.LMovieRunTime.setText("<b>Runtime: </b>" + data.get("Runtime"))
			self.LMovieGenre.setText("<b>Genre: </b>" + data.get("Genre"))
			self.LMovieDirector.setText("<b>Director(s): </b>" + data.get("Director"))
			self.LMovieWriter.setText("<b>Writer(s): </b>" + data.get("Writer"))
			self.LMovieimdbRating.setText("<b>IMDB Rating: </b>" + data.get("imdbRating"))
			self.LMovieProduction.setText("<b>Production Company: </b>" + data.get("Production"))

			time.sleep(3)
			subprocess.call(['osascript', '-e', 'tell application "Firefox" to quit'])
			os.system("TASKKILL /F /IM firefox.exe")


if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	main_window = Window()
	main_window.show()
	sys.exit(app.exec_())

