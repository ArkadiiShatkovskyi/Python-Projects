import com.company.Reader
import com.company.Element


class Data:
    def __init__(self, size):
        reader = com.company.Reader.Reader(size)
        self.size, self.columns, self.rows = reader.readFile()
        self.cSize = self.size
        self.rSize = self.size
        self.posibilities = []
        e = com.company.Element.ELement(False, self.rows[0], 0)
        self.backTrack(e, 0, [0] * self.cSize, self.getPosibleIndexes(e))
        return

    def createElements(self):
        columns = []
        rows = []
        for i in range(0, len(self.columns)):
            columns.append(com.company.Element.ELement(True, self.columns[i], i))
        for i in range(0, len(self.rows)):
            rows.append(com.company.Element.ELement(False, self.rows[i], i))
        self.takePosibilities(columns)
        self.takePosibilities(rows)
        return self.size, self.takePosibilities(columns), self.takePosibilities(rows)

    def takePosibilities(self, elements):
        for e in elements:
            self.backTrack(e, 0, [0] * self.cSize, self.getPosibleIndexes(e))
            self.clearPosibilities()
            e.setVariants(self.posibilities.copy())
            self.posibilities.clear()
        return elements.copy()

    def clearPosibilities(self):
        for p in self.posibilities:
            for i in range(0, len(p)):
                if int(p[i]) == -1:
                    p[i] = 0

    def backTrack(self, element, index, list, positions):
        if self.checkIfCorrect(list, element.takeValues()):
            self.posibilities.append(list)
            list = [0] * self.cSize
            return list
        elif index > len(positions) - 1:
            return [0] * self.cSize
        for n in positions[index]:
            if list[n] != -1:
                tempList = list.copy()
                if element.takeValues()[index] == 1:
                    list[n] = 1
                    if n + 1 <= len(list) - 1:
                        list[n + 1] = -1
                elif element.takeValues()[index] > 1:
                    lastInd = n + element.takeValues()[index]
                    for i in range(n, lastInd):
                        list[i] = 1
                    if lastInd <= len(list) - 1:
                        list[lastInd] = -1
                self.backTrack(element, index + 1, list, positions)
                list = tempList
        return [0] * self.cSize

    def getPosibleIndexes(self, element):
        values = []
        for b in range(0, len(element.takeValues())):
            index = b + 1
            values.append(
                set(range(self.cSize - (sum(element.takeValues()[index:]) + len(element.takeValues()[index:])))[::1]))
        values = self.doSelectionOnIndexes(values, element.takeValues())
        for v in range(0, len(values)):
            values[v] = self.removeImpossibleIndexes(element.takeValues(), self.convertToList(values), v)
        return values

    def removeImpossibleIndexes(self, variables, values, index):
        n = sum(variables[:index]) + (len(variables[:index]) - 1)
        removeIndex = 0
        for i in range(0, len(values)):
            if values[i] == n:
                removeIndex = i
                break
        return values[index] if index == 0 else values[index][removeIndex + 1:].copy()

    def doSelectionOnIndexes(self, indexes, n):
        for i in range(0, len(indexes)):
            maxValue = max(indexes[i])
            ind = []
            for b in indexes[i]:
                if ((b + n[i]) - 1) > maxValue:
                    ind.append(b)
            for x in ind:
                indexes[i].remove(x)
        return indexes

    def convertToList(self, values):
        result = []
        for v in values:
            result.append(list(v))
        return result

    def checkIfCorrect(self, element, values):
        s = sum(values)
        n = 0
        for e in element:
            if int(e) == 1:
                n = n + 1
        return s == n

    def deleteRepetitions(self, element, elSize):
        for i in range(0, elSize):
            if int(element[i]) == -1:
                element[i] = 0
        return element