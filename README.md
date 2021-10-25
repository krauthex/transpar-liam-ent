# transpar[liam]ent

This is a WIP; ideally, it will provide a tool to properly scrape the contents of the "Parlamentarische Anfragen" website of the Austrian parliament (see [here](https://www.parlament.gv.at/PAKT/JMAB/)).

The reason behind it is that the website itself is relatively annoying to use, and provides very poor search functionality, i.e. no full-text search nor a direct search for inquierer and receiver.

Currently, this is merely a collection of very rudimentary functions.

## Run the PoC
After installing the dependencies (`BeautifulSoup4`, `requests`, `lxml`), you can run the PoC with:

```
$ ./PoC.py
date: 25.10.2021
inquiry: {'desc': 'Schriftliche Anfrage der Abgeordneten Douglas   Hoyos-Trauttmansdorff, Kolleginnen und Kollegen an die   Bundesministerin für Landesverteidigung betreffend    Zukunft der Hackher-Kaserne', 'from': 'Eingebracht von:    Douglas Hoyos-Trauttmansdorff', 'to': 'Eingebracht an:    Mag. Klaudia Tanner Regierungsmitglied     Bundesministerium für Landesverteidigung', 'refs': [{'url': 'https://www.parlament.gv.at/PAKT/VHG/XXVII/J/J_08414/imfname_1007132.pdf', 'ref': 'Anfrage (gescanntes Original) / PDF, 648 KB'}, {'url': 'https://www.parlament.gv.at/PAKT/VHG/XXVII/J/J_08414/fname_1007151.pdf', 'ref': 'Anfrage (elektr. übermittelte Version) / PDF, 85 KB'}, {'url': 'https://www.parlament.gv.at/PAKT/VHG/XXVII/J/J_08414/fnameorig_1007151.html', 'ref': 'HTML, 85 KB'}]}
number: 8414/J
progress: has not been answered
relative url: /PAKT/VHG/XXVII/J/J_08414/index.shtml
title: Zukunft der Hackher-Kaserne (BMLV) - Frist für die Beantwortung 25.12.2021
url: https://www.parlament.gv.at/PAKT/VHG/XXVII/J/J_08414/index.shtml
```