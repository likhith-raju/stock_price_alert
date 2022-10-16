import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "4UQOMET7VODAEMYL"
NEWS_API_KEY = "40e92f1e11c74c9fb896aaf38db35f6f"

TWILIO_SID = "AC75a7f16e88fb920ff9da712bcd6433f5"
AUTH_TOKEN_TWILIO = "9927977eade3f8e56b1ca9db7bd1c989"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}


response = requests.get(STOCK_ENDPOINT,params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yester_data = data_list[0]
yester_closing_price = yester_data["4. close"]
print(yester_closing_price)


# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_close_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_close_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = abs(float(yester_closing_price) - float(day_before_yesterday_close_price))
print(diff)
# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = (diff/float(yester_closing_price))*100.0
print(percent_diff)
#If TODO4 percentage is greater than 5 then print("Get News").
if(percent_diff>5.0):
    news_params={
        "apiKey":NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,



    }
    news_response= requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()["articles"]
    print(articles)


    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
print(three_articles)




formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

client = Client(TWILIO_SID,AUTH_TOKEN_TWILIO)



for article in formatted_articles:
    messages = client.messages.create(
        body=article,
        from_="+19498064810",
        to="+917022303974"

    )


