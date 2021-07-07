"""
Created on Thu Nov 28 2019

@author: Zaahier Adams
"""

from bs4 import BeautifulSoup
import csv
from matplotlib import pyplot as plt

class Fund():
    
    start, end = 0, 0
    cash_period, cash_values = [], []
    fund_found, checked, checked_2 = False, False, False
    
    # Webpage in same directory as .py file
    # Webpage needs to be manually updated 
    # http://www.fundsdata.co.za/navs/ZEGN.htm
    with open(r'Funds.html') as html_file:
            soup = BeautifulSoup(html_file,'lxml')
    
    
    def __init__(self, fund_name):
        self.fund_name = fund_name
        
    
    # Print message for fund found/ not found
    @classmethod
    def DNE(cls,fund_name):
        if Fund.fund_found is False:
            if cls.checked_2 is False:
                print('[{}] Fund does NOT exist!'.format(fund_name))
                cls.checked_2 = True
            else:
                pass
        else:
            #print('[{}] Fund Exists'.format(fund_name))
            pass
    
    
    # Ensures that there is a search for the Fund info. 
    def Double_Check(fund_name):
        if Fund.checked is False:
            Fund.Check(fund_name)
        else:
            pass


    # Checks if fund exists 
    @classmethod
    def Check(cls,fund_name):
        strt = 0

        for search_1 in Fund.soup.find_all('tr'):    
            for search_2 in search_1.find_all('td'):
                
                if cls.fund_found is False:
                    if fund_name in search_2.text:
                        cls.fund_found = True
                    else:
                        strt+=1
                        pass
                  
                    if cls.fund_found is True:
                        strt+=1
                    else:
                        pass
                else:
                    pass

        if cls.fund_found is True:
            cls.start = strt-7
            cls.end = strt+13
            cls.cash_period.extend([strt+4, strt+6, strt+8, strt+10])
            cls.checked = True
            return Fund.DNE(fund_name)
        else:
            cls.checked = True
            return Fund.DNE(fund_name)
        
    
    # Finds all info for specific fund
    # Unlike Extract_All(), only finds info pertaining to queried fund 
    def Information(self, fund_name):
        self.columns, self.results = [], []
        count, col_cnt = 0, 0
        string_columns = ''
        string_results = ''
        
        Fund.Double_Check(fund_name)

        if Fund.fund_found is False:
            return Fund.DNE(fund_name)
        else:
            
            csv_file = open('Fund_Results.csv','w')
            csv_writer = csv.writer(csv_file, lineterminator = '\n')
                        
            
            for search_1 in Fund.soup.find_all('tr'): 
                for search_2 in search_1.find_all('td'):
             
                    # Populate columns list
                    if count> 1 and count < 21:
                        self.columns.append(search_2.text)
                    else:
                        pass
                    
                    if count > Fund.start and count < Fund.end:
                        #print('{} :\t{}'.format(self.columns[col_cnt],search_2.text))
                        self.results.append(search_2.text)
                
                        col_cnt+=1
                        if col_cnt == len(self.columns):
                            col_cnt=0
                        else:
                            pass
                    else:
                        pass
                        
                    count+=1
            
            for i1 in self.columns:
                string_columns += (i1+';')
            for i2 in self.results:
                string_results += (i2+';')
            
            csv_writer.writerow([string_columns])
            csv_writer.writerow([string_results])
            
            csv_file.close()
    
    
    # Extracts all webpage data into a csv file
    def Extract_All():
        columns_2, results_2 = [], []
        count_2, col_cnt_2 = 0, 0
        string_columns_2 = ''
        string_results_2 = ''
        col_write = False
        dd_check = False
        data_date = ''
        
        # csv file with info of all funds
        csv_file_2 = open('All_Fund_Info.csv','w')
        csv_writer_2 = csv.writer(csv_file_2, lineterminator = '\n')
        
        for search_1 in Fund.soup.find_all('tr'):
            for search_2 in search_1.find_all('td'):
                       
                # populate columns list
                if count_2 > 1 and count_2 < 21:
                    columns_2.append(search_2.text)
                else:
                    pass
                    
                if count_2 > 20:
                    # write column headings
                    if col_write is False:
                        for i3 in columns_2:
                            string_columns_2 += (i3+';')
                        csv_writer_2.writerow([string_columns_2])
                        col_write = True
                    else:
                        pass
                    
                    
                    # get date of data
                    # Only gets date of first entry
                    # Not nec. representative of the rest of data
                    if count_2 == 22:
                        if dd_check is False:
                            data_date = search_2.text
                            dd_check = True
                        else:
                            pass
                    else:
                        pass
                            
                            
                    # fill in columns for funds
                    results_2.append(search_2.text)
                    col_cnt_2+=1
                    if col_cnt_2 == len(columns_2):
                        col_cnt_2=0
                        
                        for i2 in results_2:
                            string_results_2 += (i2+';')
                        csv_writer_2.writerow([string_results_2])
                        
                        # reset results string and list:
                        string_results_2 =''
                        results_2 = []
                    else:
                        pass
                else:
                    pass
                count_2+=1   
        csv_file_2.close()
        print('> All data extracted to:\tAll_Fund_Info.csv')
        return data_date

    
    # Finds Cash Values for Fund
    @classmethod
    def C_Values(cls,fund_name):
        count = 0
        
        Fund.Double_Check(fund_name)
        
        for search_1 in Fund.soup.find_all('td'):
            if count in Fund.cash_period:
                try:
                    cls.cash_values.append(float(search_1.text))
                except:
                    #cls.cash_values.append(0)
                    pass
            else:
                pass
            count+=1
    
    
    # Prints out Cash Value Graphic      
    def Fund_Graphic(fund_name):
        
        period_names = ['6 Months','1 Year','3 Years','5 Years']

        Fund.C_Values(fund_name)
        
        if Fund.fund_found is True:
            
            # If < 4 periods provided:
            leng = len(Fund.cash_values)
            if leng != 4 :
               del period_names[leng:4]
            else:
                pass
            
            # Matplotlib:
            plt.rcdefaults()
            plt.style.use('ggplot')
            plt.plot(period_names, Fund.cash_values, '-o', color='black', linewidth =2,)
            plt.bar(period_names, Fund.cash_values, color='#e36049')
            plt.grid(True)
            plt.xlabel('Period')
            plt.ylabel('Cash Value (Rands?)')
            plt.title('Cash values for {} Fund'.format(fund_name))
            plt.savefig('{}.jpg'.format(fund_name))
            plt.show()
        else:
            pass
            

#print(help(Fund))
            
#f2_name = 'koeksister'        
#f_name = 'Old Mutual Investors - A'
#
#fund_1 = Fund(f_name)
#
#fund_1.Information(f_name)
#Fund.Fund_Graphic(f_name)

