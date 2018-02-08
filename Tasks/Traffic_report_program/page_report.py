import sys
import re
import operator
import os.path

first_arg = sys.argv[1]

# method get filename and count requests
def traffic_report(file_name):
		if not os.path.isfile(file_name):	#checking if file exist
			print("File not exist")
			return 
		data = open(file_name)
		logs = data.read()
		urls = re.findall('(?:www\.)?[A-Z]?[a-z0-9]+\.[a-z]+(?:/[A-Za-z0-9]+)?', logs)	#regex to get only urls
		counter = dict()								#dictionary to count each url
		for url in urls:
			if counter.get(url) != None:
				counter[url] = counter.get(url) + 1
			else:
				counter.update({url: 1})
		counter = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)	#sorting dictionary by number of requests
		result = ""
		for key, value in counter:
			result += str(key) + ',' + str(value) + "\n"
		print(result)
	
if __name__ == "__main__":
	traffic_report(first_arg)