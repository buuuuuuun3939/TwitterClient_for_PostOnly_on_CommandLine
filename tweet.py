import sys
from requests_oauthlib import OAuth1Session

CK = ""
CS = ""
AT = ""
ATS = ""
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/update.json"

print("Please input your tweet. If you want to exit, please input \"Ctrl + C\".")

try:
    tweet = input(">> " )
except KeyboardInterrupt:
    print("exit")
    sys.exit(0)

print("*****************************************")

try:
    params = {"status" : tweet}
    res = twitter.post(url, params = params)
    if res.status_code == 200:
        print("ツイートしました。")
except:
    print("ツイートできませんでした。")
    print(res.status_code)
