Fruity Slots
============

Klassinen hedelmäpeli, missä tavoitteena on saada 3 samanlaista kuviota voittolinjalle.


Dokumentaatio
-------------------------

[Vaatimusmäärittely](https://github.com/hzville/ohte-harjoitustyo-2021/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/hzville/ohte-harjoitustyo-2021/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/hzville/ohte-harjoitustyo-2021/blob/master/dokumentaatio/arkkitehtuuri.md)

[Viimeisin release](https://github.com/hzville/ohte-harjoitustyo-2021/releases)

[Käyttöohje](https://github.com/hzville/ohte-harjoitustyo-2021/blob/master/dokumentaatio/kayttoohje.md)


Asennus
-------------------
Sovellus on toteutettu Python-versiolla `3.8.5` Sovelluksen toimivuutta ei voida taata tätä vanhemmilla versioilla.

Sovelluksen ja testien suorittamiseen tarvitset Poetry-komentorivityökalun. 
Voit asentaa Poetryn osoitteesta https://python-poetry.org/ .

Poetryn asentamisen jälkeen, saat asennettua sovelluksen riippuvuudet komenolla:
```bash
poetry install
```
Sovelluksen voi käynnistää komennolla:
```bash
poetry run invoke start
```
Yksikkötestien suoritus tapahtuu komennolla:
```bash
poetry run invoke test
```
Yksikkötestien tulokset luodaan komenolla:
```bash
poetry run invoke coverage-report
```
Komennon jälkeen yksikkötestien tulokset löytyvät htmlcov-hakemistosta. Tulokset löytyvät hakemiston sisällä tiedostosta index.html . Tiedoston index.html voit 
avata haluamallasi verkkoselaimella tai komennolla:
```bash
firefox htmlcov/index.html
```
Koodin rakennetta voi arvioida Pylint työkalulla. Arviointi suoritetaan komennolla:
```bash
poetry run invoke lint
```

