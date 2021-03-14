import wolframalpha
import requests
def index(query):
    app_id='7HW7R4-YXEHPVTU65'
    client = wolframalpha.Client(app_id)
    res=client.query(query)
    answer=next(res.results).text
    return answer