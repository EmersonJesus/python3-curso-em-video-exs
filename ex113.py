import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Não foi possível acessar o site')
else:
    print('O site está funcionando!')