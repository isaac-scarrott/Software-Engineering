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
import pickle
import re

class Window(QtWidgets.QWidget):
	
	def __init__(self):
		super(Window, self).__init__()
		
		self.init_ui()

	def init_ui(self):
		self.setWindowTitle("Movie self.self.database Search Tool")
		self.setGeometry(100, 130, 1200, 600)

		# self.setStyleSheet("background-color:white;");

		self.data = {"Title":"","Year":"","Rated":"","Released":"","Runtime":"","Genre":"","Director":"","Writer":"","Actors":"","Plot":"","Language":"","Country":"","Awards":"","Poster":"","Ratings":[{"Source":"","Value":""},{"Source":"","Value":""},{"Source":"","Value":""}],"Metascore":"","imdbRating":"","imdbVotes":"","imdbID":"","Type":"","DVD":"","BoxOffice":"","Production":"","Website":"","Response":""}

		self.LTitle = QtWidgets.QLabel("Group B2 Movie Search Tool")
		self.LMovieTitle = QtWidgets.QLabel("<b>Movie Title:</b> " + self.data.get("Title"))
		self.LMovieRelease = QtWidgets.QLabel("<b>Release Date: " + self.data.get("Released"))
		self.LMovieAge = QtWidgets.QLabel("<b>Age Rating: " + self.data.get("Rated"))
		self.LMovieRunTime = QtWidgets.QLabel("<b>Runtime: " + self.data.get("Runtime"))
		self.LMovieGenre = QtWidgets.QLabel("<b>Genre: " + self.data.get("Genre"))
		self.LMovieDirector = QtWidgets.QLabel("<b>Director(s): " + self.data.get("Director"))
		self.LMovieWriter = QtWidgets.QLabel("<b>Writer(s): " + self.data.get("Writer"))
		self.LMovieimdbRating = QtWidgets.QLabel("<b>IMDB Rating: " + self.data.get("imdbRating"))
		self.LMovieProduction = QtWidgets.QLabel("<b>Production Company: " + self.data.get("Production"))
		LWishlistTitle = QtWidgets.QLabel("<b>Wishlist</b>")

		self.listWidget = QtWidgets.QListWidget()

		image = QtWidgets.QLabel(self)
		pixmap = QtGui.QPixmap('UOL_logo.png')		
		image.setPixmap(pixmap)

		SearchButton = QtWidgets.QPushButton("Click to search for a movie")

		AddButton = QtWidgets.QPushButton("Add")
		RemoveButtom = QtWidgets.QPushButton("Remove")
		ViewButton = QtWidgets.QPushButton("View")
		CommentsButton = QtWidgets.QPushButton("Comments")

		SearchButton.clicked.connect(self.search_btn_click)
		AddButton.clicked.connect(self.add_btn_click)
		RemoveButtom.clicked.connect(self.remove_btn_click)
		ViewButton.clicked.connect(self.view_btn_click)

		grid = QtWidgets.QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(self.LTitle, 1, 0)
		grid.addWidget(image, 1, 3)
		grid.addWidget(self.LMovieTitle, 3, 0, 1, 2)
		grid.addWidget(self.LMovieRelease, 4, 0, 1, 2)
		grid.addWidget(self.LMovieAge, 5, 0, 1, 2)
		grid.addWidget(self.LMovieRunTime, 6, 0, 1, 2)
		grid.addWidget(self.LMovieDirector, 7, 0, 1, 2)
		grid.addWidget(self.LMovieWriter, 8, 0, 1, 2)
		grid.addWidget(self.LMovieimdbRating, 9, 0, 1, 2)
		grid.addWidget(self.LMovieProduction, 10, 0, 1, 2)
		grid.addWidget(self.listWidget, 4, 2, 7, 2)
		grid.addWidget(LWishlistTitle, 3, 2, 1, 1)

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

		grid.addWidget(SearchButton, 2, 0, 1, 4)
		grid.addWidget(CommentsButton, 11, 0, 1, 1)
		grid.addWidget(AddButton, 11, 1, 1, 1)
		grid.addWidget(RemoveButtom, 11, 2, 1, 1)
		grid.addWidget(ViewButton, 11, 3, 1, 1)

		self.setLayout(grid) 		

		with open('C:/Users/Kyle/Desktop/Version 5/Version 5/wishlist.txt', 'rb') as f:
			self.wishlistArray = pickle.load(f)
		for x in self.wishlistArray:
			self.listWidget.addItem(x)

	def search_btn_click(self):				

		text, okPressed = QtWidgets.QInputDialog.getText(self, "Movie Search","Movie Title:", QtWidgets.QLineEdit.Normal, "")
		if okPressed and text != '':
			
			self.data = {"Title":"","Year":"","Rated":"","Released":"","Runtime":"","Genre":"","Director":"","Writer":"","Actors":"","Plot":"","Language":"","Country":"","Awards":"","Poster":"","Ratings":[{"Source":"","Value":""},{"Source":"","Value":""},{"Source":"","Value":""}],"Metascore":"","imdbRating":"","imdbVotes":"","imdbID":"","Type":"","DVD":"","BoxOffice":"","Production":"","Website":"","Response":""}

			if _platform == "darwin":
			   br = webdriver.Firefox(executable_path="C:/Users/Kyle/Desktop/Version 5/Version 5/Firefox Webdrivers/geckodriver")
			elif _platform == "win32":
			   br = webdriver.Firefox(executable_path="C:/Users/Kyle/Desktop/Version 5/Version 5/Firefox Webdrivers/geckodriver32.exe")
			elif _platform == "win64":
				br = webdriver.Firefox(executable_path="C:/Users/Kyle/Desktop/Version 5/Version 5/Firefox Webdrivers/geckodriver64.exe")

			br.implicitly_wait(15) 

			br.get('https://api.themoviedb.org/3/search/movie?api_key=1e0dcaa7e93980fb84e1d2430d01b887&query=' + text)

			id_num = br.find_element_by_id('/results/0/id').text
			id_num = re.findall('\d', id_num)
			id = ''.join(map(str, id_num))			

			br.get('https://api.themoviedb.org/3/movie/' + id + '?api_key=1e0dcaa7e93980fb84e1d2430d01b887')

			search_button = br.find_element_by_id('rawdata-tab')
			search_button.click()
			search_return = br.find_element_by_class_name('data').text
			self.data = json.loads(search_return)
			poster = br.find_element_by_id('poster_path')

			#img = 'https://image.tmdb.org/t/p/w185' + poster_path)

			self.LMovieTitle.setText("<b>Movie Title: </b>" + self.data.get("title"))
			self.LMovieRelease.setText("<b>Release Date: </b>" + self.data.get("release_date"))			
			self.LMovieRunTime.setText("<b>Runtime: </b>" + str(self.data.get("runtime")))
			#self.LMovieGenre.setText("<b>Genre: </b>" + self.data.get("Genre"))			
			#self.LMovieProduction.setText("<b>Production Company: </b>" + self.data.get("name"))
				
			time.sleep(3)
			#subprocess.call(['osascript', '-e', 'tell application "Firefox" to quit'])
			os.system("TASKKILL /F /IM firefox.exe")

	def add_btn_click(self):
		if self.data.get("Title") not in self.wishlistArray:
			self.wishlistArray.append(self.data.get("Title"))
			self.listWidget.addItem(self.data.get("Title"))
			with open("C:/Users/Kyle/Desktop/Version 5/Version 5/wishlist.txt", 'wb') as f:
				pickle.dump(self.wishlistArray, f)
	
	def remove_btn_click(self):
		self.wishlistArray.remove(self.listWidget.currentItem().text())
		with open("C:/Users/Kyle/Desktop/Version 5/Version 5/wishlist.txt", 'wb') as f:
				pickle.dump(self.wishlistArray, f)
		item = self.listWidget.takeItem(self.listWidget.currentRow())
		item = None
	
	def view_btn_click(self):

			text = self.listWidget.currentItem().text()

			self.data = {"Title":"","Year":"","Rated":"","Released":"","Runtime":"","Genre":"","Director":"","Writer":"","Actors":"","Plot":"","Language":"","Country":"","Awards":"","Poster":"","Ratings":[{"Source":"","Value":""},{"Source":"","Value":""},{"Source":"","Value":""}],"Metascore":"","imdbRating":"","imdbVotes":"","imdbID":"","Type":"","DVD":"","BoxOffice":"","Production":"","Website":"","Response":""}

			if _platform == "darwin":
			   br = webdriver.Firefox(executable_path="C:/Users/Kyle/Desktop/Version 5/Version 5/Firefox Webdrivers/geckodriver")
			elif _platform == "win32":
			   br = webdriver.Firefox(executable_path="C:/Users/Kyle/Desktop/Version 5/Version 5/Firefox Webdrivers/geckodriver32.exe")
			elif _platform == "win64":
				br = webdriver.Firefox(executable_path="C:/Users/Kyle/Desktop/Version 5/Version 5/Firefox Webdrivers/geckodriver64.exe")

			br.implicitly_wait(15) 
			br.get('http://www.omdbapi.com/?t=' + text + '&apikey=53d59f58')

			search_button = br.find_element_by_id('rawdata-tab')
			search_button.click()
			search_return = br.find_element_by_class_name('data').text
			self.data = json.loads(search_return)

			self.LMovieTitle.setText("<b>Release Date: </b>" + self.data.get("Title"))
			self.LMovieRelease.setText("<b>Release Date: </b>" + self.data.get("Released"))
			self.LMovieAge.setText("<b>Release Date: </b>" + self.data.get("Released"))
			self.LMovieRunTime.setText("<b>Runtime: </b>" + self.data.get("Runtime"))
			self.LMovieGenre.setText("<b>Genre: </b>" + self.data.get("Genre"))
			self.LMovieDirector.setText("<b>Director(s): </b>" + self.data.get("Director"))
			self.LMovieWriter.setText("<b>Writer(s): </b>" + self.data.get("Writer"))
			self.LMovieimdbRating.setText("<b>IMDB Rating: </b>" + self.data.get("imdbRating"))
			self.LMovieProduction.setText("<b>Production Company: </b>" + self.data.get("Production"))

			time.sleep(3)
			#subprocess.call(['osascript', '-e', 'tell application "Firefox" to quit'])
			os.system("TASKKILL /F /IM firefox.exe")

if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	main_window = Window()
	main_window.show()
	sys.exit(app.exec_())

