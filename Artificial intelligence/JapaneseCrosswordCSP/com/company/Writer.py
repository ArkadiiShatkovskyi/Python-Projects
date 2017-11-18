

class Writer:
    def __init__(self):
        self.fileToWrite = '/media/arek/N/PWR/VII/SI/crossword/writed/result.txt'

    def write(self, data):
        textToWrite = ""
        data = self.deleteZeros(data)
        for e in data:
            textToWrite += str(e) + "\n"
        text_file = open(self.fileToWrite, "w")
        text_file.write(textToWrite)
        text_file.close()

    def deleteZeros(self, data):
        for e in data:
            for n in range(0,len(e)):
                if e[n] == 0:
                    e[n] = " "
                elif e[n] == 1:
                    e[n] = "X"
        return data