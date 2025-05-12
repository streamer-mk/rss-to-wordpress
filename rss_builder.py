
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
from datetime import datetime

def build_rss(articles):
    rss = Element("rss", version="2.0")
    channel = SubElement(rss, "channel")

    title = SubElement(channel, "title")
    title.text = "Вести од Македонија - vesti.mk"

    link = SubElement(channel, "link")
    link.text = "https://www.vesti.mk/category/makedonija"

    description = SubElement(channel, "description")
    description.text = "Најнови вести од категоријата Македонија"

    pubDate = SubElement(channel, "pubDate")
    pubDate.text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")

    for article in articles:
        item = SubElement(channel, "item")

        item_title = SubElement(item, "title")
        item_title.text = article["title"]

        item_link = SubElement(item, "link")
        item_link.text = article["link"]

        item_description = SubElement(item, "description")
        item_description.text = article["description"]

        item_pubDate = SubElement(item, "pubDate")
        item_pubDate.text = article["pubDate"]

    rough_string = tostring(rss, "utf-8")
    reparsed = parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
