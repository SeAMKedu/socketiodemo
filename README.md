# Python Flask, socket.io ja Google Charts

Tässä esimerkissä näytetään, miten mittausdataa voidaan näyttää web-sovelluksessa Google Chartin avulla niin, että data päivittyy reaaliaikaisesti.

Ohjelma datageneratorclient.py (tai readdata.py) generoi simuloitua mittausdataa ja lähettää sen palvelinohjelmalla. Flaskilla toteutettu palvelinohjelma measserver.py vastaanottaa mittaukset ja välittää ne html-sivulle, jossa ne näytetään Google Chart -kaavioina. Palvelinohjelman ja html-sivun välisessä kommunikoinnissa käytetään socket.io:ta.

## Tiedostot

### datageneratorclient.py

Python-ohjelma datageneratorclient.py generoi simuloitua mittausdataa. Kuvitteellisen laitteen paikkakoordinaatit generoidaan trigonometristen funktioiden avulla:

```python
    measurement = { }
    measurement['time'] = t
    measurement['x'] = 5 * math.cos(t) + (random.random() * 2 - 1)
    measurement['y'] = 6 * math.sin(t) + (random.random() * 2 - 1)
    measurement['z'] = (random.random() * 2 - 1)
```
Generoidut mittaukset lähetetään palvelimelle HTTP Postin avulla:

```python
    # muunna json-muotoon 
    s = json.dumps(measurement)
    # TODO: lähetä data HTTP Postilla serverille
    response = requests.post("http://localhost:5000/uusimittaus", data = s)
```
### measserver.py

Python Flask-ohjelma measserver.py vastaanottaa mittaukset ja välittää ne html-sivulle socket.io:n avulla. Ohjelman alustukset ja käynnistytoimenpiteet on esitetty alla:

```python
import json
from flask import Flask, render_template, request
from flask_socketio import SocketIO
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Lista mittauksia varten
measurements = []

...

if __name__ == '__main__':
    socketio.run(app)
```
