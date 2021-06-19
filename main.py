# !/usr/bin/env python3
# for linux. exestiert -> program can be executed by terminal without "Python 3" in command
# does not exist for windows

'''
    Main.py for Error TicketTool_v001
    
    this tool aims to help Quality tester to create tickets and show some simple diagramm with often to use data
    this tool also does not repair corrupted data
    this tool does not limit inputs. Status = "NEW" "new" or "new Error" are all counted as seperate enteties
    this tool alwas loads data from TicketData.csv first
'''

import TicketCreator as TC
from tkinter import filedialog as fd  # for open file funktion
import DiagramCreator as DC
import tkinter as tk
from tkinter import ttk
import os


###########################################################################
####################  init Class/ Global Var/ Funktion ####################
###########################################################################

class main_window(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.dataname = "TicketData.csv"
        self.cwd = os.getcwd()  # cwd = current working directory
        self.master.title("ErrorTicketTool v001")
        self.create_Widgets()
        self.pack(expand=True, fill="both")

    def create_Widgets(self):
        '''create Widgets - Only buttons that open the Features'''
        self.mainFrame = tk.Frame(self, borderwidth=10)  # , bg="black")  # step 1 - everything is in mainframe

        self.lTitle = tk.Label(self.mainFrame, text=f" Error TIcket Tool v003 ", padx=25, font=("Arial", 12))
        self.lTitle.grid(row=0, column=0)

        #Tab Creator
        tabControl = ttk.Notebook(self.mainFrame)
        self.tab1 = ttk.Frame(tabControl)
        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="Ticket Creator")
        tabControl.add(self.tab2, text="Diagram")
        tabControl.grid(column=0, row=1)
        self.ticketTab = TC.ticket_creator_window(master=self.tab1)
        self.diagramTab = DC.diagram_window(master=self.tab2)

        self.bot_window()

        self.mainFrame.pack(expand=True, fill="both", anchor="e")

    def bot_window(self):
        self.botFrame = tk.Frame(self.mainFrame)

        self.lDataName = tk.Label(self.botFrame, text=f"{str(self.dataname):>35}")
        self.lDataName.grid(row=0, column=1, padx=2, pady=2, ipadx=10)

        self.openFIleButton = tk.Button(self.botFrame, text="openFIle", command=self.open_file)
        self.openFIleButton.grid(row=0, column=2, padx=2, pady=2, ipadx=10)

        self.quitButton = tk.Button(self.botFrame, text="quit", command=self.quit, padx=20, pady=2)
        self.quitButton.grid(column=3, row=0, sticky=tk.E)

        self.botFrame.grid(column=0, row=10, sticky=tk.SE)

    def open_file(self):
        '''open another csv file. activated by openFIleButton'''
        print("askopenfilename Started")
        # self.dataname = fd.askopenfilename(initialdir="/", title="Select file", filetypes=(("CSV Files", "*.csv")))
        self.dataname = fd.askopenfilename(title="Select file", filetypes=(("CSV Files", "*.csv"),))

        print("Warning: " + self.dataname + " is changed!")
        self.diagramTab.set_file(self.dataname)
        self.ticketTab.set_file(self.dataname)

        #self.open_Data_File()
        #self.update_data_file()


###########################################################################
################################### Main ##################################
###########################################################################

if __name__ == '__main__':
    mainWindow = main_window()
    mainWindow.mainloop()
else:
    print("Main of Error Ticket Tool entered")
