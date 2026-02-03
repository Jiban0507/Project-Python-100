import requests
import xml.etree.ElementTree as ET

# Primary RSS feed (CNN)
RSS_URL = "https://rss.cnn.com/rss/edition.rss"
# Backup RSS feed (BBC)
FALLBACK_URL = "http://feeds.bbci.co.uk/news/rss.xml"

def fetch_rss(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.content

def parse_rss(xml_data):
    root = ET.fromstring(xml_data)
    channel = root.find("channel")
    feed_title = channel.find("title").text

    items = []
    for item in channel.findall("item"):
        title = item.find("title").text
        link = item.find("link").text
        description = item.find("description").text
        pub_date = item.find("pubDate").text

        items.append({
            "title": title,
            "link": link,
            "description": description,
            "pub_date": pub_date
        })

    return feed_title, items

def display_feed(feed_title, items):
    print(f"\n📰 {feed_title}\n" + "=" * 50)
    for i, item in enumerate(items, start=1):
        print(f"\n{i}. {item['title']}")
        print(f"📅 {item['pub_date']}")
        print(f"🔗 {item['link']}")
        print(f"📝 {item['description'][:150]}...")

def main():
    try:
        xml_data = fetch_rss(RSS_URL)
    except Exception as e:
        print("⚠️ CNN feed failed, switching to BBC...")
        xml_data = fetch_rss(FALLBACK_URL)

    feed_title, items = parse_rss(xml_data)
    display_feed(feed_title, items)

if __name__ == "__main__":
    main()