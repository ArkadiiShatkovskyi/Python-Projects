import sys
import csv
import pycountry
import operator
from datetime import datetime

first_arg = sys.argv[1]

def startProgram(path):
	dataIn = readCSVFile(path)
	dataOut = []
	for line in dataIn:
		lineOut = processLine(line)
		mergeRows(dataOut, lineOut)
	dataOut = sortOutputData(dataOut)
	createOutputFile(dataOut, path)

def readCSVFile(path):
	l = []
	with open(path, mode='r') as infile:
		reader = csv.reader(infile)
		ll = map(list, reader)
		for line in ll:
			l.append(line)
	return l
	
def processLine(line):
	date = processDate(line[0])
	country = processState(line[1])
	impressionCount = processImpressionCount(line[2])
	cliks = processCTR(line[3], impressionCount)
	return [date, country, impressionCount, cliks]

def processDate(date):
	datetime_object = datetime.strptime(date, '%m/%d/%Y')
	return datetime_object.strftime('%Y-%m-%d')

def processState(state):
	pycountryObject = pycountry.subdivisions
	for subDiv in pycountryObject:
		if subDiv.name == state:
			countryObject=pycountry.subdivisions.get(code=subDiv.code)
			return countryObject.country.alpha_3
	return 'XXX'

def processImpressionCount(impressionCount):
	return impressionCount

def processCTR(ctr, impressionCount):
	ctr.replace(" ", "")
	impressionCount.replace(" ", "")
	ctrNumber = float(ctr[:-1])
	impressionCountNumber = float(impressionCount)
	return str(int(round((ctrNumber*impressionCountNumber)/100)))
	
def createOutputFile(data, filePath):
	with open(createOutputName(filePath), "w") as f:
		writer = csv.writer(f)
		writer.writerows(data)

def sortOutputData(data):
	data = sorted(data, key=operator.itemgetter(0, 1))
	return data

def createOutputName(inputFilePath):
	l = inputFilePath.split('.', 2)
	l[0] = l[0]+'output'
	return l[0] + '.' + l[1]
	
def mergeRows(data, line):
	if len(data) != 0:
		isChanged = 0
		for l in data:
			if l[0] == line[0] and l[1] == line[1]:
				isChanged = 1
				l[2] = str(int(float(l[2]) + float(line[2])))
				l[3] = str(int(float(l[3]) + float(line[3])))
		if not isChanged:
			data.append(line) 
	else:
		data.append(line)

if __name__ == "__main__":
	startProgram(first_arg)