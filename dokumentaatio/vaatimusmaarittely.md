**Vaatimusmäärittely**
===================

Sovelluksen tarkoitus
----------------------

Sovelluksella voidaan pelata klassista hedelmäpeliä, missä tavoitteena on saada 3 samanlaista kuviota voittolinjalle. Jos onni suosii ja voitto tulee, voidaan voittoa kokeilla tuplata. Tällöin on mahdollista tuplata voitettu summa päävoittoon asti tai hävitä koko kerääntynyt voittosumma. Peliä ei pysty pelaamaan oikealla rahalla.  

Suunnitellut toiminnallisuudet 
-------------------------------

- [x] Käyttäjä voi lisätä virtuaalisia kolikoita pelikoneeseen jotka siirtyvät käyttäjän pelivaroihin
- [x] Sovellus osaa aropa satunnaisia kuviota pelilinjoille  
- [x] Käyttäjä voi valita pelipanoksen
- [x] Pelivarat vähenevät pelipanoksen verran joka kierroksella
- [x] Peliä ei voi pelata jos panos on isompi kuin käyttäjän pelivarat  
- [x] Käyttäjä voi lukita haluamansa pelilinjan
    - [x] Lukitun pelilinjan kuvio ei muutu pelatessa
    - [ ] Kuvioita voidaan lukita max 2 kpl
    - [ ] Kuvioita ei voi lukita jos kyseisellä kierroksella tuli voitto
    - [ ] Kuviot voidaan aina lukita vain yhden kierroksen ajaksi, jonka jälkeen vaaditaan uudelleenarvonta kaikista kuvioista.
- [ ] Voittosumma voidaan yrittää tuplata
    - [ ] Tuplaus on erillinen pelialue, jossa on kaksi erilaista kuviota
    - [ ] Käyttäjä valitsee yhden kuvioista
    - [ ] Pelikone arpoo voittokuvion näiden kahden kuvion välillä ja jos kuvio on sama kuin käyttäjän valitsema, tuplaa käyttäjä voittonsa. Muutoin käyttäjä häviää koko voittonsa
    - [ ] Tuplaus on mahdollista päävoittoon asti
    - [ ] Tuplauksesta voi poistua jolloin voittosumma lisätään käyttäjän pelivaroihin. 



Jatkokehitysideat
------------------------------
- Tarkempi statistiikka käytetyistä pelivaroista ja voitoista
- Mahdollisuus säädellä ja manipuloida voittomahdollisuuksia  


