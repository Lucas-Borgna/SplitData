#Test of the saver.py function to split background and signal file

from SaverWeakV4 import Saver
import numpy as np
storage = "/mnt/storage/lborgna/"

#bkgfilename = "BigBkg.root"
#sgfilename  = "BigSig.root"

#bkgfilename = "outputjetBackground.root"
#sigfilename = "outputWSignals.root"

storage_bkg = "/mnt/storage/lborgna/DijetPreP/"
storage_sig = "/mnt/storage/lborgna/WprimePreP/"

#bkgfilename = storage_bkg + "Pre_Bkg2_LowPt_Train_25p.root"
#sigfilename = storage_sig + "Pre_Sig2_LowPt_Train_25p.root"

bkgfilename = storage_bkg + 'Pre_Bkg_Train_m600_25p.root'
sigfilename = storage_sig + 'Pre_m600_Train_25p.root'

fmin = 0.2

fmax = 0.8

Nbags = 1

bag_size = 10000

#SaverWeak.Saver(bkgfilename, sigfilename, fmin, fmax, Nbags, Nmin, Nmax)
Bag_array, fractions = Saver(bkgfilename, sigfilename, fmin, fmax, Nbags, bag_size)

store = "/mnt/storage/lborgna/WeakSupervisionData/TestSetsLowPt/"
np.save(store + "Samplesm600"+"_" + str(fmin) + "-" + str(fmax) +"_N"+str(Nbags) + "_E" + str(bag_size), Bag_array)
np.save(store + "Fractionsm600"+"_" + str(fmin) + "-" + str(fmax) +"_N" + str(Nbags) + "_E" + str(bag_size), fractions)

