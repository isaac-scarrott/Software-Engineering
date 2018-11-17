import simplejson as json
import os
from selenium import webdriver
import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
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
		self.LMovieTitle = QtWidgets.QLabel("Movie Title: " + data.get("Title"))
		self.LMovieRelease = QtWidgets.QLabel("Release Date8: " + data.get("Released"))
		self.LMovieAge = QtWidgets.QLabel("Age Rating: " + data.get("Rated"))
		self.LMovieRunTime = QtWidgets.QLabel("Runtime: " + data.get("Runtime"))
		self.LMovieGenre = QtWidgets.QLabel("Genre: " + data.get("Genre"))
		self.LMovieDirector = QtWidgets.QLabel("Director(s): " + data.get("Director"))
		self.LMovieWriter = QtWidgets.QLabel("Writer(s): " + data.get("Writer"))
		self.LMovieimdbRating = QtWidgets.QLabel("IMDB Rating: " + data.get("imdbRating"))
		self.LMovieProduction = QtWidgets.QLabel("Production Company: " + data.get("Production"))
		button = QtWidgets.QPushButton("Click to search for a movie")

		button.clicked.connect(self.btn_click)

		grid = QtWidgets.QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(self.LTitle, 1, 0)
		grid.addWidget(self.LMovieTitle, 3, 0)
		grid.addWidget(self.LMovieRelease, 4, 0)
		grid.addWidget(self.LMovieAge, 5, 0)
		grid.addWidget(self.LMovieRunTime, 6, 0)
		grid.addWidget(self.LMovieDirector, 7, 0)
		grid.addWidget(self.LMovieWriter, 8, 0)
		grid.addWidget(self.LMovieimdbRating, 9, 0)
		grid.addWidget(self.LMovieProduction, 10, 0)

		grid.addWidget(button, 2, 0)

		self.setLayout(grid) 

		# self.LMovieWriter.setMaximumWidth(300)

		

	def btn_click(self, input):

		text, okPressed = QtWidgets.QInputDialog.getText(self, "Movie Search","Movie Title:", QtWidgets.QLineEdit.Normal, "")
		if okPressed and text != '':
			
			data = {"Title":"","Year":"","Rated":"","Released":"","Runtime":"","Genre":"","Director":"","Writer":"","Actors":"","Plot":"","Language":"","Country":"","Awards":"","Poster":"","Ratings":[{"Source":"","Value":""},{"Source":"","Value":""},{"Source":"","Value":""}],"Metascore":"","imdbRating":"","imdbVotes":"","imdbID":"","Type":"","DVD":"","BoxOffice":"","Production":"","Website":"","Response":""}

			if _platform == "darwin":
			   br = webdriver.Firefox(executable_path="/Users/isaacscarrott/Universirty Work/Software Engineering/Programming/webdrivers/firefox/geckodriver")
			elif _platform == "win32":
			   br = webdriver.Firefox(executable_path="C:/Users/Kyle/Desktop/geckodriver.exe")
			elif _platform == "win64":
			    br = webdriver.Firefox(executable_path="C:/Users/Kyle/Desktop/geckodriver.exe")

			br.implicitly_wait(15) 
			br.get('http://www.omdbapi.com/')

			search = br.find_element_by_name('t')
			search.send_keys(text)
			search_button = br.find_element_by_id('search-by-title-button')
			search_button.click()
			search_return = br.find_element_by_class_name('alert-success').text
			data = json.loads(search_return)
			
			
			OLMovieRelease = QtWidgets.QLabel("Release Date8: " + data.get("Released"))
			OLMovieAge = QtWidgets.QLabel("Age Rating: " + data.get("Rated"))
			OLMovieRunTime = QtWidgets.QLabel("Runtime: " + data.get("Runtime"))
			OLMovieGenre = QtWidgets.QLabel("Genre: " + data.get("Genre"))
			OLMovieDirector = QtWidgets.QLabel("Director(s): " + data.get("Director"))
			OLMovieWriter = QtWidgets.QLabel("Writer(s): " + data.get("Writer"))
			OLMovieimdbRating = QtWidgets.QLabel("IMDB Rating: " + data.get("imdbRating"))
			OLMovieProduction = QtWidgets.QLabel("Production Company: " + data.get("Production"))

			self.LMovieTitle.setText("Release Date: " + data.get("Title"))
			self.LMovieRelease.setText("Release Date: " + data.get("Released"))
			self.LMovieRunTime.setText("Runtime: " + data.get("Runtime"))
			self.LMovieGenre.setText("Genre: " + data.get("Genre"))
			self.LMovieDirector.setText("Director(s): " + data.get("Director"))
			self.LMovieWriter.setText("Writer(s): " + data.get("Writer"))
			self.LMovieimdbRating.setText("IMDB Rating: " + data.get("imdbRating"))
			self.LMovieProduction.setText("Production Company: " + data.get("Production"))

			time.sleep(3)
			subprocess.call(['osascript', '-e', 'tell application "Firefox" to quit'])
			os.system("TASKKILL /F /IM firefox.exe")


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec_())

