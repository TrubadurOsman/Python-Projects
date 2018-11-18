from numpy import double

from song import *


print("""***********************************



Operations;

1. Show the songs

2. Search for a song

3. Add a song

4. Delete a song 

5. Update a song

Press q to exit.
***********************************""")

library= Library()

while True:
    operation = input("Choose an operation:")

    if (operation == "q"):
        
        print("Closed")
        break
    elif (operation == "1"):
        library.info()

    elif (operation == "2"):
        name = input("Which book ? ")
        print("Searching for it...")


        library.finder(name)

    elif (operation == "3"):
        name = input("name:")
        artist = input("artist:")
        album = input("album:")
        production = input("production:")
        length = float(input("length"))

        new_song = Song(name,artist,album,production,length)

        

        library.insert_song(new_song)
        print("Song is added")


    elif (operation == "4"):
        name = input("which song to delete?")

        cevap = input("Y/N")
        if (cevap == "Y"):
            
            
            library.delete_song(name)
            print("song is deleted")


    elif (operation == "5"):
        name = input("Which song to Update ?")
        artist=input("Who is the artist ?")
        
        library.update_song(name,artist)
        

    else:
        print("wrong operation")
