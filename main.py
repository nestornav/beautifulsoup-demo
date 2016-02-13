from bs4 import BeautifulSoup as bs


def run():
	file2read = open("farm-turno")
	soup = bs(file2read,"html.parser")
	file2read.close()
	print( soup.prettify() )

if __name__ == '__main__':
	run()