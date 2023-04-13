import requests    
import json   
import math   
import time  
import random 

import numpy as np # pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib

# tehdään listat plottaamista varten
alfat = []
xt = []
yt = []

sade = 10
alfa = 0
while alfa < 10:
    # import random 
    measurement = { }
    measurement['alfa'] = alfa
    measurement['x'] = sade * math.cos(alfa) + (random.random() * 2 - 1)
    measurement['y'] = sade * math.sin(alfa) + (random.random() * 2 - 1)
    measurement['z'] = 0

    # lisätään vielä listoihin plottaamista varten
    alfat.append(measurement['alfa'])
    xt.append(measurement['x'])
    yt.append(measurement['y'])

    # muunna json-muotoon 
    s = json.dumps(measurement)
    # TODO: lähetä data HTTP Postilla serverille
    response = requests.post("http://localhost:5000/uusimittaus", data = s)

    print(s)
    time.sleep(0.5)

    alfa += 0.1
# plotataan
plt.plot(alfat, xt, '-r')
plt.plot(alfat, yt, '-b')
plt.show()
