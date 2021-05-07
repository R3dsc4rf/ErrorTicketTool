'''
    Open a Window with Data shown in Diagramm from "TicketData.csv"

    Diagrams:
    - Tickets Created in time
    - Status distribution in %
    - Prio distribution in %
    *note Time run you. you will see some handover variable not used in current version

    buttons:
    - quit -> close window
    - openFIle -> Select a new .csv to load data. Additional use this to update Window if datafile is changed
'''

##############################################################################
################################### Import ###################################
##############################################################################

import tkinter as tk
from tkinter import filedialog as fd  # for open file funktion
import datetime as dt
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


###########################################################################
####################  init Class/ Global Var/ Funktion ####################
###########################################################################

class diagram_window(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.master = master
        self.isTab = False
        try:
            self.master.title("Diagramm")
        except AttributeError:
            print("Note: Diagram Creator is opened in Tab")
            self.isTab = True

        self.dataname = "TicketData.csv"
        self.rowdict = {}  # Temp data to read data into myarrayDict

        self.rowdata = []  # my data rows are in here
        self.myarrayDict = []  # your data in dict is saved in here. use it for work

        self.now = dt.datetime.now()

        self.open_Data_File()
        self.data_to_dict_list()

        self.create_Widgets()
        print("ticket_creator_window - created")

    ################################### Widgets ##################################
    def create_Widgets(self):
        '''do this at beginning to Create Widgets. Top middle and bottom frames are generated and include label, button, etc'''
        self.mainFrame = tk.Frame(self.master)  # , bg="red")  # step 1 - everything is in mainframe

        self.top_widgets()
        self.mid_widgets()
        self.bottom_widgets()

        self.mainFrame.grid()

    def top_widgets(self):
        '''create top frame for Header data'''
        self.topFrame = tk.Frame(self.mainFrame)

        self.lTitle = tk.Label(self.topFrame, text=f" Diagram ", padx=100, font=("Arial", 18))
        self.lTitle.grid(row=0, column=0)
        self.lNote = tk.Label(self.topFrame, text="- Open File if you want to update Data")
        self.lNote.grid(row=1, column=0)
        self.lTitle = tk.Label(self.topFrame, text=dt.datetime.now().strftime("%d.%m.%Y"), padx=2, pady=2)
        self.lTitle.grid(row=0, column=1)

        self.topFrame.pack(padx=2, pady=2)

    def mid_widgets(self):
        '''Create middle frame for Diagramm / Fig'''
        self.midFrame = tk.Frame(self.mainFrame)

        self.create_Fig()

        self.midFrame.pack(padx=2, pady=2)

    def bottom_widgets(self):
        ''' create bottom frame for buttons to load new file / data / quit window'''
        self.bottomFrame = tk.Frame(self.mainFrame)  # , bg="green")

        self.lFileName = tk.Label(self.bottomFrame, text=f"...{self.dataname:<30}")
        self.lFileName.grid(row=0, column=1)
        self.openFIleButton = tk.Button(self.bottomFrame, text="openFIle", command=self.open_file)
        self.openFIleButton.grid(row=0, column=2, sticky=tk.SE, padx=2, pady=2, ipadx=10)
        if not self.isTab:
            self.quitButton = tk.Button(self.bottomFrame, text="Quit", command=self.master.destroy)
            self.quitButton.grid(row=0, column=5, sticky=tk.SE, padx=2, pady=2, ipadx=10)

        self.bottomFrame.pack(anchor="e")

    ################################### Diagrams / Fig ##################################
    def create_Fig(self, figsize=4, DONESTATUS="Done", PiechartBottomLeftColumnTitle="Prio"):
        '''creat figures from matlib plot -> start this in middle frame. Change size with figsize
        change bottom left fig with title of column in PiechartBottomLeftColumnTitle'''

        # Date fig
        self.fig = Figure(figsize=(figsize * 1.5, figsize), facecolor="white")
        self.fig.suptitle("Tickets Created in Time")

        counterdict = self.count_values_in_row()
        #print("counterdict", counterdict)
        self.axis = self.fig.add_subplot(111)

        self.axis.plot(sorted(counterdict.keys()), counterdict.values(), label="Date")
        # self.axis.plot(counterdict.keys(), counterdict.values(), label="Date")
        self.fig.autofmt_xdate(rotation=45)

        # Status Pie Chart
        self.fig2 = Figure(figsize=(figsize, figsize), facecolor="white")
        self.fig2.suptitle("Status distribution in %")
        statusDict = self.count_values_in_row("Status")
        explode = []
        for k in statusDict.keys():
            if k == DONESTATUS:
                explode.append(0.2)  # make Done tickets a little split form the rest of the pie chart
            else:
                explode.append(0)
        self.axis2 = self.fig2.add_subplot(111).pie(statusDict.values(), labels=statusDict.keys(), explode=explode,
                                                    autopct='%1.1f%%', startangle=90)

        # Prio Pie Chart or bonus chart
        self.fig3 = Figure(figsize=(figsize, figsize), facecolor="white")
        self.fig3.suptitle(" " + str(PiechartBottomLeftColumnTitle) + " distribution in %")
        PrioDict = self.count_values_in_row(PiechartBottomLeftColumnTitle)
        self.axis3 = self.fig3.add_subplot(111).pie(PrioDict.values(), labels=PrioDict.keys(), autopct='%1.1f%%')

        # draw section
        canvas = FigureCanvasTkAgg(self.fig, master=self.midFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=0, padx=2, pady=2)
        canvas2 = FigureCanvasTkAgg(self.fig2, master=self.midFrame)
        canvas2.draw()
        canvas2.get_tk_widget().grid(column=1, row=0, padx=2, pady=2)
        canvas3 = FigureCanvasTkAgg(self.fig3, master=self.midFrame)
        canvas3.draw()
        canvas3.get_tk_widget().grid(column=0, row=1, padx=2, pady=2)

    def count_values_in_row(self, columnTitle="Date"):
        '''for fig generation. looks at csv table and returns a dictionary with key = name of  value and value = number of same values.
        e.g. count how many tickets in table have the same date. key = date -> value = how many tickets are created on this date'''
        mycounter = {}
        for row in self.myarrayDict:
            if row[columnTitle] in mycounter:
                mycounter[row[columnTitle]] += 1
            else:
                mycounter[str(row[columnTitle])] = 1
        return mycounter

    ################################### Open Data / Update ##################################
    def open_Data_File(self):
        '''open file and save it into mydata. do this at the beginning or after dataname is changed'''
        with open(self.dataname) as data:
            mydata = csv.reader(data)
            for row in mydata:
                self.rowdata.append(row)

    def data_to_dict_list(self):
        '''Saves Data into dict list. use it in ini or if you open new file'''
        self.rowtitel = self.rowdata.pop(0)  # 0 because index may be wrong from open data file
        # print("rot tittel: ", self.rowtitel)
        for row in self.rowdata:
            # print(row, type(row))
            if not row:  # Ignore empty row
                pass
            else:
                for title in range(0, self.rowtitel.__len__()):
                    self.rowdict[self.rowtitel[title]] = row[title]
                    # print(row[title])
                # print(self.rowdict)
                self.myarrayDict.append(self.rowdict.copy())  # need copy of it will only save the reverence

        # print("my array dict: ", self.myarrayDict, type(self.myarrayDict))
        # for i in self.myarrayDict:
        #    print("My array dict I: ", i, type(i))

    def update_data_file(self):
        '''you opened a new data file - Update ID and other'''
        self.lFileName["text"] = f"...{self.dataname[-30:len(self.dataname)]}"

        self.rowdata.clear()
        self.myarrayDict.clear()

        self.open_Data_File()
        self.data_to_dict_list()
        self.create_Fig()

        #print(self.myarrayDict)
        self.update()

    def open_file(self):
        '''open another csv file. activated by openFIleButton'''
        self.dataname = fd.askopenfilename(title="Select file", filetypes=(("CSV Files", "*.csv"),))
        print("Warning: " + self.dataname + " is changed!")
        self.open_Data_File()
        self.update_data_file()

    ################################### do i even use you? ##################################
    # todo do i even use you?
    def get_column(self, columnTitle="ID"):
        '''return column with name columnTitle from loadet data'''
        column = []
        for dict in self.myarrayDict:  # get column of columnTitle
            column.append(dict[columnTitle])
        return column

    # todo do i even use you?
    def remove_list_duplicates(self, list):
        '''remove duplicates from import list'''
        list = list(dict.fromkeys(list))  # Remove duplicates
        return list


###########################################################################
################################### Main ##################################
###########################################################################

if __name__ == "__main__":
    root = tk.Tk()
    ticketCreator = diagram_window(master=root)
    root.mainloop()
else:
    print("You entered: diagram_window.py")
