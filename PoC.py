#!/usr/bin/env python
import json
import bs4

from scraping_tools import req_and_unescape, enrich_data, dict_from_html_tablerow

OVERVIEW_URL = "https://www.parlament.gv.at/PAKT/JMAB/"

if __name__ == "__main__":
    plaintxt = req_and_unescape(OVERVIEW_URL)
    soup = bs4.BeautifulSoup(plaintxt, features="lxml")

    # get big table
    table = soup.find("table", {"class": "filter tabelle table-responsive table-mobile-inline"})
    rows = table.find_all("tr")

    # print some rows
    # first row is just header
    results = []
    for i in rows[1:5]:
        current = enrich_data(dict_from_html_tablerow(i))
        print(json.dumps(current, ensure_ascii=False))

        results.append(current)

    with open("data/results.json", 'w', encoding="utf-8") as jsonfile:
        json.dump(results, jsonfile, ensure_ascii=False)
