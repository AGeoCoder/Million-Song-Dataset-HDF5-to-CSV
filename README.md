# Million-Song-Dataset-HDF5-to-CSV, 

Million Song Dataset HDF5 to CSV Converter, 
Alexis Greenstreet

The code in "msdHDF5toCSV.py" is designed to convert the HDF5 files of the Million Song Dataset
to a CSV by extracting various song properties.

The script writes to a "SongCSV.csv" in the directory containing this script.

Please note that in the current form, this code only extracts the following
information from the HDF5 files:
AlbumID, AlbumName, ArtistID, ArtistLatitude, ArtistLocation,
ArtistLongitude, ArtistName, Danceability, Duration, KeySignature,
KeySignatureConfidence, SongID, Tempo, TimeSignature, TimeSignatureConfidence,
Title, and Year.

Additional Files:
The code requires the use "HDF5_getters.py", written by Thierry Bertin-Mahieux at Columbia University, copyright 2010. This file makes use of the python libraries numpy (Numerical Python) and tables (PyTables/Python Tables), which aid in dealing with a hierarchical format such as HDF5.

Python:
This code was tested with a Python interpreter with version 2.7.9.

Necessary Python Libraries:
The file "HDF5_getters.py" uses python libraries NumPy and PyTables.
You can get the python library NumPy (Numerical Python) here: "www.numpy.org" > "http://www.scipy.org/scipylib/download.html".
You can get python library tables (PyTables/Python Tables) here: "http://www.pytables.org/" > "http://www.pytables.org/downloads.html".

NumPy and PyTables Notes:
I had significant difficulties installing NumPy and PyTables, so I eventually decided to use the Python IDE Canopy by Enthought, which included NumPy and had the ability to download PyTables. Other IDEs such as Python(x,y) may also be helpful.
If you choose to not use an IDE, you may need a C and FORTRAN compiler to install NumPy and/or PyTables. If you are using Windows, you may be interested in the Minimalist GNU for Windows project: http://www.mingw.org/.

