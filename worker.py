import urllib.request, urllib.error
import sys, io

url = 'http://www.mektep.kz/'

f = io.open('links.txt', 'r')
ff = io.open('files.txt', 'w+', encoding='utf8')

contents = None

if f.mode == 'r':
	contents = f.read()

f.close()

links = contents.split('http:')
links.remove('')

links = ['http:' + s for s in links]
files = []

for link in links:
	try:
		conn = urllib.request.urlopen(link)
	except urllib.error.HTTPError as e:
		# Return code error (e.g. 404, 501, ...)
		# ...
		print('HTTPError: {}'.format(e.code))
	except urllib.error.URLError as e:
		# Not an HTTP-specific error (e.g. connection refused)
		# ...
		print('URLError: {}'.format(e.reason))
	else:
		bytes = conn.read()
		page = bytes.decode('utf8')
		ref_point = page.find('Books')
		if ref_point != -1:
			titleStart = page.find('<title>')
			titleEnd = page.find('</title>')
			title = page[titleStart+7:titleEnd]
			start = page.find('href', ref_point)
			end = page.find('download', ref_point)
			files.append(title+'~'+url+page[start + 6:end - 2])
		conn.close()

print(files)

for file in files:
	ff.write(file+'\n')

ff.close()
