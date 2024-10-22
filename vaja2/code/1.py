import numpy as np
import matplotlib.pyplot as plt


wav = np.loadtxt('spektri/val.dat', comments='#')

spectra_array =[]

for spectrum in range(1, 5750):
    flux = np.loadtxt('spektri/%s.dat' % spectrum, comments='#')
    spectra_array.append(flux)

spectra_array = np.array(spectra_array)

plt.plot(wav, spectra_array[1234], 'k-')
plt.show()