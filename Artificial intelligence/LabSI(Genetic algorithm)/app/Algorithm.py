import Lab1SI.app.ReaderAndWriter as RW
import Lab1SI.app.Element as Element
import random
import subprocess
import re


class Algorithm:
    def __init__(self, ffe, sizeOfPop, pc, pm):
        self.rw = RW.ReaderAndWriter()
        self.data = self.readData()
        self.ffe = ffe
        self.population = []
        # self.ffe = 100
        # self.sizeOfPopulation = 20
        # self.probabilityOfCrossing = 50
        # self.probabilityOfMutation = 10
        self.sizeOfPopulation = sizeOfPop
        self.probabilityOfCrossing = pc
        self.probabilityOfMutation = pm
        self.command = "sumo -c /media/arek/N/PWR/VII/SI/dane/acosta/run.sumo.cfg -v"
        self.elementsPointsInPopulation = []
        return

    def run(self):
        self.createFirstPopulation()
        print("Run: pop:" + str(self.sizeOfPopulation) + ", ffe:" + str(self.ffe) + ", pc:" + str(
            self.probabilityOfCrossing) + ", pm:" + str(self.probabilityOfMutation))
        # self.showPopulation()
        for i in range(0, self.ffe):
            self.evaluatePopulation()
            print("Values" + str(i) + ": best:" + str(max(self.elementsPointsInPopulation)) +
                  ", avg:" + str(sum(self.elementsPointsInPopulation) / len(self.elementsPointsInPopulation)) +
                                 ", min:" + str(min(self.elementsPointsInPopulation)))
            self.population = self.selection()
            self.crossing()
            self.evaluatePopulation()
            print("Values" + str(i) + ": best:" + str(max(self.elementsPointsInPopulation)) +
                  ", avg:" + str(sum(self.elementsPointsInPopulation) / len(self.elementsPointsInPopulation)) +
                  ", min:" + str(min(self.elementsPointsInPopulation)))
            self.mutation()
        self.evaluatePopulation()
        print("Values" + str(i) + ": best:" + str(max(self.elementsPointsInPopulation)) +
              ", avg:" + str(sum(self.elementsPointsInPopulation) / len(self.elementsPointsInPopulation)) +
              ", min:" + str(min(self.elementsPointsInPopulation)))
        # self.showPopulation()

    def readData(self):
        pop = []
        data = self.rw.readFile()
        for el in data:
            pop.append(Element.Element(el[0], el[1], el[2], el[3], -1))
        return pop

    def createFirstPopulation(self):
        for n in range(0, self.sizeOfPopulation):
            tempOs = []
            for c in self.data:
                value = int(random.randint(int(c.getMinDur()), int(c.getMaxDur())))
                tempOs.append(Element.Element(c.getMinDur(), c.getMaxDur(), c.getDurr(), c.getState(), value))
            self.population.append(tempOs.copy())
        return

    def selection(self):
        newPopulation = []
        for e in range(0, len(self.population)):
            os1 = random.randint(0, len(self.population) - 1)
            os2 = random.randint(0, len(self.population) - 1)
            os3 = random.randint(0, len(self.population) - 1)
            os4 = random.randint(0, len(self.population) - 1)
            best = os1
            for o in [os2, os3, os4]:
                if self.elementsPointsInPopulation[best] < self.elementsPointsInPopulation[o]:
                    best = o
            newPopulation.append(self.population[best])
            #newPopulation.append(
                #self.population[os1] if self.elementsPointsInPopulation[os1] > self.elementsPointsInPopulation[os2]
                #else self.population[os2])
        return newPopulation

    def crossing(self):  # krzyżowanie równolegle
        for i in range(0, len(self.population)):
            indexOs1 = random.randint(0, len(self.population) - 1)
            indexOs2 = random.randint(0, len(self.population) - 1)
            os1 = self.population[indexOs1]
            os2 = self.population[indexOs2]
            for e in range(0, len(os1)):
                if random.randrange(0, 101, 1) <= self.probabilityOfCrossing:
                    temp = os1[e].getValue()
                    os1[e].setValue(os2[e].getValue())
                    os2[e].setValue(temp)
        return

    def mutation(self):
        for p in self.population:
            for e in p:
                if random.randrange(0, 101, 1) <= self.probabilityOfMutation:
                    e.setValue(random.randint(int(e.getMinDur()), int(e.getMaxDur())))
        return

    def writeElement(self, data):  # zapisywanie osobnika
        for os in data:
            self.rw.writeFile(os)

    def evaluatePopulation(self):
        self.elementsPointsInPopulation.clear()
        for e in self.population:
            self.writeElement(e)
            self.elementsPointsInPopulation.append(self.evaluateElement())

    def evaluateElement(self):  # ewaulacja osobnika
        numbers = self.takeEvaluateArguments()
        inserted = 0
        loaded = 1
        running = 0
        waiting = 0
        teleports = 0
        if len(numbers) == 4:
            inserted, loaded, running, waiting = numbers
        elif len(numbers) >= 5:
            inserted = numbers[0]
            loaded = numbers[1]
            running = numbers[2]
            waiting = numbers[3]
            teleports = numbers[4]
        # print(str(inserted) + ", " + str(loaded) + ", " + str(running) + ", " + str(waiting) + ", " + str(teleports))
        return 1 - (loaded - inserted + running + waiting + teleports) / loaded

    def takeEvaluateArguments(self):
        process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=None, shell=True)
        output = process.communicate()
        s = output[0]
        smod = s[675:]
        s1 = smod.decode("utf-8")
        s1 = re.sub('[()]', '', s1)
        # print(s1)
        return [int(s) for s in s1.split() if s.isdigit()]

    def showPopulation(self):
        print("Populacja")
        for n in range(0, len(self.population)):
            print("Osobnik" + str(n) + " [", end='', flush=True)
            for e in self.population[n]:
                print(e.getValue(), end=', ', flush=True)
            print("]\n", end='', flush=True)
        print()
        '''
        print("Data ")
        for el in self.data:
            print("minDur: " + el.getMinDur() + ", maxDur: " + el.getMaxDur())
        '''
