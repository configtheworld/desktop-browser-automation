from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep, ctime
from collections import namedtuple
from threading import Thread
from os.path import isfile
import csv
import aaargh


app = aaargh.App(description="desktop-browser-automation")

# Application level arguments:
app.arg('--name', help="Name of the person to greet", default="stranger")

# Application level defaults:
app.defaults(name="visitor")  # overrides "stranger"


@app.cmd
def hello(name):  # application level "name" argument is always passed
    print("Hello, world!")


@app.cmd(name="hi", help="Say hi")  # override subcommand name
@app.cmd_arg('-r', '--repeat', type=int, default=1, help="How many times?")
def say_hi(name, repeat):  # both application and subcommand args
    for i in range(repeat):
        print("Hi, %s!" % name)


@app.cmd
# overrides "visitor" for this command only
@app.cmd_defaults(name="my friend")
def greetings(name):
    print("Greetings, %s." % name)


@app.cmd(alias='bye')  # Allow "bye" aswell as goodbye
def goodbye(name):
    print("Goodbye, cruel world!")


class BrowserAutomation ():
    def __init__(self):
        # Create a headless browser
        opts = Options()
        opts.add_argument("--headless")
        self.browser = Firefox(options=opts)
        self.browser.get("https://github.com/configtheworld")

        # States
        self.open = []
        self.play = []
        self.start()

    def start(self):
        app.run()


ba = BrowserAutomation()
