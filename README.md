# HEEM-Data-Extractions

Dit project valt onder het promotieonderzoek van Tim Vergeer.
Juni 2020.

### Auteurs
- Sanne Hoeken
- Tim Vergeer

### Project

Het promotieonderzoek waar dit project onder valt is een onderzoek naar emoties in zeventiende-eeuwse toneelstukken vertaald uit het Spaans. In dit project wordt data geëxtraheert uit een reeds bestaande dataset: [het Historic Embodied Emotions Model (HEEM)](https://github.com/NLeSC/HEEM-dataset). Deze dataset is ontwikkeld aan de VU door het emotie-expertisecentrum ACCESS (o.b.v. Inger Leemans). De ontwikkelaars hebben via machine learning emoties gelabeld voor 278 zeventiende-eeuwse en achttiende-eeuwse toneelstukken, waarvan 9 van Spaanse origine zijn. 
De data-extractie in dit project dient de vergelijking van een paar specifieke genres van toneel: 
- Spaans drama
- Senecaans-Scaligeriaans drama
- Vondels toneel
- Gruwel- en Spektakeltoneel

De code in dit project voert drie verschillende analyses uit voor geselecteerde toneelstukken uit de HEEM-dataset: 
1. Per tekst en genre wordt in een csv-bestand uitgesplitst hoe vaak welke concepttypes, emotietypes, emotieclusters, lichaamsdelen en sentimenten voorkomen in aantallen, gecorrigeerd naar het aantal versregels.
2. Voor zes emoties wordt per genre geplot welke lichaamsdelen het sterkst tot uitdrukking komen.
3. Voor vier stukken wordt het emotionele verloop van een selectie personages gevisualiseerd op basis van positieve en negatieve emoties.

## Aan de slag

### Vereisten

Deze codebase is volledig geschreven in Python 3.7. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip d.m.v. de volgende instructie:

```
pip install -r requirements.txt
```

### Gebruik

De resultaten kunnen opnieuw gegenereerd worden door aanroepen van:

```
python main.py
```

Het programma zal je vragen welke van de drie analyses je op de dataset uit wil voeren. De resultaten worden opgeslagen in ./results.

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **emotion_references.py**: bevat de code voor de analyse van emotiereferenties per tekst en per genre
- **embodied_emotions.py**: bevat de code voor het plotten van de gegevens over belichaming van emoties per genre
- **sentiment_visualisation.py**: bevat de code voor de visualisatie van het emotionele verloop in een toneelstuk
- **/data**: bevat geselecteerde bestanden uit de HEEM-dataset
- **/results**: bevat alle resultaten van dit project
- **/help_methods**: bevat functies die de benodigd zijn bij verschillende programma's

### Note

In de HEEM-dataset is voor de werken van Coster één file ('cost001rako01_01.xml') die de annotaties van meerdere toneelstukken van Coster omvat. Met behulp van de functie split_coster() (klik [hier](https://github.com/SanneHoeken/HEEM-Data-Extractions/blob/master/help_methods/split_coster.py) voor de implementatiedetails) zijn uit deze file de annotaties van vier toneelstukken geëxtraheert en opgeslagen als losse files. Het gaat om de stukken Ithys, Iphigenia, Isabella and Polyxena; opgeslagen in de datafolder als respectievelijk 'cost001rako01_ithys.xml', 'cost001rako01_iphigenia.xml', 'cost001rako01_isabella.xml' en 'cost001rako01_polyxena.xml'. 

## License
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License (http://creativecommons.org/licenses/by-sa/4.0/).

## Referenties
J.M. van der Zwaan, I. Leemans, E. Kuijpers, and I. Maks. HEEM, a Complex Model for Mining Emotions in Historical Text. 11th IEEE International Conference on eScience, 2015 10.1109/eScience.2015.18