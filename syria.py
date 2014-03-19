import urllib2
from BeautifulSoup import BeautifulSoup
import codecs

f = codecs.open('syriawar_new.tsv', 'w', 'utf-8')
f.write("Row" + "\t" + "Data" + "\n")

for x in range (0,7):

  syria = "file" + "\t" + str(x)
  print "fetching data ... " + syria

  url ='http://vdc-sy.org/index.php/en/martyrs/' + str(x) + '/c29ydGJ5PWEua2lsbGVkX2RhdGV8c29ydGRpcj1ERVNDfGFwcHJvdmVkPXZpc2libGV8c2hvdz0xfGV4dHJhZGlzcGxheT0wfA=='

  page = urllib2.urlopen(url)
  soup = BeautifulSoup(page)

  rows = soup.findAll('tr')

  i = 0;
  for row in rows[3:]:
     if i%2 == 0:
     	
        f.write(str(i/2) + "\t" + row.text + "\n" )
     i += 1

f.close()