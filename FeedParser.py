import requests
import json

def generate_response(prompt):
    url = 'http://localhost:11434/api/generate'
    data = {'model': 'llama3.2', 'prompt': prompt, 'stream': False}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json().get('response')
    else:
        raise Exception(f'Error {response.status_code}: {response.text}')
    
def parse_rss_feeds(rss_feeds):
    aggregated_data = {}

    for feed in rss_feeds:
        parser = feedparser.parse(feed['url'])
        for entry in parser.entries:
            title = entry.get('title', '')
            link = entry.get('link', '')
            description = entry.get('summary', '')

            if not aggregated_data.get(title):
                aggregated_data[title] = {'description': description, 'links': [link]}
            else:
                aggregated_data[title]['description'] += '\n' + description
                aggregated_data[title]['links'].append(link)

    return aggregated_data

def main():
    rss_feeds = [
        {'url': 'https://feeds.feedburner.com/TheHackersNews'},
        # Add more RSS feeds here
    ]

    aggregated_data = parse_rss_feeds(rss_feeds)
    json_file = open('aggregated.json', 'w')
    json.dump(aggregated_data, json_file)
    json_file.close()

if __name__ == '__main__':
    main()