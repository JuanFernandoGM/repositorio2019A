from bs4 import BeautifulSoup
import urllib3
import pandas as pd
from tabulate import tabulate 
http=urllib3.PoolManager()

urllib3.disable_warnings()

url='https://es.wikipedia.org/wiki/Anexo:Presidentes_de_los_Estados_Unidos_por_edad'

responde=http.request('GET',url)


soup=BeautifulSoup(responde.data)
table = soup.find_all('table')
g=str(table)

df = pd.read_html(g)




print( tabulate(df[0], headers='keys', tablefmt='psql') )
