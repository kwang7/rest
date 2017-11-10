import urllib2, json
from flask import Flask, render_template

app = Flask(__name__)

    
@app.route("/")
def nasa():
    coolStuff = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=jLVNWeyJx4FB8wdTZZhdUK9qcSEmdSKynyIAaTVF')
    print coolStuff.geturl()
    print "----------------"
    pic = coolStuff.info()
    #print coolStuff.read()
    read = coolStuff.read()
    space = json.loads(read)
    return render_template('cool.html', space = space['explanation'], pic = space['hdurl'])


if __name__ == "__main__":
    app.debug = True
    app.run()
