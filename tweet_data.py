import os, sys, re, getopt
import traceback

if sys.version_info[0] < 3:
    raise Exception("Python 2.x is not supported. Please upgrade to 3.x")

import GetOldTweets3 as got

try:
    tweetCriteria = got.manager.TweetCriteria()
    outputFileName = "./tweet.csv"
    debug = False
    tweetCriteria.querySearch = "#CycloneFani"
    tweetCriteria.since="2017-01-01"
    tweetCriteria.until="2019-06-01"
    tweetCriteria.maxTweets = 300

    outputFile = open(outputFileName, "w+", encoding="utf8")
    outputFile.write('date,username,to,replies,retweets,favorites,text,geo,mentions,hashtags,id,permalink\n')
    
    cnt = 0
    def recieveBuffer(tweets):
        global cnt
        for t in tweets:
            data = [t.date.strftime("%Y-%m-%d %H:%M:%S"),
                t.username,
                t.to or '',
                t.replies,
                t.retweets,
                t.favorites,
                '"'+t.text.replace('"','""')+'"',
                t.geo,
                t.mentions,
                t.hashtags,
                t.id,
                t.permalink]
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
