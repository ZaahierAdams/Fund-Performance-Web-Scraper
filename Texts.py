
def Description():
    Description ='''
This program has two main functions:

(1) 'Extract All Fund Data' extracts all data from webpage, and 
      stores it in: 
      All_Fund_Info.csv

(2) The user can search for the performance of a particular 
     fund using the search bar
    
    - This will produce a diagram for the queried fund's cash 
      values in the python console
   
    - Moreover, it saves all the queried fund's data to:
      Fund_Results.csv
  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Note:

(1) The data (webpage) needs to be manually updated, 
    the website used:
    http://www.fundsdata.co.za/navs/ZEGN.htm

(2) The directory for all files is the folder "Fund Check"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Possible Future Developements:

(1) Convenient method of selecting saved web page

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
    return Description


def Version():
    Version ="""
Version 1.00

Created on:\t29 November 2019
Lasted updated:\t29 November 2019 

Created by:\tZaahier Adams
"""
    return Version