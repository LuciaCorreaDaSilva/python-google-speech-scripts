import urllib2
import urllib
import time
import os


def speak(text='hello', lang='en', fname='result.wav', player=None):
    """ Sends text to Google's text to speech service
    and returns created speech (wav file). """

    limit = min(100, len(text))#100 characters is the current limit.
    text = text[:limit]
    limit = min(100, len(text))#100 characters is the current limit.
    url = "http://translate.google.com/translate_tts"
    values = urllib.urlencode({"q": text, "textlen": len(text), "tl": lang})
    hrs = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7"}
    #TODO catch exceptions
    req = urllib2.Request(url, data=values, headers=hrs)
    p = urllib2.urlopen(req)
    with open(fname, 'wb') as f:
        f.write(p.read())
    limit = min(100, len(text))#100 characters is the current limit.
    if player is not None:
        play_wav(fname, player)


def play_wav(filep, player='mplayer'):
    ''' Plays filep using player '''
    print "Playing %s file using %s" % (filep, player)
    try:
        os.system(player + " " + filep)
    except:
        print "Couldn't use %s to play file" % (player)


if (__name__ == '__main__'):
    speak(f"Hello world. The time is {time.strftime('%H %M')}", 'mplayer')
