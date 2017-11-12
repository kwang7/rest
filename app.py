import urllib2, json, os
from flask import Flask, render_template, flash 


app = Flask(__name__)
app.secret_key = os.urandom(32) #32 bits of random data as a string
    
@app.route("/")
def nasa():

    '''
    coolStuff = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=jLVNWeyJx4FB8wdTZZhdUK9qcSEmdSKynyIAaTVF')
    print coolStuff.geturl()
    print "----------------"
    print  coolStuff.info()
    #print coolStuff.read()
    read = coolStuff.read()
    space = json.loads(read)
    '''
    #------------------------------------------------------------

    stuff = urllib2.urlopen('https://api.foursquare.com/v2/venues/4ae6363ef964a520aba521e3/events?&client_id=G3NQIBYY5BBHHOSYUZNWGDOFAKLFBSCEVZTUC0ER0KUA4JPQ&client_secret=NOVKQLZI5XSB3NQECVEFWCDIZK3OT0TUOU5IAP0IHMSKXHP1&v=20171112')
    #print stuff.info()
    reid = stuff.read()
    #print reid
    wow = json.loads(reid)
    #holey moley
    print wow.get('response').get('events').get('items')
    print "---------------------33-345435435-----------23532523--32523-----------------------------"
    for key in wow.get('response').get('events').get('items'):
        print key

        
        
        #website for show
        stri = '<a href =' + key.get('url') + '</a>'
        flash(stri) 

        #icon
        
        #api provides outdated link for icon
        #pic = key.get('categories')[0].get('icon').get('prefix') + '64' + key.get('categories')[0].get('icon').get('suffix')

        #correct link
        pic = 'https://foursquare.com/img/categories/arts_entertainment/musicvenue_64.png'
        stri = '<img src ="' + pic + '">'
        flash(stri)
        
        #name of artist
        stri = key.get('name')
        flash(stri)

        #category
        stri = 'Category: ' + key.get('categories')[0].get('pluralName')
        flash(stri)

        #timezone
        stri= 'Time Zone: ' + key.get('timeZone')
        flash(stri)

        #check ins 
        stri = 'Check-Ins: ' + str(key.get('stats').get('checkinsCount'))
        flash(stri)
        
        #people here now 
        stri = 'Here Now: ' + str(key.get('hereNow').get('count'))
        flash(stri)
        flash('\n')
        print '-------------------------------------'
    return render_template('cool.html', summary = wow.get('response').get('events').get('summary'), pic = pic )





if __name__ == "__main__":
    app.debug = True
    app.run()
