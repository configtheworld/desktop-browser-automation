import webbrowser
import pyautogui
import getopt
import sys
import csv
import itertools
import threading
import time

# csv file name
filename = "urls.csv"

# initializing the titles and rows list
fields = ["Index", "Url", "Operation"]
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

# create argument list
argumentList = sys.argv[1:]

# Options
options = "a:r:s:oplhd"
# Long options
long_options = ["add", "remove", "song", "open", "play", "list", "help", "all"]

done = False


class BrowserAutomation ():
    def __init__(self):
        # no need init
        pass

    def add(self, url):
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(
                [[len(rows)+1, url, "o"]])
            print("=> Added to list:", url)
        self.refresh_list()

    def add_song(self, url):
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(
                [[len(rows)+1, url, "p"]])
            print("=> Added to list:", url)
        self.refresh_list()

    def remove(self, number):
        with open(filename, "w")as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            for row in rows:
                if number != row[0]:
                    csvwriter.writerow(row)
            print("=> ", number, " removed to list!")
        self.refresh_list()

    def open(self):
        try:
            print(currentValue, "=> Here is your favorite Tabs")
            t = threading.Thread(target=self.animation)
            t.start()  # prevent multiple musics playing same time
            for row in rows:
                if row[2] == "o":
                    webbrowser.open_new_tab(row[1])

        except webbrowser.Error as e:
            print(e)

    def play(self):
        try:
            print(currentValue, "Music playing ")
            t = threading.Thread(target=self.animation)
            t.start()
            play_flag = False  # prevent multiple musics playing same time
            for row in rows:
                if row[2] == "p" and play_flag != True:
                    webbrowser.open_new_tab(row[1])
                    time.sleep(7)
                    pyautogui.press("space")
                    play_flag = True

        except webbrowser.Error as e:
            print(e)

    def open_and_play(self):
        try:
            print(currentValue, "Opening and Playing ...")
            t = threading.Thread(target=self.animation)
            t.start()
            play_flag = False  # prevent multiple musics playing same time
            for row in rows:
                if row[2] == "o":
                    webbrowser.open_new_tab(row[1])
                elif row[2] == "p" and play_flag != True:
                    webbrowser.open_new_tab(row[1])
                    time.sleep(7)

                    pyautogui.press("space")
                    play_flag = True

        except webbrowser.Error as e:
            print(e)

    def show_list(self, rows):
        print("-Your URL List-")
        for row in rows:
            print(row[0], "=>",  "*open* " if row[2]
                  == "o" else "*play* ", row[1])

    def refresh_list(self):
        with open(filename, 'r') as csvfile:
            rows_temp = []
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                rows_temp.append(row)
            self.show_list(rows=rows_temp[1:])

    def animation(self):
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone!     ')


# create object
ba = BrowserAutomation()


try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-a", "--add"):
            # add url to csv
            ba.add(currentValue)
        elif currentArgument in ("-s", "--song"):
            # add song
            ba.add_song(currentValue)
        elif currentArgument in ("-r", "--remove"):
            # remove url from csv
            ba.remove(currentValue)
        elif currentArgument in ("-o", "--open"):
            # open tabs from csv
            ba.open()
        elif currentArgument in ("-p", "--play"):
            # play url
            ba.play()
        elif currentArgument in ("-d", "--all"):
            # open tabs and play url
            ba.open_and_play()
        elif currentArgument in ("-l", "--list"):
            # show csv list
            ba.show_list(rows=rows)
        elif currentArgument in ("-h", "--help"):
            print("Available Arguments: \n-a <url_for_open_tab>             || -all <url_for_open_tab>,\n-s <url_for_play_youtube>         || -song <url_for_play_youtube>,\n-r <list_index_for_remove_item>   || -remove <list_index_for_remove_item>,\n-o                                || -open #opens tabs,\n-p                                || -play #plays one youtube song ,\n-d                                || -all #opens one youtube link and all tabs,\n-l                                || --list #shows the list")

    done = True

except getopt.error as err:
    # output error, and return with an error code
    print(str(err))
