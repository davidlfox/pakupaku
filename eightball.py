import http.client
import json
import urllib.parse

class EightBall:
    def __init__(self, question):
        self.question = question
    
    def getFortune(self):
        conn = http.client.HTTPSConnection("8ball.delegator.com")
        question = urllib.parse.quote(self.question)
        conn.request('GET', '/magic/JSON/' + question)
        
        response = conn.getresponse()
        fortune = json.loads(response.read())
        answer = fortune["magic"]["answer"]
        answerType = fortune["magic"]["type"]
        return f'the paku-paku\'s {answerType.lower()} response is: {answer.lower()}'
