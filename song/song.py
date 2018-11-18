import sqlite3


class Song():
	def __init__(self,nam,artist,album,production,length):
		self.nam = nam
		self.artist = artist
		self.album = album
		self.production = production
		self.length = length
	def __str__(self):
			return "{} {} {} {} {}".format(self.nam,self.artist,self.album,self.production,self.length)

class Library():
	def __init__(self):
		self.connector()

	def connector(self):
		self.connection = sqlite3.connect("library.db")

		self.cursor = self.connection.cursor()

		cacher = "Create Table If not exists songs (nam TEXT,artist TEXT,album TEXT,production TEXT,lenght DOUBLE)"

		self.cursor.execute(cacher)

		self.connection.commit()

	def disconnect(self):
		self.connection.close()

	def info(self):
		cacher = "Select * From songs"

		self.cursor.execute(cacher)

		songs = self.cursor.fetchall()

		if (len(songs) == 0):
			print("There is no song...")
		else:
			for i in songs:
				song = Song(i[0], i[1], i[2], i[3], i[4])
				print(song)


	def finder(self,nam):

		cacher = "Select * From songs where nam  = ?"

		self.cursor.execute(cacher,(nam,))

		songs = self.cursor.fetchall()

		if (len(songs) == 0):
			print("There is no song ...")
		else:
			song = Song(songs[0][0],songs[0][1],songs[0][2],songs[0][3],songs[0][4])
			print(song)

	def insert_song(self,song):

		cacher = "Insert into songs Values(?,?,?,?,?)"

		self.cursor.execute(cacher,(song.nam,song.artist,song.album,song.production,song.length))

		self.connection.commit()

	def delete_song(self,nam):

		cacher = "Delete From songs where nam = ?"

		self.cursor.execute(cacher,(nam,))

		self.connection.commit()

	def update_song(self,nam,unkown):

		cacher = "Select * From songs where nam = ?"

		self.cursor.execute(cacher,(nam,))


		songs = self.cursor.fetchall()

		if (len(songs) == 0):
			print("there is no song ...")
		else:

			artist = unkown



			cacher3 ="Update songs  set artist = ? where nam = ?"


			self.cursor.execute(cacher3, (artist, nam))

			self.connection.commit()


