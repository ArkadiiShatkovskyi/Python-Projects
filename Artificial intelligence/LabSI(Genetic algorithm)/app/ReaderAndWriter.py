import xml
import xml.etree.ElementTree as ET
import io


class ReaderAndWriter:
    def __init__(self):
        self.fileToWrite = '/media/arek/N/PWR/VII/SI/dane/acosta/acosta_tls.add.xml'
        self.fileToRead = '/media/arek/F2620FB6620F7F1B/Work spaces/PyCharmProjects/Lab1SI/Lab1SI/dane/acosta_tls.add.xml'
        self.tree = ET.parse(self.fileToRead)

    def readFile(self):
        data = []
        root = self.tree.getroot()
        for parent in root:  # tlogic
            # print("TLogic: " + str(parent.attrib))
            for child in parent:  # phase
                durr = child.get('duration')
                minDur = child.get('minDur')
                maxDur = child.get('maxDur')
                state = child.get('state')
                if minDur != maxDur:
                    data.append([minDur, maxDur, durr, state])
                    #print("Phase: durr:" + str(durr) + ", minDur:" + str(minDur) + ", maxDur:" + str(maxDur) + ", state: "+str(state))
        return data

    def writeFile(self, el):
        root = self.tree.getroot()
        for child in root.findall('tlLogic'):
            for p in child:
                minD = int(p.get('minDur')) if p.get('minDur') is not None else 0
                maxD = int(p.get('maxDur')) if p.get('maxDur') is not None else 0
                st = str(p.get('state'))
                minDur = int(el.getMinDur())
                maxDur = int(el.getMaxDur())
                state = str(el.getState())
                #print("el1("+str(minD)+","+str(maxD)+","+str(st)+") el2("+str(minDur)+","+str(maxDur)+","+str(state)+")"+" if: "+str(minD == minDur and maxD == maxDur and st == state))
                if minD == minDur and maxD == maxDur and st == state:
                    p.set('duration', str(el.getValue()))
                    #print("Here")
                    self.tree.write(self.fileToWrite)