br.implicitly_wait(15) 
br.get('http://www.omdbapi.com/?t=' + text + '&apikey=53d59f58')

search_button = br.find_element_by_id('rawdata-tab')
search_button.click()
search_return = br.find_element_by_class_name('data').text
self.data = json.loads(search_return)

self.LMovieTitle.setText("<b>Movie Title: </b>" + self.data.get("Title"))
self.LMovieRelease.setText("<b>Release Date: </b>" + self.data.get("Released"))
self.LMovieAge.setText("<b>Age Rating: </b>" + self.data.get("Released"))
self.LMovieRunTime.setText("<b>Runtime: </b>" + self.data.get("Runtime"))
self.LMovieGenre.setText("<b>Genre: </b>" + self.data.get("Genre"))
self.LMovieDirector.setText("<b>Director(s): </b>" + self.data.get("Director"))
self.LMovieWriter.setText("<b>Writer(s): </b>" + self.data.get("Writer"))
self.LMovieimdbRating.setText("<b>IMDB Rating: </b>" + self.data.get("imdbRating"))
self.LMovieProduction.setText("<b>Production Company: </b>" + self.data.get("Production"))