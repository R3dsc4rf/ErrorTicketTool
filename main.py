# !/usr/bin/env python3
# for linux. exestiert -> program can be executed by terminal without "Python 3" in command
# does not exist for windows

'''
    Main.py for Error TicketTool_v001
    
    this tool aims to help Quality tester to create tickets and show some simple diagramm with often to use data
    however, the tool is right now limited to the example data in TicketData.csv adding / deleting columns may cause error
    this tool also does not repair corrupted data
    this tool does not limit inputs. Status = "NEW" "new" or "new Error" are all counted as seperate enteties
    this tool alwas loads data from TicketData.csv first
    
    the main screen shows you different buttons as funktions:
    add ticket
        opens new window
        shows a mask with text inputs to fill. this way you can create a new ticket
    
    show diagram
        opens new window
        shows basic diagramm of loaded data
    
    quit
        exit the programm and all including windows
        
    #todo
    features for the future:
    - change autoloaded csv data file
    - check colum title first and adjust add ticket inputs
    - change id as index -> catch id errors
    - diagram changable with text button
    - other ideas
    - Rename funktions / Variables correctly (upper / lowercase / camel / etc.)
    - if i think about extra windows. i could make every feature in a tab. but time is running out
'''

import TicketCreator as TC
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
        self.cwd = os.getcwd()  # cwd = current working directory
        self.master.title("ErrorTicketTool v001")
        self.create_Widgets()
        self.pack(expand=True, fill="both")

    def create_Widgets(self):
        '''create Widgets - Only buttons that open the Features'''
        self.mainFrame = tk.Frame(self, borderwidth=10)  # , bg="black")  # step 1 - everything is in mainframe

        self.lTitle = tk.Label(self.mainFrame, text=f" Error TIcket Tool v002 ", padx=50, font=("Arial", 18))
        self.lTitle.grid(row=0, column=0)

        tabControl = ttk.Notebook(self.mainFrame)

        self.tab1 = ttk.Frame(tabControl)
        self.tab2 = ttk.Frame(tabControl)

        tabControl.add(self.tab1, text="Ticket Creator")
        tabControl.add(self.tab2, text="Diagram")
        tabControl.grid(column=0, row=1)

        self.ticketTab = TC.ticket_creator_window(master=self.tab1)
        self.diagramTab = DC.diagram_window(master=self.tab2)

        self.quitButton = tk.Button(self.mainFrame, text="quit", command=self.quit, padx=20, pady=2)
        self.quitButton.grid(column=0, row=10, sticky=tk.E)

        self.mainFrame.pack(expand=True, fill="both", anchor="e")


###########################################################################
################################### Main ##################################
###########################################################################

if __name__ == '__main__':
    mainWindow = main_window()
    mainWindow.mainloop()
else:
    print("Main of Error Ticket Tool entered")
