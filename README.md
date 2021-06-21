Error Ticket Tool v001
======================

Description
-----------

Error Ticket Tool is an Tool to help you adding Error Tickets into an
.csv. (You can use .csv as Excell Table.) Additionly it adds a small
Graph tool to show basic Information.

![grafik](https://user-images.githubusercontent.com/83809431/122727211-162e3400-d277-11eb-9a5f-de06774d64e6.png)

![grafik](https://user-images.githubusercontent.com/83809431/122727262-247c5000-d277-11eb-844d-86d90d5477fa.png)


**this tool cannot do:**

- this tool also does not repair corrupted data
- this tool does not limit inputs. Status = "NEW" "new" or "new Error" are all counted as seperate enteties
- this tool alwas loads data from TicketData.csv first
- this tool always work with .csv data with this heading:
    

![grafik](https://user-images.githubusercontent.com/83809431/122727997-f2b7b900-d277-11eb-983b-8593e25fb446.png)


I started this tool as port of an python crash cours and finished it privatly after i passed.
This tool i an excersize for me to learn python and github. I worked as a system tester and felt comfortable with the idea building a small ticket creator.
looking back to it i should have organized it a little better. especially in the diagramm creator part. However, as a first real python project i think i leared a lot of basics. Feel free to adjust the code as you want. Every feedback is welcome, too.

Instalation
-----------

Just download the files on https://github.com/R3dsc4rf/ErrorTicketTool/edit/main.
You will need Python and have to install:

``` {.bash}
pip install tk
pip install daytime
pip install -U pip
pip install -U matplotlib
```

HOW TO START
------------

### starting with console

#### Anaconda prompt

1.  Start anaconda promt
2.  type: python D:...\ErrorTicketTool\_v001\main.py for "..." enter
    your file location. e.g. your download folder

#### CMD

1.  win + r
2.  type cmd and press ok
3.  navigate to ErrorTicketTool\_v001 Folder
4.  C:...\python D:...\ErrorTicketTool\_v001\main.py for "..." enter
    your file location. e.g. your download folder

### Important

if you Console gives you this error:
```
FileNotFoundError: [Errno 2] No such file or directory: 'TicketData.csv'
```

The tool looks first in the activ folder *(your current location you are in while you execute)* to find TicketData.csv. If there
is no TicketData.csv, it will not open the window.

navigate to the same folder ...\TicketData.csv then start the program
again OR Create a TicketData.csv file in your current folder. this
problem will be adressed in "Future plans" section


Support
-------

no Support guaranteed

License
-------

MIT
