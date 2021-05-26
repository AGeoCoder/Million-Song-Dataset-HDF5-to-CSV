import hdf5_getters
import numpy as np
f = 'MillionSongSubset/A/A/A/TRAAAAW128F429D538.h5'
songH5File = hdf5_getters.open_h5_file_read(f)
print(np.array(songH5File['analysis']))
print(np.array(songH5File['metadata']['songs']))
print(np.array(songH5File['musicbrainz']))