'''
Developed by: Zaahier Adams
https://github.com/ZaahierAdams
'''


from tkinter import *
import os
from tkinter import messagebox
from PIL import ImageTk, Image
from importlib import reload
import Fund 
import Texts

def Extract():
    print('='*50)
    data_date = Fund.Fund.Extract_All()
    print('\n> Data was obtained on:\t\t{}'.format(data_date))
    print('='*50)
    messagebox.showinfo('Extract','Extraction Successful!\n\nAll data extracted to\t=\tAll_Fund_Info.csv\nDate of data\t\t=\t'+data_date)


'For some reason it no Query() no longer works outside of main'
# def Query(): 
#     fund_name = entry_1.get()
#     print('\n(i) More information on this fund can be found in Fund_Results.csv\n')
#     Fund.Fund(fund_name).Information(fund_name)
#     Fund.Fund.Fund_Graphic(fund_name)
#     reload(Fund)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def About():
    messagebox.showinfo('About',Texts.Description())
def Version():
    messagebox.showinfo('About',Texts.Version())

def main():
    
    def Query(): 
        fund_name = entry_1.get()
        print('\n(i) More information on this fund can be found in Fund_Results.csv\n')
        Fund.Fund(fund_name).Information(fund_name)
        Fund.Fund.Fund_Graphic(fund_name)
        reload(Fund)
        
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~      GUI     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Master Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       
    root = Tk()
    root.title('Fund Query')
    root.configure(background="white")
    root.resizable(False, False)
    'Icon from dribble.com'
    root.iconbitmap(resource_path("wallet.ico"))
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Dropdown Menu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    menu = Menu(root)
    root.config(menu=menu)
    dd_Help = Menu(menu)
    menu.add_cascade(label="Help",menu=dd_Help)
    dd_Help.add_command(label="About",command=About)
    dd_Help.add_command(label="Version",command=Version)
    
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Frame() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               
    Frame_1 = Frame(root, background='#FED97E' )
    Frame_2 = Frame(root, background='#03B079' )
    Frame_3 = Frame(root, background='#C39363' )
    Frame_4 = Frame(root, background='#C39363' )
    Frame_5 = Frame(root, background='#C39363' )
    Frame_6 = Frame(root)
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Label() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    image_location1 = resource_path("wallet.png")
    photo = ImageTk.PhotoImage(Image.open(image_location1))

    Label_1 = Label(Frame_1, width=300, height=225, bg='#FED97E', image=photo)
    Label_1.pack()
    
    Label_2 = Label(Frame_2,bg='#03B079',fg='#03B079')
    Label_2.grid(sticky=W)
    
    Label_3 = Label(Frame_3, width=50, height=1, bg='#C39363', fg ='black', text = 'Fund name:', font=("Helvetica", 12), anchor=N)
    Label_3.grid(row=0, column =0,  sticky=E)
    
    Label_4 = Label(Frame_4, bg='#C39363')
    Label_4.grid(row=0, column =0, sticky =E)
    
    Label_5 = Label(Frame_5, width=50,  bg='#C39363')
    Label_5.grid(row=0, column =0, sticky =E)
    
    Label_6 = Label(Frame_6,bd=1, relief=SUNKEN)
    Label_6.grid(row=0, column =0, sticky =E)
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Button() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    button_1 = Button(Label_2, text = "Extract all Fund data!", bg ='#03B079', fg='Black', command= Extract, font=("Helvetica", 12))
    button_1.bind("<Button-1>")
    button_1.grid(row=0, column =0, columnspan=2, sticky=N, padx =140, pady=20)
    
    button_2 = Button(Frame_4, text = "Search!", bg ='#C39363', fg='Black',command = Query)
    button_2.grid(row=2, column =0, sticky=W, padx =195, pady=0)
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Text Box ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    entry_1 = Entry(Frame_4)
    entry_1.grid(row=0, column =0,padx =50)
    
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  pack() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Frame_1.pack(fill=X)
    Frame_2.pack(fill=X)   
    Frame_3.pack(fill=X)    
    Frame_4.pack(fill=X)
    Frame_5.pack(fill=X)   
    Frame_6.pack(fill=X)   
    
                     
    root.mainloop()
    
if __name__ == '__main__':
    main()









