import os
import urllib.request
import io
import urllib.request

f = io.open('files.txt', 'r', encoding='utf8')

contents = None

if f.mode == 'r' or f.mode == 'rb':
	contents = f.read()

files = contents.split('\n')

destination = 'C:\\Users\\sanzh\\PycharmProjects\\ddos\\books\\'

for file in files:
	title = file.split('~')[0]
	link = file.split('~')[1]
	try:
		conn = urllib.request.urlretrieve(link)
		os.rename(conn[0], destination + title + '.epub')
		print('Successfully downloaded ' + title)
	except Exception as e:
		print(link + ' was unsuccessful and error was '+e.__str__())

f.close()
