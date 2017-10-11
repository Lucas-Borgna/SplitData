#Test of the saver.py function to split background and signal file

import SaverTest2
import time
import numpy as np
#storage = "/mnt/storage/lborgna/" (this caused problems further downstream)

from timeit import default_timer as timer
start = timer()
storage_bkg = "/mnt/storage/lborgna/DijetPreP/"
storage_sig = "/mnt/storage/lborgna/WprimePreP/"
#bkgfilename = "Pre_Bkg_All.root"
#sgfilename  = "Pre_SignalAll.root"

bkgfilename = 'Pre_Bkg7_m600_Train_25p.root'
sgfilename = 'Pre_Sig7_m600_Train_25p.root'



bkg_file = storage_bkg+bkgfilename
sig_file = storage_sig+sgfilename


#bkgfilename = "JZ3W-1.root"
#sgfilename  = "m600_Test.root"

"""
maxSig = 500000
minSig = 0
maxBkg = 500000
minBkg = 0
"""

B_events = 50000
S_events = 50000

#Saver.Saver(bkgfilename, sgfilename, maxSig, minSig, maxBkg, minBkg)
#SaverTest2.Saver(bkg, sig, maxSig, minSig, maxBkg, minBkg)

bkgArray, sigArray = SaverTest2.Saver(bkg_file, sig_file, B_events, S_events)
end = timer()
print("seconds: ", end - start)
print('minutes: ', (end-start)/60.0)

store = "/mnt/storage/lborgna/FullSupervisedData/Test/"

np.save(store+"Bkg7_m600_Train_25p_N"+str(B_events), bkgArray)
np.save(store+"Sig7_m600_Train_25p_N"+str(S_events), sigArray)
