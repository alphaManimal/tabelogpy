import tabel

fkey = open('~/.tabelogapikey','r')
apiKey = fkey.readline().strip('\n')

# test sets
mycrawler = tabel.crawler(apiKey)
mycrawler.setLatitude('35.784')
mycrawler.setLongitude('139.756')
mycrawler.setStation('Yokohama')
mycrawler.setResultSet('large')
mycrawler.setSortOrder('highprice')
mycrawler.setResultDatum('Tokyo')
mycrawler.setSearchRange('large')
#mycrawler.setPageNumber('1')

mycrawler.setOutputFile('test.xml')

# test gets
print mycrawler.getKey()
print mycrawler.getLatitude()
print mycrawler.getLongitude()
print mycrawler.getStation()
print mycrawler.getResultSet()
print mycrawler.getSortOrder()
print mycrawler.getResultDatum()
print mycrawler.getSearchRange()
print mycrawler.getPageNumber()

print mycrawler.countParams()

# test workers
#print mycrawler.crawl()



