# Äänestä aktivoituva valvontakamera

## Johdanto

Harjoitustyön tarkoituksena oli toteuttaa Internet of Things- projekti osana kurssia IoT-järjestelmän toteutus TTIW0200. Projektin aiheeksi valikoitui äänestä aktivoituva kamera jonka tarkoitus on ottaa kuva kun tarpeeksi voimakas ääni syntyy mikrofonin lähellä. Kuva lähetetään palvelimelle ja sitä voi verkkosivun kautta katsoa. Tiedot kuvista siirtyvät myös tietokantaan jota sivusto käyttää kuvien näyttämisessä. Projektin suunnitelma [täällä](/Suunnitelma.md).

Järjestelmä toteutettiin Raspberry Pi:llä hyödyntäen laitteeseen sopivia moduleja (kamera ja mikrofoni). Tavoitteena oli luoda ympäristö missä kameraa voidaan käyttää ikään kuin turvakamerana. Ryhmän aiheeseen liittyvä osaaminen oli melko kapea-alainen ennen projektia mikä toi toteutukseen haastetta. 

Kuvien lähettämiseen palvelimelle päätettiin käyttää MQTT-protokollaa, ja yhteyden tarjoavana brokerina Mosquitto. Tähän päädyttiin koska MQTT on yleisesti käytetty ja kätevä viestinvälitystapa tämän kaltaisissa projekteissa ja toisaalta projekti oli hyvä tilaisuus tutustua MQTT:n paremmin.

Osan ryhmästä web-palvelinohjelmointikurssilla tekemää harjoitustyötä päätettin käyttää tämän harjoitustyön yhteydessä kuvien esittämiseen tarkoitettuna järjestelmänä. Sovellus on Laravelilla toteutettu PHP-pohjainen MySQL-tietokantaan yhteydessä oleva ja kirjautumisen vaativa järjestelmä joka näyttää kuvat sitä mukaa kun Raspi niitä lähettää. Tuon järjestelmän tarkempia yksityiskohtia ei tässä raportissa käsitellä. 



## Toteutus

### Laitteisto

Järjestelmää alettiin toteuttamaan koululta saadun Raspberry Pi:n avulla toimivaksi. Raspiin yhdistettiin siihen sopiva kamera ja mikrofoni, ja sinne tehtiin Python-koodi, joka mikrofonilta syötteen saatuaan käskee kameraa ottamaan kuvan. Koodi tiedostossa [kuva2.py](/kuva2.py).

<img src="/raspi.jpg" width="400" height="400" title="Raspberry Pi">  <img src="/plugit.png" width="700" height="400" title="Kytkennät">

Mikrofonin ja kameran yhteistoiminta testattiin kotioloissa ja todettiin toimivaksi, mutta koronatilanteesta johtuen projektia vietiin eteenpäin ilman mikrofonia jotta järjestelmää pystyi testaamaan etänä sen jälkeen kun Raspi oli palautettu koululle. Päivitetyssä versiossa kuva otettiin ilman mikrofonia ajamalla koodi  [sendimage.py](/sendimage.py) Raspissa.


### MQTT

Kuvan lähettämiseen Rapsberry Pi:ltä käytettiin MQTT (Message Queuing Telemetry Transport) julkaisu protokollaa. MQTT on kevyt lähetys ja vastaanotto protokolla, jota käytetään lähettämään viestejä laitteiden välillä. MQTT-yhteyden tarjoava Mosquitto asennettiin Rapsberry Pi:lle ja palvelin puolelle siten, että palvelin on vastaanottaja ja Rapsberry Pi on lähettäjä. Kuvan ottamisen jälkeen kuva muutetaan Base64 encryptaus muotoon, jonka jälkeen se lähetetään brokerille, josta palvelin sen saa. Palvelimella kuva muutetaan takaisin normaaliin kuva formattiin. [sendimage.py](/sendimage.py)

### Palvelin 

Palvelimena toimi koulun verkkoon perustettu virtuaalikone. Palvelimelle tehtiin Python-koodi joka ottaa Raspberry Pi:n muuntaman ja lähettämän kuvan vastaan ja purkaa Base64-muunnoksen takaisin kuvaksi ja tallentaa sen datetime-timestampin nimisenä public-kansioon. Kuvan vastaanoton yhteydessä kuvan tiedot lähetetään myös MySQL-palvelimelle missä olevan tietokannan avulla kuvat näytetään käyttäjälle. Tietoturvasyistä MySQL-yhteyden tarkemmat tiedot ovat eri tiedostossa joka ei tässä raportissa ole mukana. Palvelimella oleva koodi [sub.py](/sub.py)

### MySql

Tietokanta sijaitsi JAMK:n student-palvelimella. Images-taulun time-kenttä jäi turhaksi koska aikaleima tuli kuvan nimeksi mutta se siellä vielä on.

