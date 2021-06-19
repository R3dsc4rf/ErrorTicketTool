Error Ticket Tool v001
======================

Error Ticket Tool is an Tool to help you adding Error Tickets into an
.csv. (You can use .csv as Excell Table.) Additionly it adds a small
Graph tool to show basic Information.

Instalation
-----------

You will need Python and have to install:

``` {.bash}
pip install tk
pip install daytime
pip install -U pip
pip install -U matplotlib
```

Additional: - Remember your download Folder for Python and Error Ticket
Tool - Start Error Ticket Tool in Error Ticket tool folder.

HOW TO START
------------

### Anaconda prompt

1.  Start anaconda promt
2.  type: python D:...\ErrorTicketTool\_v001\main.py for "..." enter
    your file location. e.g. your download folder

### CMD

1.  win + r
2.  type cmd and press ok
3.  navigate to ErrorTicketTool\_v001 Folder
4.  C:...\python D:...\ErrorTicketTool\_v001\main.py for "..." enter
    your file location. e.g. your download folder

### Important

The tool looks 1. in the activ folder to find TicketData.csv. If there
is no TicketData.csv will not open information in window.

if you Console gives you this error: FileNotFoundError: [Errno 2] No
such file or directory: 'TicketData.csv'

navigate to the same folder ...\TicketData.csv then start the program
again OR Create a TicketData.csv file in your current folder. this
problem will be adressed in "Future plans" section

Description
-----------

This program is build as a part of a python crash course. It includes a
Main window. Buttons on Main window will open a second window with
following features: - Ticket Creator (add Ticket): Window shows fix
Information with Text input to add a Ticket to your selected CSV datai.
- DiagramCreator (show Diagram): Show basic information about the loaded
window. To Update, you have to open your selected file again.

### What it cannot do

This tool does not repair corrupted data. It does not combine similar
data. a wrong date will be displayed wrong. error type "new" and "NEW"
will be 2 seperate types You cannot dat columns to example data right
now.

Support
-------

no Support guaranteed

License
-------

MIT

Future plans
------------

todo - add save last opend .csv to autoload after programm starts - Make
ui better -\> do not open new window, make windows in seperate tabs in
main - restrickt import to reduce corrupted data -\> e.g. date have to
be date, id have to be number only. - make ticket creator dynamic so you
can add column in csv
