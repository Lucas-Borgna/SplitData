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
from random import shuffle
import pdb
import random

def Saver(bkgfilename, sgfilename, fmin, fmax, Nbags, bag_size):
    sig = ROOT.TFile.Open(sgfilename)
    bkg = ROOT.TFile.Open(bkgfilename)

    f_array = np.linspace(fmin, fmax, Nbags, endpoint=True)

    fractions = []
    MixArray = []

    Nbkg = len(bkg.GetListOfKeys())
    Nsig = len(sig.GetListOfKeys())

    US = random.sample(xrange(Nsig), bag_size * Nbags)

    UB = random.sample(xrange(Nbkg), bag_size * Nbags)
    countS = 0.0
    countB = 0.0
    count_total =0.0
    Sf = []
    Bf = []
    Bc = []
    Sc = []
    Ct = []
    for j in range(0, Nbags):
        countS = 0.0
        countB = 0.0
        count_total = 0.0

        print '-----------------------Bag#: ', j, '--------------------'
        for i in xrange(bag_size):

            if (i < (bag_size * f_array[j])):

                histoname = "histo" + str(US[i+ j * bag_size])
                aHisto = sig.Get(histoname)
                aHisto.Print()
                print("signal Bag: ", j)
                anArrayfromHisto = root_numpy.hist2array(aHisto)
                anArrayfromHisto = np.rot90(anArrayfromHisto)
                if np.sum(anArrayfromHisto) != 0.0:
                    MixArray.append(anArrayfromHisto)
                    fractions.append(f_array[j])
                    countS = countS + 1.0
                    count_total = count_total + 1.0

            else:
                histoname = "histo" + str(UB[i + j * bag_size])
                aHisto = bkg.Get(histoname)
                aHisto.Print()
                print("background Bag:", j)
                anArrayfromHisto = root_numpy.hist2array(aHisto)
                anArrayfromHisto = np.rot90(anArrayfromHisto)
                MixArray.append(anArrayfromHisto)
                fractions.append(f_array[j])
                countB = countB + 1.0
                count_total = count_total + 1.0
        Bc.append(countB)
        Sc.append(countS)
        Ct.append(count_total)
        Sf.append(countS/count_total)
        Bf.append(countB/count_total)

    print('Bc', Bc)
    print('Sc', Sc)
    print('Ct', Ct)
    print("Sf", Sf)
    print("Bf", Bf)



    Bag_array = []
    for x in range(0, Nbags):
        #print '-----------------------Bag#: ', j, '--------------------'
        bag = MixArray[x * bag_size:(x + 1) * bag_size]
        shuffle(bag)
        Bag_array.append(bag)

    Bag_array = np.array(Bag_array)
    fractions = np.array(fractions)
    fractions = np.reshape(fractions, (Nbags, -1))
    #print Bag_array.shape
    #print fractions



    return Bag_array, fractions


