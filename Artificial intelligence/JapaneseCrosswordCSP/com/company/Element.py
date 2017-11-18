class ELement:
    def __init__(self, column, values, index):
        self.ifColumn = column
        self.values = values
        self.index = index
        self.variant = []
        self.ifVariableSet = False
        self.settetValue = []

    def takeValues(self):
        return self.values

    def elementType(self):
        return self.ifColumn

    def setVariants(self, variant):
        self.variant = variant

    def getVariants(self):
        return self.variant

    def getIndex(self):
        return self.index

    def setSettetValue(self, v):
        self.settetValue = v

    def getSettetValue(self):
        return self.settetValue

    def deleteVariable(self, v):
        self.variant.remove(v)

    def ifSetVariable(self):
        return self.ifVariableSet

    def setVariable(self, flag):
        self.ifVariableSet = flag

    def toString(self):
        return "Column/Row: " + str(self.ifColumn) + ", Values: " + str(self.values) + ", index: " + str(self.index)