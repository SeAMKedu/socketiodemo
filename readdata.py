import json, time, requests
import matplotlib.pyplot as plt # pip install matplotlib

tiedosto = open("data_2022_02_23.txt")

# {"ts":1645602535246612,"imu":{"afx":-0.635549,"afy":1.752426,"afz":-0.166623,"q0":0.920865,"q1":-0.007186,"q2":0.004896,"q3":0.389784,"roll":-0.539632,"pitch":0.837595,"yaw":45.879949},"uwb":"9D84[0.00,2.00,0.00]=0.85 14A6[0.00,0.00,0.00]=1.05 1B95[2.00,2.00,0.00]=1.88 1539[2.00,0.00,0.00]=2.08 le_us=3906 est[0.25,1.09,-0.07,55]"}

# listat x- ja y-dataa varten
xx = []
yy = []

alfa = 0
for rivi in tiedosto:
    rivi = rivi.rstrip()
    # deserialisoidaan rivi
    rivi_olio = json.loads(rivi)   
    
    # "uwb":"9D84[0.00,2.00,0.00]=0.85 14A6[0.00,0.00,0.00]=1.05 1B95[2.00,2.00,0.00]=1.88 1539[2.00,0.00,0.00]=2.08 le_us=3906 est[0.25,1.09,-0.07,55]"
    uwb_text = rivi_olio['uwb']
    
    osat = uwb_text.split(' ')
    # otetaan viimeinen alkio
    # est[0.25,1.09,-0.07,55]
    est = osat[-1]
    
    alku = est.find('[')
    loppu = est.find(']')
    s = est[alku+1:loppu] # 0.25,1.09,-0.07,55
    osat = s.split(',')
    x = float(osat[0])
    y = float(osat[1])
    # lisätään listoihin
    xx.append(x)
    yy.append(y)
    
    # TEHTÄVÄ A) Lähetä data Flask-palvelinsovellukselle
    # käyttäen requests-kirjastoa ja HTTP POSTia
    # Käytä samaa formaattia kuin edellisessä harjoituksessa (datagenerator.py)
    # Käynnistä ensin Flask-server
    s = {}
    s['alfa'] = alfa
    s['x'] = x
    s['y'] = y
    s['z'] = 0
    ss = json.dumps(s)
    response = requests.post("http://localhost:5000/uusimittaus", data = ss)
    alfa += 1
    
    # TEHTÄVÄ B) Lähetä data MQTT-brokerille (tämä ohjelma on MQTT publisher)
    # Käynnistä ensin Subscriber
    
    # TEHTÄVÄ C) Etsi datasta "alfa" eli suunta, johon laite on menossa. Olisiko yaw?
    
    time.sleep(1) # import time
    print(x, y)
    
plt.plot(xx,yy)
plt.show()

    
    

