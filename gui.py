from selenium import webdriver
import math
import os

isopen = 0
def init():
    global isopen
    if isopen == False:
        global driver
        driver = webdriver.Chrome()
        driver.get('file://' + os.getcwd() + "/gui/indexx.html")
        isopen = True


def updateGUI(emote_val, emote, genre):
    init()
    htmlfile = open('./gui/indexx.html', 'w')
    htmltext = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Music For Your Mood</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/animate.min.css" rel="stylesheet">
    <link href="css/main.css" rel="stylesheet">
    <link id="css-preset" href="css/presets/preset1.css" rel="stylesheet">
    <link href="css/responsive.css" rel="stylesheet">
    
    <!--[if lt IE 9]>
    <script src="js/html5shiv.js"></script>
    <script src="js/respond.min.js"></script>
    <![endif]-->
    
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700' rel='stylesheet' type='text/css'>
    <link rel="shortcut icon" href="images/favicon.ico">
    </head><!--/head-->
    
    <body>
    
    
    <header id="home">
    <div id="home-slider" class="carousel slide carousel-fade" data-ride="carousel">
    <div class="carousel-inner">
    <div class="item active" style="background-image: url(images/slider/1.png); background-position: center; background-size: cover">
    <div class="caption">
    <h1 class="animated fadeInLeftBig">You're <span>""" + str(math.trunc(emote_val * 100)) + """%</span> """ + emote + """</h1>
    <p class="animated fadeInRightBig">We're playing some """ + genre + """</p>
    </div>
    </div>
    </div>
    
    <script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript" src="js/bootstrap.min.js"></script>
    <script type="text/javascript" src="js/main.js"></script>
    </body>
    </html>
    """
    htmlfile.write(htmltext)
    htmlfile.close()
    global driver
    driver.get('file://' + os.getcwd() + '/gui/indexx.html')
