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
		#Sets the window title, where the window starts on the screen and the size of the window
		self.setWindowTitle("Movie database Search Tool")
		self.setGeometry(100, 130, 1200, 600)

		#Used to define all of the text that is displayed on the screen
		self.LTitle = QtWidgets.QLabel("Group B2 Movie Search Tool")
		self.LMovieTitle = QtWidgets.QLabel("<b>Movie Title:</b> ")
		self.LMovieRelease = QtWidgets.QLabel("<b>Release Date: </b>")
		self.LMovieAge = QtWidgets.QLabel("<b>Age Rating: </b>")
		self.LMovieRunTime = QtWidgets.QLabel("<b>Runtime: </b>")
		self.LMovieGenre = QtWidgets.QLabel("<b>Genre: </b>")
		self.LMovieDirector = QtWidgets.QLabel("<b>Director(s): </b>")
		self.LMovieWriter = QtWidgets.QLabel("<b>Writer(s): </b>")
		self.LMovieimdbRating = QtWidgets.QLabel("<b>IMDB Rating: </b>")
		self.LMovieProduction = QtWidgets.QLabel("<b>Production Company: </b>")
		LWishlistTitle = QtWidgets.QLabel("<b>Wishlist</b>")

		#This is used to define the wish list (Selection box on right hand side of the screen)
		self.listWidget = QtWidgets.QListWidget()
		
		#Used to load the image in
		image = QtWidgets.QLabel(self)
		pixmap = QtGui.QPixmap('UOL_logo.png')
		image.setPixmap(pixmap)

		#Defines all of the buttons and what they say on them
		SearchButton = QtWidgets.QPushButton("Click to search for a movie")

		AddButton = QtWidgets.QPushButton("Add")
		RemoveButtom = QtWidgets.QPushButton("Remove")
		ViewButton = QtWidgets.QPushButton("View")
		CommentsButton = QtWidgets.QPushButton("Comments")

		#Used to say what happens when one the buttons is pressed
		SearchButton.clicked.connect(self.search_btn_click)

		AddButton.clicked.connect(self.add_btn_click)
		RemoveButtom.clicked.connect(self.remove_btn_click)
		ViewButton.clicked.connect(self.view_btn_click)

		#Used to define the layout type as a grid layout
		grid = QtWidgets.QGridLayout()
		grid.setSpacing(10)

		#Used to display all of the widgets. First value is the row, second value is the column, third is the number of rows that the widget spans across, fourth is the number of columns that the widget spans across
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

		#So the text doesn't go off the screen
		self.LMovieTitle.setWordWrap(True)
		self.LMovieRelease.setWordWrap(True)
		self.LMovieAge.setWordWrap(True)
		self.LMovieRunTime.setWordWrap(True)
		self.LMovieGenre.setWordWrap(True)
		self.LMovieDirector.setWordWrap(True)
		self.LMovieWriter.setWordWrap(True)
		self.LMovieimdbRating.setWordWrap(True)
		self.LMovieProduction.setWordWrap(True)

		#Makes some of the text bold and a bigger size
		self.myFont = QtGui.QFont()
		self.myFont.setBold(True)
		self.myFont.setPointSize(20)

		self.LTitle.setFont(self.myFont)

		#Places the uni of lincoln logo on the far right of the screen
		image.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

		#Defines where the buttons are placed. See above for value meanings
		grid.addWidget(SearchButton, 2, 0, 1, 4)
		grid.addWidget(CommentsButton, 11, 0, 1, 1)
		grid.addWidget(AddButton, 11, 1, 1, 1)
		grid.addWidget(RemoveButtom, 11, 2, 1, 1)
		grid.addWidget(ViewButton, 11, 3, 1, 1)

		#Uses grid layou
		self.setLayout(grid) 

		#Loads an array from a text file and puts it into a variable. This array then pooulates the wish list selection box (right hand side of the screen)
		with open('wishlist.txt', 'rb') as f:
			self.wishlistArray = pickle.load(f)
		for x in self.wishlistArray:
			self.listWidget.addItem(x)

	#When the search button is clicked this function will run
	def search_btn_click(self):
		#Used for the pop up that will ask for an input for the movie title and will take a boolean saying if the ok button was pressed and the value of the text
		text, okPressed = QtWidgets.QInputDialog.getText(self, "Movie Search","Movie Title:", QtWidgets.QLineEdit.Normal, "")
		if okPressed and text != '':
			#Clears the data dictionary
			self.data = {"Title":"","Year":"","Rated":"","Released":"","Runtime":"","Genre":"","Director":"","Writer":"","Actors":"","Plot":"","Language":"","Country":"","Awards":"","Poster":"","Ratings":[{"Source":"","Value":""},{"Source":"","Value":""},{"Source":"","Value":""}],"Metascore":"","imdbRating":"","imdbVotes":"","imdbID":"","Type":"","DVD":"","BoxOffice":"","Production":"","Website":"","Response":""}

			#Used to determine which OS you are using and load the right web driver file
			if _platform == "darwin":
			   br = webdriver.Firefox(executable_path="Firefox Webdrivers/geckodriver")
			elif _platform == "win32":
			   br = webdriver.Firefox(executable_path="Firefox Webdrivers/geckodriver32.exe")
			elif _platform == "win64":
				br = webdriver.Firefox(executable_path="Firefox Webdrivers/geckodriver64.exe")

			#Website to use the API
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
 			self.LMovieTitle.setText("<b>Movie Title: </b>" + self.data.get("title"))
			self.LMovieRelease.setText("<b>Release Date: </b>" + self.data.get("release_date"))			
			self.LMovieRunTime.setText("<b>Runtime: </b>" + str(self.data.get("runtime")))
			#self.LMovieGenre.setText("<b>Genre: </b>" + self.data.get("Genre"))			
			#self.LMovieProduction.setText("<b>Production Company: </b>" + self.data.get("name"))
				
			time.sleep(3)
			subprocess.call(['osascript', '-e', 'tell application "Firefox" to quit'])
			#subprocess.call(['osascript', '-e', 'tell application "Firefox" to quit'])
			os.system("TASKKILL /F /IM firefox.exe")

	#Adds the current movie searched to the selection box
	def add_btn_click(self):
		#Checks if it already exists
		if self.data.get("Title") not in self.wishlistArray:

			#Add the item to the array and then selection box
			self.wishlistArray.append(self.data.get("Title"))
			self.listWidget.addItem(self.data.get("Title"))

			#Saves the updates array to a file
			with open("wishlist.txt", 'wb') as f:
				pickle.dump(self.wishlistArray, f)
	
	#Removes the selected item from the selection box
	def remove_btn_click(self):
		#Removes the selected item from the array box
		self.wishlistArray.remove(self.listWidget.currentItem().text())

		#Saves the updated array to a file
		with open("wishlist.txt", 'wb') as f:
				pickle.dump(self.wishlistArray, f)

		#Removes the selected item from the selection box
		item = self.listWidget.takeItem(self.listWidget.currentRow())
		item = None

	#View the infomation of the selected item in the selection box
	def view_btn_click(self):

			#Gets the text from the selection box
			text = self.listWidget.currentItem().text()

			self.data = {"Title":"","Year":"","Rated":"","Released":"","Runtime":"","Genre":"","Director":"","Writer":"","Actors":"","Plot":"","Language":"","Country":"","Awards":"","Poster":"","Ratings":[{"Source":"","Value":""},{"Source":"","Value":""},{"Source":"","Value":""}],"Metascore":"","imdbRating":"","imdbVotes":"","imdbID":"","Type":"","DVD":"","BoxOffice":"","Production":"","Website":"","Response":""}

			#Used to determine which OS you are using and load the right web driver file
			if _platform == "darwin":
			   br = webdriver.Firefox(executable_path="Firefox Webdrivers/geckodriver")
			elif _platform == "win32":
			   br = webdriver.Firefox(executable_path="Firefox Webdrivers/geckodriver32.exe")
			elif _platform == "win64":
				br = webdriver.Firefox(executable_path="Firefox Webdrivers/geckodriver64.exe")

			#Website to use the API
			br.implicitly_wait(15) 
			br.get('http://www.omdbapi.com/')

			#Returns the data into the data list
			search = br.find_element_by_name('t')
			search.send_keys(text)
			search_button = br.find_element_by_id('search-by-title-button')
			search_button.click()
			search_return = br.find_element_by_class_name('alert-success').text
			self.data = json.loads(search_return)

			#Displays the returned on the window
			self.LMovieTitle.setText("<b>Release Date: </b>" + self.data.get("Title"))
			self.LMovieRelease.setText("<b>Release Date: </b>" + self.data.get("Released"))
			self.LMovieAge.setText("<b>Release Date: </b>" + self.data.get("Released"))
			self.LMovieRunTime.setText("<b>Runtime: </b>" + self.data.get("Runtime"))
			self.LMovieGenre.setText("<b>Genre: </b>" + self.data.get("Genre"))
			self.LMovieDirector.setText("<b>Director(s): </b>" + self.data.get("Director"))
			self.LMovieWriter.setText("<b>Writer(s): </b>" + self.data.get("Writer"))
			self.LMovieimdbRating.setText("<b>IMDB Rating: </b>" + self.data.get("imdbRating"))
			self.LMovieProduction.setText("<b>Production Company: </b>" + self.data.get("Production"))

			#Closes firefox
			time.sleep(3)
			subprocess.call(['osascript', '-e', 'tell application "Firefox" to quit'])
			os.system("TASKKILL /F /IM firefox.exe")

if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	main_window = Window()
	main_window.show()
	sys.exit(app.exec_())