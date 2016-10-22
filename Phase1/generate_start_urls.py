f = open('urls.txt','wb')
for i in range(1,45):
	f.write('"http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-%d?PageSize=36&order=BESTMATCH"\n,'%i)
f.close()

