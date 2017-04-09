"""
Alexis Greenstreet (October 4, 2015) University of Wisconsin-Madison

This code is designed to convert the HDF5 files of the Million Song Dataset
to a CSV by extracting various song properties.

The script writes to a "SongCSV.csv" in the directory containing this script.

Please note that in the current form, this code only extracts the following
information from the HDF5 files:
AlbumID, AlbumName, ArtistID, ArtistLatitude, ArtistLocation,
ArtistLongitude, ArtistName, Danceability, Duration, KeySignature,
KeySignatureConfidence, SongID, Tempo, TimeSignature,
TimeSignatureConfidence, Title, and Year.

This file also requires the use of "hdf5_getters.py", written by
Thierry Bertin-Mahieux (2010) at Columbia University

Credit:
This HDF5 to CSV code makes use of the following example code provided
at the Million Song Dataset website 
(Home>Tutorial/Iterate Over All Songs, 
http://labrosa.ee.columbia.edu/millionsong/pages/iterate-over-all-songs),
Which gives users the following code to get all song titles:

import os
import glob
import hdf5_getters
def get_all_titles(basedir,ext='.h5') :
    titles = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            h5 = hdf5_getters.open_h5_file_read(f)
            titles.append( hdf5_getters.get_title(h5) )
            h5.close()
    return titles
    
ArtistName, Danceability, Duration, Energy, Key, Loudness, Hotness, Tempo, TimeSignature, Title, Year
"""

import sys
import os
import glob
import hdf5_getters
import re

class Song:
    songCount = 0

    def __init__(self, songID):
        self.id = songID
        Song.songCount += 1

        self.albumName = None
        self.albumID = None
        self.artistID = None
        self.artistLatitude = None
        self.artistLocation = None
        self.artistLongitude = None
        self.artistName = None
        self.danceability = None
        self.duration = None
        self.energy = None
        self.keySignature = None
        self.keySignatureConfidence = None
        self.loudness = None
        self.lyrics = None
        self.hotness = None
        self.tempo = None
        self.timeSignature = None
        self.timeSignatureConfidence = None
        self.title = None
        self.year = None

    def displaySongCount(self):
        print "Total Song Count %i" % Song.songCount

    def displaySong(self):
        print "ID: %s" % self.id   


