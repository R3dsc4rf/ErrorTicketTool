'''
 Ticket Creator.py is used to add error tickes to an csv data.
 The class includes a csv reader, UI with TKinter and adds the current time to the ticket.
 there is only very minor error cathing. i may delete this in the future
 so do not use corrupted data or future primary key ticket id may be wrong
 ! warning. right now the tool will always load the file TicketData.csv first
 '''

##############################################################################
################################### Import ###################################
##############################################################################

import tkinter as tk
import csv
import datetime as dt
from tkinter import filedialog as fd  # for open file funktion

###########################################################################
####################  init Class/ Global Var/ Funktion ####################
###########################################################################

class ticket_creator_window(tk.Frame):
    '''This class adds user interfact to add Error tickets and saves it in dataname .csv file.
    - It offers a quit, add and change csv file button
    - it offerst text input for name, type, prio, date, status, occureance, description, error, expected. these input windows
        are fix. you have to change the code if you change your csv data, too
    - you cannot overwrite an open csv file. make sure you saved and closed your csv file bevor starting / adding code'''

    def __init__(self, master):
        tk.Frame.__init__(self)
        # super().__init__(*args, **kwargs)

        self.master = master

        self.isTab = False
        try:
            self.master.title("Error Ticket Adder")
            self.master.resizable(0, 0)
        except AttributeError:
            print("Note: Ticket Creator is opend with Tab")
            self.isTab = True


        self.dataname = "TicketData.csv"
        self.mydata = ""  # i am just a temp datafile because pointer problems
        self.myarraydata = []  # my data rows are in here
        self.newestID = 0

        self.now = dt.datetime.now()

        self.open_Data_File()
        self.create_Widgets()
        print("ticket_creator_window - created")
        # self.pack(expand=True, fill="both")

    ################################### Widgets ##################################
    def create_Widgets(self):
        '''do this at beginning to Create Widgets. Top middle and bottom frames are generated and include label, button, etc'''
        self.mainFrame = tk.Frame(self.master, borderwidth=10)  # , bg="red")  # step 1 - everything is in mainframe

        self.create_Top_Frame()
        self.create_middle_Frame()
        self.create_bottom_Frame()

        #self.mainFrame.pack(expand=True, fill="both")
        self.mainFrame.pack(fill="both")

    def create_Top_Frame(self):
        ''' Frame for Ticket description. if Entry is change jump in text_edited()'''
        self.topFrame = tk.LabelFrame(self.mainFrame, text="Ticket Data", borderwidth=2, pady=5)  # , bg='#ffdb99')

        self.lName = tk.Label(self.topFrame, text="Error Name")
        self.lName.grid(row=0, column=0, padx=10, pady=5)
        svName = tk.StringVar()
        # string var trace to check self.text_edited() every time a button is pressed
        # also possible with validate and validate command in tk.Entry
        svName.trace("w",
                     lambda name, index, mode, sv=svName: self.text_edited(svName))
        self.eName = tk.Entry(self.topFrame, textvariable=svName)
        self.eName.grid(row=0, column=1, padx=10, pady=5)

        self.lType = tk.Label(self.topFrame, text="Type")
        self.lType.grid(row=1, column=0, padx=10, pady=5)
        svType = tk.StringVar()
        svType.trace("w", lambda name, index, mode, sv=svType: self.text_edited(svType))
        self.eType = tk.Entry(self.topFrame, textvariable=svType)
        # self.eType = tk.Entry(self.topFrame, textvariable=svType, validate="key", validatecommand=self.text_edited())
        self.eType.grid(row=1, column=1, padx=10, pady=5)

        self.lPrio = tk.Label(self.topFrame, text="Prio")
        self.lPrio.grid(row=2, column=0, padx=10, pady=5)
        svPrio = tk.StringVar()
        svPrio.trace("w", lambda name, index, mode, sv=svPrio: self.text_edited(svPrio))
        self.ePrio = tk.Entry(self.topFrame, textvariable=svPrio)
        self.ePrio.grid(row=2, column=1, padx=10, pady=5)

        self.lOccurrence = tk.Label(self.topFrame, text="Occurrence")
        self.lOccurrence.grid(row=0, column=2, padx=10, pady=5)
        svOccurrence = tk.StringVar()
        svOccurrence.trace("w", lambda name, index, mode, sv=svOccurrence: self.text_edited(svOccurrence))
        self.eOccurrence = tk.Entry(self.topFrame, textvariable=svOccurrence)
        self.eOccurrence.grid(row=0, column=3, padx=10, pady=5)

        self.lStatus = tk.Label(self.topFrame, text="Status")
        self.lStatus.grid(row=1, column=2, padx=10, pady=5)
        svStatus = tk.StringVar()
        svStatus.trace("w", lambda name, index, mode, sv=svStatus: self.text_edited(svStatus))
        self.eStatus = tk.Entry(self.topFrame, textvariable=svStatus)
        self.eStatus.grid(row=1, column=3, padx=10, pady=5)
        self.eStatus.insert("0", "New")  # throws AttributeError because button = disabled -> pass

        self.lDate = tk.Label(self.topFrame, text="Date")
        self.lDate.grid(row=2, column=2, padx=10, pady=5)
        svDate = tk.StringVar()
        svDate.trace("w", lambda name, index, mode, sv=svDate: self.text_edited(svDate))
        self.eDate = tk.Entry(self.topFrame, textvariable=svDate)
        self.eDate.grid(row=2, column=3, padx=10, pady=5)
        self.eDate.insert("0",
                          str(self.now.strftime(
                              "%d.%m.%Y")))  # throws AttributeError because button = disabled -> pass

        self.topFrame.pack(expand=True, fill="both")

    def create_middle_Frame(self):
        '''Frame for Error Description'''
        self.midFrame = tk.LabelFrame(self.mainFrame, text="Ticket Description", borderwidth=2,
                                      pady=5)

        self.lDescription = tk.Label(self.midFrame, text="Description")
        self.lDescription.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.eDescription = tk.Text(self.midFrame, wrap="word", height=10)
        self.eDescription.insert("0.0", "Step1: Do something \nStep2: Do something \nStep3: Do something")
        self.eDescription.grid(row=1, column=0, padx=10, pady=5)

        self.lError = tk.Label(self.midFrame, text="Error")
        self.lError.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.eError = tk.Text(self.midFrame, wrap="word", height=3)
        self.eError.insert("0.0", "On Step2 there was an Error\nStuff happened")
        self.eError.grid(row=3, column=0, padx=10, pady=5)

        self.lExpected = tk.Label(self.midFrame, text="Expected")
        self.lExpected.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.eExpected = tk.Text(self.midFrame, wrap="word", height=3)
        self.eExpected.insert("0.0", "On Step2 there should be XXX")
        self.eExpected.grid(row=5, column=0, padx=10, pady=5)

        self.midFrame.pack(expand=True, fill="both")

    def create_bottom_Frame(self):
        '''Frame for Buttons'''
        self.botFrame = tk.Frame(self.mainFrame)

        if __name__ == "__main__":
            self.lDataName = tk.Label(self.botFrame, text=f"{str(self.dataname):>35}")
            self.lDataName.grid(row=0, column=1, padx=2, pady=2, ipadx=10)

        self.lTicketID = tk.Label(self.botFrame, text="Ticket Number: " + str(self.newestID + 1))
        self.lTicketID.grid(row=0, column=2, padx=2, pady=2, ipadx=10)

        if __name__ == "__main__":
            self.openFIleButton = tk.Button(self.botFrame, text="openFIle",
                                        command=self.open_FIle)
            self.openFIleButton.grid(row=0, column=3, sticky=tk.SE, padx=2, pady=2, ipadx=10)

        self.addTicketButton = tk.Button(self.botFrame, text="add Ticket",
                                         command=self.add_Ticket)
        self.addTicketButton["state"] = tk.DISABLED
        self.addTicketButton.grid(row=0, column=4, sticky=tk.SE, padx=2, pady=2, ipadx=10)

        if not self.isTab:
            self.quitButton = tk.Button(self.botFrame, text="Quit", command=self.master.destroy)
            self.quitButton.grid(row=0, column=5, sticky=tk.SE, padx=2, pady=2, ipadx=10)

        self.botFrame.pack(anchor="ne", expand=True)

    def text_edited(self, sv):
        ''' a text input widget is changed? check if it is empty? yes -> disable addButton'''
        print("text_edited - something changed")
        # print(sv.get())
        try:
            if self.eName.get() and self.eType.get() and self.ePrio.get() and self.eOccurrence.get() and self.eStatus.get() and self.eDate.get():
                self.addTicketButton["state"] = tk.ACTIVE
            else:
                self.addTicketButton["state"] = tk.DISABLED
        except AttributeError:
            print("Warning, Button input on disabled Button - You can ignore me!")

    ################################### Open Data / Update / add ticket ##################################
    def open_Data_File(self):
        '''open file and save it into mydata. do this at the beginning or after dataname is changed'''
        with open(self.dataname) as data:
            self.mydata = csv.reader(data)
            print("TicketCreator Data loaded: ", self.mydata, type(self.mydata))
            for row in self.mydata:
                # Warning! mydata pointer and data pointer is at last row after this
                # do not use mydata, instead use myarraydata for work
                self.myarraydata.append(row)
                '''self.newestID += 1
            self.newestID -= 1      #überschrift zeile wird mit übergeben'''

        # catch some errors, just to be save.
        # look what the last id in myarraydata list is and add 1 for next ticket. except id is no number. then use len for ID
        # this does not save you from errors if data is corupted
        try:
            self.newestID = int(
                str(self.myarraydata[len(self.myarraydata) - 1]).translate({ord(i): None for i in "[]'"}).split(",")[0])
        except:
            print("Data Error - ID no int - Quit - Please repair Data ID in DataFile:", self.dataname)
            self.newestID = len(self.myarraydata) - 1
        print(self.newestID)

    def update_data_file(self):
        '''you opened a new data file - Update ID and other'''

        self.lTicketID["text"] = "Ticket Number: " + str(self.newestID)

        if __name__ == "__main__":
            self.lDataName["text"] = f"...{self.dataname[-30:len(self.dataname)]}"

        self.update()

    def add_Ticket(self):
        '''append a new ticket on currently selected csv file. quit itself if done '''
        print("addTicket Started")
        newID = str(self.newestID + 1)
        newName = self.eName.get()
        newType = self.eType.get()
        newPrio = self.ePrio.get()
        newDate = self.eDate.get()
        newStatus = self.eStatus.get()
        newOccurrence = self.eOccurrence.get()
        newDescription = self.eDescription.get("1.0", tk.END)
        newError = self.eError.get("1.0", tk.END)
        newExpected = self.eExpected.get("1.0", tk.END)

        print(newID, newName, newType, newPrio, newDate, newStatus, newOccurrence)
        # print(newDescription, newError, newExpected)

        self.add_csv_row(
            newRow=[newID, newName, newType, newPrio, newDate, newStatus, newOccurrence, newDescription, newError,
                    newExpected])

    def add_csv_row(self, newRow):
        ''' activated by add_Ticket(). add a newRow to csv data. ONLY USE IF NEW ROW IS CORRECTLY FILLED WITH DATA.
            there is only manual deleting if data is added'''
        print(f"add {newRow} in {self.dataname}")
        # a+ Open for reading and appending (writing at end of file).
        with open(self.dataname, 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(newRow)
        self.master.destroy()

    def open_FIle(self):
        '''open another csv file. activated by openFIleButton'''
        print("askopenfilename Started")
        # self.dataname = fd.askopenfilename(initialdir="/", title="Select file", filetypes=(("CSV Files", "*.csv")))
        self.dataname = fd.askopenfilename(title="Select file", filetypes=(("CSV Files", "*.csv"),))
        print("Warning: " + self.dataname + " is changed!")
        self.open_Data_File()
        self.update_data_file()

    def set_file(self, fileName):
        self.dataname = fileName
        self.open_Data_File()
        self.update_data_file()



###########################################################################
################################### Main ##################################
###########################################################################

if __name__ == "__main__":
    print("test")
    root = tk.Tk()
    ticketCreator = ticket_creator_window(master=root)
    # ticketCreator.master.title("Error Ticket Adder")
    # ticketCreator.master.geometry("640x480")
    # ticketCreator.master.resizable(0, 0)
    root.mainloop()
else:
    print("You entered: TicketCreator.py")
