import html
from typing import Any, Union

import bs4
import requests as req

## custom types
Data = dict[str, Any]
ReferenceList = list[Data]
InquiryData = dict[str, Union[str, ReferenceList]]
EnrichedData = dict[str, Union[Data, InquiryData]]

BASE_URL = "https://www.parlament.gv.at"


def req_and_unescape(url: str) -> str:
    """Get response content decoded as utf-8 and unescape html codes."""
    res = req.get(url)
    plain_html = res.content.decode("utf-8")
    return html.unescape(plain_html)


def clean_contents(raw_contents: bs4.element.Tag) -> str:
    """Clean html contents from '\r' and whitespaces and such."""
    def clean_str(_s: str) -> str:
        return _s.replace("\n", "").replace("\t", "")

    conts = raw_contents.contents
    if len(conts) == 1:
        content_string = conts[0].text.strip()
        return clean_str(content_string)

    # we apparently have to remove some nested tags in here
    for i, cont in enumerate(conts):
        if hasattr(cont, "text"):
            content_string = cont.text
            conts[i] = clean_str(content_string)
    return "".join(conts).strip()


def dict_from_html_tablerow(tablerow: bs4.element.Tag) -> Data:
    """Generate a dictionary from an html tablerow."""
    status_img = {
        "03.gif": "has not been answered",
        "05.gif": "has been answered"
    }

    raw_title, raw_number = tablerow.find_all("a", {"class": "table-mobile__title"})

    # TODO: type (J, or something else)
    data = {
        "rel_url": tablerow.find("div", {"class": "table-mobile__entry"})['data-arrow-url'],
        "date": clean_contents(tablerow.find("div", {"class": "table-mobile__date"})),
        "progress": status_img[tablerow.find("img")['src'].split("/")[-1]],
        "title": clean_contents(raw_title),
        "number": clean_contents(raw_number)
    }

    return data


def enrich_data(data: Data) -> EnrichedData:
    """Enrich the data."""
    enriched_data = {**data}
    enriched_data["url"] = f"{BASE_URL}{enriched_data['rel_url']}"
    enriched_data["inquiry"] = inquiry_scraper(enriched_data["url"])

    return enriched_data


def inquiry_scraper(url: str) -> InquiryData:
    """Scrape contents of an inquiry page like description, sender, receiver and file links."""
    plaintxt = req_and_unescape(url)
    soup = bs4.BeautifulSoup(plaintxt, features="lxml")
    info = soup.find("div", {"class": "c_2"})
    description, fro, to = info.find_all("p")

    def reference_builder(refs: list[bs4.element.Tag]) -> ReferenceList:
        """Builds a list of file names with hrefs."""
        inq_refs = []
        for a in refs:
            inq_refs.append({
                "url": f"{BASE_URL}{a['href']}",
                "ref": a.contents[1]
            })
        return inq_refs

    inq_data: dict[str, Any] = {
        "desc": clean_contents(description),
        "from": clean_contents(fro),
        "to": clean_contents(to),
        "refs": reference_builder(info.find("ul").find_all("a"))
    }

    return inq_data
