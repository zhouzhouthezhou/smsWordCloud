from xml.dom import minidom
from wordcloud import WordCloud, STOPWORDS 

import pandas as pd
import matplotlib.pyplot as plt 

import pickle
import sys
import os.path

def parseXML(target):
    doc = minidom.parse(target)
    sms = doc.getElementsByTagName('sms')

    texts = list()

    for text in sms:
        address = text.attributes['address'].value
        date = text.attributes['date'].value
        body = text.attributes['body'].value
        texts.append((address, date, body))

    df = pd.DataFrame(texts, columns =['Number', 'Date', 'Body']) 
    df.to_pickle(target.split(".")[0] + '.pkl')
    return df

def generateWordCloud(df, name):
    print("Generating word cloud for", name)

    stopwords = set(STOPWORDS) 
    
    text = " ".join(word for word in df.Body)
    
    wordcloud = WordCloud(width = 800, height = 800, 
                    background_color ='white', 
                    stopwords = stopwords, 
                    min_font_size = 10).generate(text) 

    wordcloud.to_file(name + '.png')
    print("Word cloud saved as", name + ".png")
  
    #plt.figure(figsize = (8, 8), facecolor = None) 
    #plt.imshow(wordcloud) 
    #plt.axis("off") 
    #plt.tight_layout(pad = 0) 
  
    #plt.show() 

def main():
    filename = sys.argv[1].split('.')[0]
    sender = sys.argv[2]
    receiver = sys.argv[3]

    if os.path.isfile(filename + '.pkl'):
        print('Pickle found')
        log = pd.read_pickle(filename + '.pkl')
    elif os.path.isfile(filename + '.xml'):
        print('No pickle found, falling back to xml, this may take a while')
        log = parseXML(filename + '.xml')
    else:
        print(filename, "cannot be found as an xml or pkl file.")
        return

    generateWordCloud(log[log['Number'].str.contains("\+")], receiver)
    generateWordCloud(log[~log['Number'].str.contains("\+")], sender)

if __name__ == "__main__":
    main()
