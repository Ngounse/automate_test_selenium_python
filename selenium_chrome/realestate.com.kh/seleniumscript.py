from requests_html import HTMLSession
import json
import time

class Rewiews:
  def __init__(self, asin) -> None:
    self.asin = asin
    self.session = HTMLSession()
    self.headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    self.url = f'https://www.amazon.com/product-reviews/{self.asin}/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&filterByStar=five_star&reviewerType=all_reviews&sortBy=recent&pageNumber='
      
  def pagination(self, page):
    r = self.session.get(self.url + str(page))
    print ("r:::",r.html.find('div[data-hook=review]'))
    if not r.html.find('div[data-hook=review]'):
      return False 
    else:
      return r.html.find('div[data-hook=review]')
    
  def parse(self, reviews):
    total = []
    for review in reviews:
      title = review.find('a[data-hook=review-title', first=True).text
      rating = review.find('i[data-hook=review-rating span', first=True).text
      body = review.find('span[data-hook=review-body] span', first=True).text.replace('\n','').strip()
      
      data = {
        'title': title,
        'rating': rating,
        'body': body[:100],
      }
      print ("data::", data)
      total.append(data)
    return total
  
  def save(self, result ):
    with open(self.asin + '-review.json', 'w') as f:
      json.dump(result, f)
  
  
if __name__ == '__main__':
  amz = Rewiews('B0779B2K8B')
  result = []
  for x in range(1,5):
    print('getting page ',x)
    time.sleep(0.3)
    reviews = amz.pagination(x)
    if reviews is not False:
      result.append(amz.parse(reviews))
      # print("::::::",amz.parse(reviews))
      print("review::",reviews)
    else:
      print("no more page")
      break
    
  print(result)
  amz.save(result)