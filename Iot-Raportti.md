# Äänestä aktivoituva valvontakamera

## Johdanto

Harjoitustyön tarkoituksena oli toteuttaa Internet of Things- projekti osana kurssia IoT-järjestelmän toteutus TTIW0200. Projektin aiheeksi valikoitui äänestä aktivoituva kamera jonka tarkoitus on ottaa kuva kun tarpeeksi voimakas ääni syntyy mikrofonin lähellä. Kuva lähetetään palvelimelle ja sitä voi verkkosivun kautta katsoa. Tiedot kuvista siirtyvät myös tietokantaan jota sivusto käyttää kuvien näyttämisessä. Projektin suunnitelma täällä (linkki tähän).

Järjestelmä toteutettiin Raspberry Pi:llä hyödyntäen laitteeseen sopivia moduleja (kamera ja mikrofoni). Tavoitteena oli luoda ympäristö missä “kameraa” voidaan käyttää ns. turvakamerana. Ryhmän aiheeseen liittyvä osaaminen oli melko kapea-alainen ennen projektia mikä toi toteutukseen haastetta. 

Kuvien lähettämiseen palvelimelle päätettiin käyttää MQTT-protokollaa, ja yhteyden tarjoavana brokerina Mosquitto.

Osan ryhmästä palvelinohjelmointikurssilla tekemää harjoitustyötä päätettin käyttää tämän harjoitustyön yhteydessä kuvien esittämiseen tarkoitettuna järjestelmänä. Sovellus on Laravelilla toteutettu PHP-pohjainen MySQL-tietokantaan yhteydessä oleva ja kirjautumisen vaativa järjestelmä joka näyttää kuvat sitä mukaa kun Raspi niitä lähettää. Tuon järjestelmän tarkempia yksityiskohtia ei tässä raportissa käsitellä. 



## Toteutus

### Laitteisto

Järjestelmää alettiin toteuttamaan koululta saadun Raspberry Pi:n avulla toimivaksi. Raspiin yhdistettiin siihen sopiva kamera ja mikrofoni, ja sinne tehtiin Python-koodi, joka mikrofonilta syötteen saatuaan käskee kameraa ottamaan kuvan. Koodi tiedostossa kuva2.py. Linkki tähän?

<img src="/rasbi.jpg" width="100" height="100">

Mikrofonin ja kameran yhteistoiminta testattiin kotioloissa ja todettiin toimivaksi, mutta koronatilanteesta johtuen projektia vietiin eteenpäin ilman mikrofonia jotta järjestelmää pystyi testaamaan etänä sen jälkeen kun Raspi oli palautettu koululle. Päivitetty koodi otti kuvan ilman mikrofonia ajamalla koodi Raspissa. 


### MQTT

Kuvan lähettämiseen käytettiin MQTT-yheyttä. Tähän vois vähän kertoo miten se toimii???

Ennen lähettämistä Raspi muuttaa kuvan base64-muotoon. 

### Palvelin 

Palvelimena toimi koulun verkkoon perustettu virtuaalikone. Palvelimelle tehtiin Python-koodi joka ottaa Raspbetty Pi:n muuntaman ja lähettämän kuvan vastaan ja purkaa Base64-muunnoksen takaisin kuvaksi ja tallentaa sen datetime-timestampin nimisenä public-kansioon. Kuvan vastaanoton yhteydessä kuvan tiedot lähetetään myös MySQL-palvelimelle missä olevan tietokannan avulla kuvat näytetään käyttäjälle. 

### Laravel


Palvelimelle asensimme Laravel:n joka on ilmainen, avoimen lähdekoodin PHP web-ohjelmistokehys. Laravel on suunniteltu helpottamaan verkkosovellusten kehittämistä sisäänrakennettujen ominaisuuksien avulla. Laravel:n ominaisuuksia ovat mm. modulaarinen pakkausjärjestelmä joka tarkoittaa sitä että voit helposti lisätä toimintoja Laravel-sovellukseesi kirjoittamatta niitä tyhjästä sekä myös valmiiksi rakennettu todennusominaisuus. Myös MySQL-tietokannan käyttö on Laravelin avulla kätevää. 

Mietimme mitä ominaisuuksia haluaisimme kyseiseen kehykseen, jotta se vastaisi harjoitustyön vaatimuksia myös Web-palvelinohjelmointi opintojakson puolella.

Ominaisuuksia:
* Laravel näyttää kuvat MySQL-tietokannasta linkkien kautta. 
* Järjestelmään rekisteröityminen sekä kirjautuminen
* Kuvien katsominen valitsemalla joko listasta tai selaamalla
* Kuvakohtainen kommentointi
* Admin-oikeuksilla kommenttien poistaminen ja kuvien tietojen muokkaaminen
* Kuvat nimetty datetime:lla kuvan oton yhteydessä


## Ongelmia

Ongelmia tuotti Laravel-kehyksen asentaminen palvelimelle, koska palvelimelle oli asennettu Ubuntun versio 7.2 mutta jostain syystä MySql oli taasen versio 7.4 eivätkä näme olleet yhteensopivia. Tämä aiheutti sen että migraatioita palvelimen ja MySql:n välillä ei voitu suorittaa.

Myös MQTT-yhteyden kanssa oli melko paljon ongelmia ennen kuin se saatiin toimimaan. Tämä johtui lähinnä siitä että MQTT oli melko uusi tuttavuus kaikille tekijöille ja yhteyden käytännön toteutus sen vuoksi vierasta.

## Pohdinta

