import com.company.Data
import copy
import time


class ForwardChecking:

    def __init__(self, s, sortMethod = None):
        data = com.company.Data.Data(s)
        self.writer = com.company.Writer.Writer()
        size, self.columns, self.rows = data.createElements()
        if sortMethod == None:
            self.elements = self.createListOfElements()
        else:
            self.elements = sortMethod(self.rows, self.columns) #heuristic
        self.grid = [[int(0)]*size for _ in range(size)]
        self.history = []
        self.history.append(self.grid.copy())
        self.awaibleVariables = self.createListOfVariables()
        self.cSize = size
        self.rSize = size
        self.sets = 0

    def createListOfElements(self):
        elements = []
        for i in range(0, len(self.columns)):
            elements.append(self.rows[i])
            elements.append(self.columns[i])
        return elements

    def createListOfVariables(self):
        list = []
        for e in self.elements:
            list.append(copy.deepcopy(e.getVariants()))
        return list

    def run(self):
        start_time = time.time()
        result = self.forwardChecking(0)
        print("Result: " + str(result) + " Time: " + str((time.time() - start_time) * 1000) + ", Sets: " + str(self.sets))
        self.showGrid()
        self.writer.write(self.grid)
        return (time.time() - start_time) * 1000, self.sets

    def forwardChecking(self, index):
        if self.IfEndOfGrid():
            return True
        tempElements = copy.deepcopy(self.elements)
        for v in self.awaibleVariables[index]:
            self.setVariableToGrid(v, self.elements[index])
            self.setConstrains(self.elements[index])
            self.sets += 1
            if self.checkCollisions(index):
                if self.forwardChecking(index + 1):
                    return True
        self.elements = tempElements
        self.undoVariable(self.elements[index])
        self.updateGrid(index)
        return False

    def IfEndOfGrid(self):
        for e in self.elements:
            if not e.ifSetVariable():
                return False
        return True

    def setConstrains(self, element):
        type = element.elementType()
        for e in self.elements:
            for v in e.getVariants():
                i = e.getIndex()
                if not type and e.elementType():
                    if v[i] != element.getSettetValue()[i]:
                        e.deleteVariable(v)
                elif type and not e.elementType():
                    if v[i] != element.getSettetValue()[i]:
                        e.deleteVariable(v)


    def checkCollisions(self, index):
        for e in self.elements[0:index+1]:
            type = e.elementType()
            actualEl = []
            if type == False:
                actualEl = self.grid[e.getIndex()]
            else:
                tempEl = []
                for i in range(0, len(self.grid)):
                    tempEl.append(self.grid[i][e.getIndex()])
                actualEl = tempEl
            s = sum(e.takeValues())
            n = sum(actualEl)
            if int(n) != int(s):
                return False
        return True

    def undoVariable(self, element):
        typeOfElement = element.elementType()
        if typeOfElement == False:
            self.grid[element.getIndex()] = [0] * self.rSize
            element.setVariable(False)
            element.setSettetValue([0] * self.rSize)
        else:
            for i in range(0, len(self.grid)):
                self.grid[i][element.getIndex()] = 0
            element.setVariable(False)
            element.setSettetValue([0] * self.cSize)

    def updateGrid(self, index):
        for e in self.elements[0:index]:
            typeOfElement = e.elementType()
            if typeOfElement == False:
                self.grid[e.getIndex()] = e.getSettetValue().copy()
            else:
                for i in range(0, len(self.grid)):
                    self.grid[i][e.getIndex()] = e.getSettetValue()[i]

    def setVariableToGrid(self, v, element):
        typeOfElement = element.elementType()
        if typeOfElement == False:
            self.grid[element.getIndex()] = v.copy()
            element.setVariable(True)
            element.setSettetValue(v)
        else:
            for i in range(0, len(self.grid)):
                self.grid[i][element.getIndex()] = v[i]
            element.setVariable(True)
            element.setSettetValue(v)
        return self.grid.copy()

    def showElements(self, elements):
        for e in elements:
            print("Elements" + str(e.getIndex()) + ", " + "column/row:" + str(e.elementType()) + ":" + str(e.getVariants()))
        print()

    def showGrid(self):
        for r in self.grid:
            print(r)
        print()

    def toStringElement(self):
        for e in self.elements:
            print(str(e.toString()) + "Variables: " + str(len(e.getVariants())))
        print()