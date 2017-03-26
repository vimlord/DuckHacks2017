from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math
import os

driver = 0
isopen = 0
guiopen = 0
inpandoratab = True

def init():
    global isopen
    if isopen == False:
        global driver
        driver = webdriver.Chrome()
        driver.get('http://www.pandora.com/')
        isopen = True
        global inpandoratab
        time.sleep(2.5)

def search(keyword):
    init()
    global inpandoratab
    if inpandoratab == False:
        driver.switch_to_window(driver.window_handles[0])
        time.sleep(2)
    driver.find_element_by_class_name('SearchField__placeholder').click()
    search_bar = driver.find_element_by_class_name('SearchField__input')
    search_bar.send_keys(keyword)
    time.sleep(1)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(2)

def updateGUI(emote_val, emote, genre):
    global guiopen
    if guiopen == False:
        newtab = driver.execute_script("window.open('');")
        #driver.execute_script("window.open('https://www.google.com');")
        driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + Keys.TAB)
        guiopen = True
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
    driver.switch_to_window(driver.window_handles[1])
    global inpandoratab
    inpandoratab = False
    driver.get('file://' + os.getcwd() + '/gui/indexx.html')
