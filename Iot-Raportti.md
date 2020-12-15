# Äänestä aktivoituva valvontakamera

## Johdanto

Harjoitustyön tarkoituksena oli toteuttaa Internet of Things- projekti osana kurssia IoT-järjestelmän toteutus TTIW0200. Projektin aiheeksi valikoitui äänestä aktivoituva kamera jonka tarkoitus on ottaa kuva kun tarpeeksi voimakas ääni syntyy mikrofonin lähellä. Kuva lähetetään palvelimelle ja sitä voi verkkosivun kautta katsoa. Tiedot kuvista siirtyvät myös tietokantaan jota sivusto käyttää kuvien näyttämisessä. 

Järjestelmä toteutettiin Raspberry Pi:llä hyödyntäen laitteeseen sopivia moduleja(kamera ja mikrofoni). Tavoitteena oli luoda ympäristö missä “kameraa” voidaan käyttää ns. turvakamerana. Ryhmän aiheeseen liittyvä valmis osaaminen oli melko kapea-alainen ennen projektia mikä toi toteutukseen haastetta. 



## Toinen luku(esim.toteutus tai selitys laitteista)

Järjestelmää alettiin suunnitella ja toteuttaa Raspberry Pi:n avulla toimivaksi. Raspiin yhdistettiin siihen sopiva kamera ja mikrofoni, ja sinne tehtiin Python-koodi, joka mikrofonilta syötteen saatuaan käskee kameraa ottamaan kuvan. Koodi tiedostossa kuva2.py. Linkki tähän?

Mikrofonin ja kameran yhteistoiminta testattiin kotioloissa ja todettiin toimivaksi, mutta koronatilanteesta johtuen projektia vietiin eteenpäin ilman mikrofonia jotta järjestelmää pystyi testaamaan etänä. 

- Raspiin asennettiin Ubuntu käyttöjärjestelmä. 

## Kolmas luku

- 
