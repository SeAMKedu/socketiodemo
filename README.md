# Python Flask, socket.io ja Google Charts

Tässä esimerkissä näytetään, miten mittausdataa voidaan näyttää web-sovelluksessa Google Chartin avulla niin, että data päivittyy reaaliaikaisesti.

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
