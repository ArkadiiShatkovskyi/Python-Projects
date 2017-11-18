class Element:

    def __init__(self, minDur, maxDur, durr, state, value):
        self.maxDur = maxDur
        self.minDur = minDur
        self.durr = durr
        self.value = value
        self.state = state

    def getMaxDur(self):
        return self.maxDur

    def setMaxDur(self, dur):
        self.maxDur = dur

    def getMinDur(self):
        return self.minDur

    def setMinDur(self, dur):
        self.minDur = dur

    def setValue(self, value):
        self.value = value

    def getDurr(self):
        return self.durr

    def getValue(self):
        return self.value

    def getState(self):
        return self.state

    def toString(self):
        return "Osobnik: min:"+self.getMinDur()+", max:"+self.getMaxDur()
