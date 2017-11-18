import xml.etree.ElementTree as ET


class Reader:
    def __init__(self, s):
        self.fileToRead5 = '/media/arek/N/PWR/VII/SI/crossword/2.xml'
        self.fileToRead6 = '/media/arek/N/PWR/VII/SI/crossword/6x6h.xml'
        self.fileToRead6e = '/media/arek/N/PWR/VII/SI/crossword/6x6e.xml'
        self.fileToRead7 = '/media/arek/N/PWR/VII/SI/crossword/7x7.xml'
        self.fileToRead8 = '/media/arek/N/PWR/VII/SI/crossword/8x8.xml'
        self.fileToRead9 = '/media/arek/N/PWR/VII/SI/crossword/9x9.xml'
        self.fileToRead10 = '/media/arek/N/PWR/VII/SI/crossword/10x10.xml'
        self.fileToRead12e = '/media/arek/N/PWR/VII/SI/crossword/12x12e.xml'
        self.fileToRead12h = '/media/arek/N/PWR/VII/SI/crossword/12x12h.xml'
        self.fileToRead15 = '/media/arek/N/PWR/VII/SI/crossword/15x15.xml'
        self.test = '/media/arek/N/PWR/VII/SI/crossword/test.xml'

        if s == 5:
            self.tree = ET.parse(self.fileToRead5)
        elif s == 6:
            self.tree = ET.parse(self.fileToRead6e)
        elif s == 7:
            self.tree = ET.parse(self.fileToRead7)
        elif s == 8:
            self.tree = ET.parse(self.fileToRead8)
        elif s == 9:
            self.tree = ET.parse(self.fileToRead9)
        elif s == 10:
            self.tree = ET.parse(self.fileToRead10)
        elif s == 12:
            self.tree = ET.parse(self.fileToRead12e)
        elif s == 15:
            self.tree = ET.parse(self.fileToRead15)
        elif s == 0:
            self.tree = ET.parse(self.test)

    def readFile(self):
        columns = []
        rows = []
        root = self.tree.getroot()
        size = 0
        for el in root:  # columns and rows
            # print("Element" + str(el.attrib))
            c = el.get('type')
            v = el.get('value')
            if str(c) == "column":
                columns.append([int(s) for s in v.split() if s.isdigit()])
            elif str(c) == "row":
                rows.append([int(s) for s in v.split() if s.isdigit()])
            elif str(c) == "size":
                size = int(v)
        #print("Columns: " + str(columns))
        #print("Rows: " + str(rows))
        return size, columns, rows
