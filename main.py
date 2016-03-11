import requests as req
from bs4 import BeautifulSoup as bs

def run():
	
	#I will get all the all-night farmacy
	file2read = req.get( "http://www.colfacor.org.ar/turnosfarmacias/grid_turno_farmacia/" )	
	soup = bs(file2read.content,"html.parser")	
	
	#create a file where I will dump the data extracted	for test pourpuse
	file2write = open("table-data","w")

	#Get the data in an ugly way
	for tag in soup.find_all('table'):		
		table_raw = tag.attrs
		table_id = table_raw.get('id')		
		if str(table_id).find("#") != -1:
			file2write.write( str(tag) )						
	file2write.close()

if __name__ == '__main__':
	run()