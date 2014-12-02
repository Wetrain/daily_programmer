from bs4 import BeautifulSoup as bs4
import requests

def get_comments(url):
    html = requests.get("https://plus.googleapis.com/u/0/_/widget/render/comments?first_party_property=YOUTUBE&href="+url)
    soup = bs4(html.text)
    return  [comment.string for comment in soup.findAll('div', class_='Ct')]

def negative_sentiment(comments):
    count = 0
    negative_words = ['hate','hated','dislike','disliked','awful','terrible','bad','painful','worst', 'suck', 'rubbish', 'sad', 'sodding']
    for comment in comments:
        if comment == None:
            continue
        else:
            for word in comment.split(' '):
                if word in negative_words:
                    count += 1
    return count

def positive_sentiment(comments):
    count = 0
    positive_words = ['love','loved','like','liked','awesome','amazing','good','great','excellent', 'brilliant', 'cool']
    for comment in comments:
        if comment == None:
            continue
        else:
            for word in comment.split(' '):
                if word in positive_words:
                    count += 1
    return count

def main():    
    url = raw_input("enter youtube url \n")

    if(url):
        comments = get_comments(url)
        positive_score = positive_sentiment(comments)
        negative_score = negative_sentiment(comments)
        total_score = positive_score + negative_score

        if(positive_score > negative_score):
            print("This video is generally positive {0} positive / {1} total hits").format(positive_score, total_score)
        elif(negative_score > positive_score):
            print("This video is generally negative {0} negative / {1} total hits").format(negative_score, total_score)
        else:
            print("This video is mutual {0} positive {1} negative").format(positive_score, negative_score)
    else:
        print("No url supplied")


if __name__ == "__main__":
    main()    

