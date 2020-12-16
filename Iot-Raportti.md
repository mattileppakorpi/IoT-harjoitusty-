# Äänestä aktivoituva valvontakamera

## Johdanto

Harjoitustyön tarkoituksena oli toteuttaa Internet of Things- projekti osana kurssia IoT-järjestelmän toteutus TTIW0200. Projektin aiheeksi valikoitui äänestä aktivoituva kamera jonka tarkoitus on ottaa kuva kun tarpeeksi voimakas ääni syntyy mikrofonin lähellä. Kuva lähetetään palvelimelle ja sitä voi verkkosivun kautta katsoa. Tiedot kuvista siirtyvät myös tietokantaan jota sivusto käyttää kuvien näyttämisessä. Projektin suunnitelma täällä (linkki tähän).

Järjestelmä toteutettiin Raspberry Pi:llä hyödyntäen laitteeseen sopivia moduleja (kamera ja mikrofoni). Tavoitteena oli luoda ympäristö missä “kameraa” voidaan käyttää ns. turvakamerana. Ryhmän aiheeseen liittyvä valmis osaaminen oli melko kapea-alainen ennen projektia mikä toi toteutukseen haastetta. 

Kuvien lähettämiseen palvelimelle päätettiin käyttää MQTT-protokollaa, ja yhteyden tarjoavana brokerina... mitä?

Osan ryhmästä palvelinohjelmointikurssilla tekemää harjoitustyötä päätettin käyttää tämän harjoitustyön yhteydessä kuvien esittämiseen tarkoitettuna järjestelmänä. Sovellus on Laravelilla toteutettu PHP-pohjainen MySQL-tietokantaan yhteydessä oleva ja kirjautumisen vaativa järjestelmä joka näyttää kuvat sitä mukaa kun Raspi niitä lähettää. Tuon järjestelmän tarkempia yksityiskohtia ei tässä raportissa käsitellä. 



## Toteutus

### Laitteisto

Järjestelmää alettiin toteuttaa koululta saadun Raspberry Pi:n avulla toimivaksi. Raspiin yhdistettiin siihen sopiva kamera ja mikrofoni, ja sinne tehtiin Python-koodi, joka mikrofonilta syötteen saatuaan käskee kameraa ottamaan kuvan. Koodi tiedostossa kuva2.py. Linkki tähän?

Mikrofonin ja kameran yhteistoiminta testattiin kotioloissa ja todettiin toimivaksi, mutta koronatilanteesta johtuen projektia vietiin eteenpäin ilman mikrofonia jotta järjestelmää pystyi testaamaan etänä sen jälkeen kun Raspi oli palautettu koululle. Päivitetty koodi otti kuvan ilman mikrofonia ajamalle koodi Raspissa.

### Palvelin 

Palvelimena toimi koulun verkkoon perustettu virtuaalikone.

### MQTT

### Laravel

Raspiin asennettiin Ubuntu käyttöjärjestelmä. (Asennettiinko me? Anssi?)(ei asennettu, raspin mukana tuli oma käyttis, joka oli luultavasti Rasbian, en muista varmasti)

Palvelimelle asensimme Laravel:n joka on ilmainen, avoimen lähdekoodin PHP web-ohjelmistokehys. Laravel on suunniteltu helpottamaan verkkosovellusten kehittämistä sisäänrakennettujen ominaisuuksien avulla. Laravel:n ominaisuuksia ovat mm. modulaarinen pakkausjärjestelmä joka tarkoittaa sitä että voit helposti lisätä toimintoja Laravel-sovellukseesi kirjoittamatta niitä tyhjästä sekä myös valmiiksi rakennettu todennusominaisuus.


## Ongelmia

Ongelmia tuotti Laravel-kehyksen asentaminen palvelimelle, koska palvelimelle oli asennettu Ubuntun versio 7.2 mutta jostain syystä MySql oli taasen versio 7.4 eivätkä näme olleet yhteensopivia. Tämä eiheutti sen että migraatioita palvelimen ja MySql:n välillä ei voitu suorittaa.

## Pohdinta

