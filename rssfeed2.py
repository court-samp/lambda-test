import feedparser
import boto3
import re


sns = boto3.client('sns')
news_url = {"aws" : "https://aws.amazon.com/about-aws/whats-new/recent/feed/"}
keyword = "aurora"
entry_list = []

def parseRSS(rss_url):
    return feedparser.parse(rss_url)

def get_entries(rss_url):
    feed = parseRSS(rss_url)
    for entry in feed.entries:
        for tag in entry.tags:
            new = str(tag.values())
            if re.search("%s" % keyword, new):
                entry_list.append(entry['title'])
                entry_list.append("NEWLINE")
                entry_list.append(entry['summary'])
                entry_list.append("NEWLINE")
                entry_list.append(entry['link'])
                entry_list.append("NEWLINE")
                entry_list.append(entry['published'])
                entry_list.append("DBL_NEWLINE")   
    return entry_list

def sendUpdate(Message):
    response = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:157171802921:TestTopic',
        Message = clean_entries(Message)
    )
    return response

def clean_entries(data):
    text = str(data)
    #remove http tags from entries, subbing whitespace for tags
    clean = re.compile(r'<[^>]+>')
    new_text = clean.sub("", text)

    #adding line breaks between entry posts
    newer_text = new_text.replace('DBL_NEWLINE' , '\n, \n')
    newest_text = newer_text.replace('NEWLINE', '\n')
    #final_text = newest_text.replace("','", '')
    print(newest_text)
    return newest_text


for key, url in news_url.items():
    get_entries(url)
    
sendUpdate(entry_list)

