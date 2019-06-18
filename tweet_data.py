import os, sys, re, getopt
import traceback

if sys.version_info[0] < 3:
    raise Exception("Python 2.x is not supported. Please upgrade to 3.x")

import GetOldTweets3 as got

try:
    tweetCriteria = got.manager.TweetCriteria()
    outputFileName = "./tweet.csv"
    debug = False
    tweetCriteria.querySearch = "#KeralaFloods"
    tweetCriteria.since="2018-08-07"
    tweetCriteria.until="2018-08-17"
    tweetCriteria.maxTweets = 20000
    tweetCriteria.lang = "en"
    

    outputFile = open(outputFileName, "w+", encoding="utf8")
    outputFile.write('date,username,retweets,text,mentions,hashtags\n')
    
    cnt = 0
    def recieveBuffer(tweets):
        global cnt
        for t in tweets:
            if t.text != '':
                data = [t.date.strftime("%Y-%m-%d %H:%M:%S"),
                    t.username,
                    t.retweets,
                    '"'+t.text.replace('"','""')+'"',
                    t.mentions,
                    t.hashtags]
                data[:] = [i if isinstance(i, str) else str(i) for i in data]
                outputFile.write(','.join(data) + '\n')

        outputFile.flush()
        cnt += len(tweets)

        if sys.stdout.isatty():
            print("\rSaved %i"%cnt, end='', flush=True)
        else:
            print(cnt, end=' ', flush=True)

    print("Downloading tweets...")
    got.manager.TweetManager.getTweets(tweetCriteria, recieveBuffer, debug=debug)

except KeyboardInterrupt:
    print("\r\nInterrupted.\r\n")
except Exception as err:
    print(traceback.format_exc())
    print(str(err))
finally:
    if "outputFile" in locals():
        outputFile.close()
        print()
        print('Done. Output file generated "%s".' % outputFileName)
