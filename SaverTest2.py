
###################################################
#                                                 #
#   Master's Project Data Handling Script         #
#   Version 1                                     #
#   Sam Wright February 2017                      #
#                                                 #
###################################################
import root_numpy
import ROOT
import numpy as np
import math
import random

storage = "/mnt/storage/lborgna/"

def Saver(bkgfilename, sgfilename, B_events, S_events):

	sig = ROOT.TFile.Open(sgfilename)
	bkg = ROOT.TFile.Open(bkgfilename)

	Nbkg = len(bkg.GetListOfKeys())
	Nsig = len(sig.GetListOfKeys())

	bkgArray = []
	sigArray = []
	
	bkg_iteration = random.sample(xrange(0, Nbkg), B_events)
	sig_iteration = random.sample(xrange(0, Nsig), S_events)
	#print(bkg_iteration)

	countBKG = 0
	countSig = 0

	RangeSig = [0,Nsig, int(math.floor(Nsig/S_events))]

	for i in range(0, Nbkg, int(math.floor(Nbkg/B_events))):
  		histoname = "histo"+str(i)
  		aHisto = bkg.Get(histoname)
  		aHisto.Print() #This prevents all the array elements being 0.
		#print("BKG")
  		anArrayfromHisto = root_numpy.hist2array(aHisto)
 		anArrayfromHisto = np.rot90(anArrayfromHisto)
 		bkgArray.append(anArrayfromHisto)
		countBKG = countBKG + 1
		print(countBKG)


	for i in range(0, Nsig, int(math.floor(Nsig/S_events))):
  		histoname = "histo"+str(i)
  		aHisto = sig.Get(histoname)
  		aHisto.Print() #This prevents all the array elements being 0.
		#print("SIG")
  		anArrayfromHisto = root_numpy.hist2array(aHisto)
  		anArrayfromHisto = np.rot90(anArrayfromHisto)
  		if np.sum(anArrayfromHisto) != 0.0:
  			sigArray.append(anArrayfromHisto)
			countSig = countSig +1
			print(countSig)

  	bkgArray = np.array(bkgArray)
  	sigArray = np.array(sigArray)


	print(countBKG)
	print(countSig)

	return bkgArray, sigArray
