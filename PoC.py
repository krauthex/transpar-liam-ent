#!/usr/bin/env python
import bs4

from scraping_tools import req_and_unescape, enrich_data, dict_from_html_tr

OVERVIEW_URL = "https://www.parlament.gv.at/PAKT/JMAB/"

if __name__ == "__main__":
    plaintxt = req_and_unescape(OVERVIEW_URL)
    soup = bs4.BeautifulSoup(plaintxt, features="lxml")

    # get big table
    table = soup.find("table", {"class": "filter tabelle table-responsive table-mobile-inline"})
    rows = table.find_all("tr")

    # print some rows
    # first row is just header
    for i in rows[1:2]:
        for k, v in sorted(enrich_data(dict_from_html_tr(i)).items()):
            print(f"{k}: {v}")