<img src="/mysql1.PNG" width="200" height="200" title="Tietokanta"> <img src="/mysql2.PNG" width="400" height="200" title="Images table">

### Laravel


Palvelimelle asennettiin Laravel, joka on ilmainen, avoimen lähdekoodin PHP web-ohjelmistokehys. Laravel on suunniteltu helpottamaan verkkosovellusten kehittämistä sisäänrakennettujen ominaisuuksien avulla. Laravel:n ominaisuuksia ovat mm. modulaarinen pakkausjärjestelmä joka tarkoittaa sitä että voit helposti lisätä toimintoja Laravel-sovellukseesi kirjoittamatta niitä tyhjästä sekä myös valmiiksi rakennettu todennusominaisuus. Myös MySQL-tietokannan käyttö on Laravelin avulla kätevää, ja tietoturva-asiat on Laravelissa huomioitu hyvin. Tarkemmin kuvat näyttävään sovellukseen voi tutustua linkin takaa.  [ Laravel ](https://student.labranet.jamk.fi/~N3998/Palvelinohjelmointi/harjoitustyo/Raportti.html)

Alle on listattu ominaisuuksia mitä kyseiseen kehykseen haluttiin, jotta se vastaisi harjoitustyön vaatimuksia myös Web-palvelinohjelmointi opintojakson puolella.

* Laravel näyttää kuvat MySQL-tietokannasta linkkien kautta. 
* Järjestelmään rekisteröityminen sekä kirjautuminen
* Kuvien katsominen valitsemalla joko listasta tai selaamalla
* Kuvakohtainen kommentointi
* Admin-oikeuksilla kommenttien poistaminen ja kuvien tietojen muokkaaminen
* Kuvat nimetty datetime:lla kuvan oton yhteydessä

<img src="/laravel1.PNG" width="500" height="400" title="Kuvat lista muodossa"> <img src="/laravel2.PNG" width="500" height="400" title="Kommentit">

Kuvassa laravel-sivusto. Kuvista suurin osa on testidataa. Ääkköset eivät jostain syystä toimi.
## Ongelmia

Ongelmia tuotti Laravel-kehyksen asentaminen palvelimelle, koska palvelimelle oli asennettu Ubuntun versio 7.2 mutta jostain syystä MySql oli taasen versio 7.4 eivätkä näme olleet yhteensopivia. Tämä aiheutti sen että migraatioita palvelimen ja MySql:n välillä ei voitu suorittaa.

Myös MQTT-yhteyden kanssa oli melko paljon ongelmia ennen kuin se saatiin toimimaan. Tämä johtui lähinnä siitä että MQTT oli melko uusi tuttavuus kaikille tekijöille ja yhteyden käytännön toteutus sen vuoksi vierasta.

## Pohdinta

Projekti oli kokonaisuutena erittäin opettava ja mielenkiintoinen. Kun miettii lähtökohtia jotka olivat ne, että Raspberry Pi oli aivan vieras laite ryhmäläisille ennen kurssia, python kielenä vieras monelle, IoT-laitteen ja palvelimen yhteistyö tuntematonta ja kuinka vaikealta tuntui keksiä aihetta projektiin niin projekti onnistui mielestämme erittäin hyvin.

IoT-järjestelmän perusosat ovat yksinkertaisesti mutta hyvin esillä työssä. Sensori eli mikrofoni ottaa ympäristöstä syötteen, actuator tekee toiminnan, eli Pi ottaa kuvan, ja data käsitellään muuttamalla se base64 muotoon ennen lähettämistä eteenpäin, tässä tapauksessa säilytettäväksi ja esitettäväksi palvelimelle. 
Harjoitustyön aikana tuli opittua paljon uusia asioita, ja ennen lähinnä teoriapohjalla ollut IoT-tietämys lisääntyi. Esim Raspberry Pi:n käyttö oli kaikille ryhmäläisille uusia asia, samaten siihen liittyvien kameran ja mikrofonin. Myös MQTT oli entuudestan tuttu vain Johdatus teolliseen intrnetiin-kurssin yhdestä harjoitustyöstä jossa sitä käytettiin Noderedin avulla, mutta nyt aiheeseen tutustuttiin paremmin. 
Python koodauskielenä ei ollut kaikkein tutuin entuudestaan mutta siihen päädyttiin sen vuoksi että se on niin laajalti käytetty IoT-projekteissa ja esimerkkikoodeja olisi varmasti helpoimmin löydettävissä. Mahdollisesti työ olisi valmistunut hieman nopeammin esim. C#:ia käyttäen, mutta samat haastavat kohdat olisi ollut selvitettävänä kuitenkin ja esimerkkitoteutuksia olisi ehkä ollut vaikeampi löytää. 
MQTT-yhteys olisi ollut fiksumpi tehdä niin päin että palvelin toimii 



- Tuliko opittua jotain muuta??
-Mitä olisi voinut tehdä toisin?