def main():
    outputFile1 = open('SongCSV.csv', 'w')
    csvRowString = ""

    #################################################
    #change the order of the csv file here
    #Default is to list all available attributes (in alphabetical order)
    csvRowString = ("SongID,AlbumID,AlbumName,ArtistID,ArtistLatitude,ArtistLocation,"+
        "ArtistLongitude,ArtistName,Danceability,Duration,Energy,KeySignature,"+
        "KeySignatureConfidence,Loudness,Hotness,Tempo,TimeSignature,TimeSignatureConfidence,"+
        "Title,Year")
    #################################################

    csvAttributeList = re.split('\W+', csvRowString)
    for i, v in enumerate(csvAttributeList):
        csvAttributeList[i] = csvAttributeList[i].lower()
    outputFile1.write("SongNumber,");
    outputFile1.write(csvRowString + "\n");
    csvRowString = ""  

    #################################################


    #Set the basedir here, the root directory from which the search
    #for files stored in a (hierarchical data structure) will originate
    basedir = "../MillionSongSubset/data/" # "." As the default means the current directory
    ext = ".h5" #Set the extension here. H5 is the extension for HDF5 files.
    #################################################

    #FOR LOOP
    for root, dirs, files in os.walk(basedir):        
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            print f

            songH5File = hdf5_getters.open_h5_file_read(f)
            #print ("Number of songs in file: " + str(hdf5_getters.get_num_songs(songH5File)))
            for i in range(hdf5_getters.get_num_songs(songH5File)):
                song = Song(str(hdf5_getters.get_song_id(songH5File, i)))
                
                song.artistID = str(hdf5_getters.get_artist_id(songH5File, i))
                song.albumID = str(hdf5_getters.get_release_7digitalid(songH5File, i))
                song.albumName = str(hdf5_getters.get_release(songH5File, i))
                song.artistLatitude = str(hdf5_getters.get_artist_latitude(songH5File, i))
                song.artistLocation = str(hdf5_getters.get_artist_location(songH5File, i))
                song.artistLongitude = str(hdf5_getters.get_artist_longitude(songH5File, i))
                song.artistName = str(hdf5_getters.get_artist_name(songH5File, i))
                song.danceability = str(hdf5_getters.get_danceability(songH5File, i))
                song.duration = str(hdf5_getters.get_duration(songH5File, i))
                song.energy = str(hdf5_getters.get_energy(songH5File, i))
                song.keySignature = str(hdf5_getters.get_key(songH5File, i))
                song.keySignatureConfidence = str(hdf5_getters.get_key_confidence(songH5File, i))
                song.loudness = str(hdf5_getters.get_loudness(songH5File, i))
                song.hotness = str(hdf5_getters.get_song_hotttnesss(songH5File, i))
                song.tempo = str(hdf5_getters.get_tempo(songH5File, i))
                song.timeSignature = str(hdf5_getters.get_time_signature(songH5File, i))
                song.timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(songH5File, i))
                song.title = str(hdf5_getters.get_title(songH5File, i))
                song.year = str(hdf5_getters.get_year(songH5File, i))
                
                print ("Song number: " + str(song.songCount))
                csvRowString += str(song.songCount) + ","
                
                for attribute in csvAttributeList:
                    if attribute == 'AlbumID'.lower():
                        csvRowString += song.albumID
                    elif attribute == 'AlbumName'.lower():
                        albumName = song.albumName
                        albumName = albumName.replace(',',"")
                        csvRowString += "\"" + albumName + "\""
                    elif attribute == 'ArtistID'.lower():
                        csvRowString += "\"" + song.artistID + "\""
                    elif attribute == 'ArtistLatitude'.lower():
                        latitude = song.artistLatitude
                        if latitude == 'nan':
                            latitude = ''
                        csvRowString += latitude
                    elif attribute == 'ArtistLocation'.lower():
                        location = song.artistLocation
                        location = location.replace(',','')
                        csvRowString += "\"" + location + "\""
                    elif attribute == 'ArtistLongitude'.lower():
                        longitude = song.artistLongitude
                        if longitude == 'nan':
                            longitude = ''
                        csvRowString += longitude                
                    elif attribute == 'ArtistName'.lower():
                        csvRowString += "\"" + song.artistName + "\""                
                    elif attribute == 'Danceability'.lower():
                        csvRowString += song.danceability
                    elif attribute == 'Duration'.lower():
                        csvRowString += song.duration
                    elif attribute == 'Energy'.lower():
                        csvRowString += song.energy
                    elif attribute == 'KeySignature'.lower():
                        csvRowString += song.keySignature
                    elif attribute == 'KeySignatureConfidence'.lower():
                        csvRowString += song.keySignatureConfidence
                    elif attribute == 'Loudness'.lower():
                        csvRowString += song.loudness
                    elif attribute == 'SongID'.lower():
                        csvRowString += "\"" + song.id + "\""
                    elif attribute == 'Hotness'.lower():
                        csvRowString += song.hotness
                    elif attribute == 'Tempo'.lower():
                        csvRowString += song.tempo
                    elif attribute == 'TimeSignature'.lower():
                        csvRowString += song.timeSignature
                    elif attribute == 'TimeSignatureConfidence'.lower():
                        csvRowString += song.timeSignatureConfidence
                    elif attribute == 'Title'.lower():
                        csvRowString += "\"" + song.title + "\""
                    elif attribute == 'Year'.lower():
                        csvRowString += song.year
                    else:
                        csvRowString += "Erm. This didn't work. Error. :( :(\n"

                    csvRowString += ","

                #Remove the final comma from each row in the csv
                lastIndex = len(csvRowString)
                csvRowString = csvRowString[0:lastIndex-1]
                csvRowString += "\n"
                outputFile1.write(csvRowString)
                csvRowString = ""

            songH5File.close()

    outputFile1.close()
	
main()
