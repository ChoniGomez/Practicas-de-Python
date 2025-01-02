#libreria para acceder a la ip
import requests

#hago una peticion a una api a traves de requests
request = requests.get('https://ident.me')
ip_publica = request.text
print(ip_publica)


