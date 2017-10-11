# SplitData
Scripts used to split the data from its root file into numpy arrays

This is where the differences between the fully supervised and weakly supervised classifiers appear. 
The data for the weakly supervised case are made into bags with fractional knowledge of the class labels.

For the Fully supervised case:

use the SplitDataTest2.py scripts to interface with SaverTest2.py. 
The business logic is contained in SaverTest2.py, where SplitDataTest2.py only handles user inputs. 

For the Weakly supervised case:

Similar to the Fully supervised case.

use SplitDataWeakV4.py to interface with the business logic contain in SaverWeakV4.py.


This has been tested to work with ROOT version 6 and its root_numpy/ pyROOT packages. 


