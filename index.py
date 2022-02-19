import webbrowser
import getopt
import sys
import csv


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
options = "a:r:op:l"
# Long options
long_options = ["add", "remove", "open", "play", "list"]


class BrowserAutomation ():
    def __init__(self):
        # no need init
        pass

    def add(self, url):
        with open(filename, 'a') as csvfile:
            cvswriter = csv.writer(csvfile)
            cvswriter.writerows(
                [[len(rows)+1, url, "o"]])
            print("=> Added to list:", url)

    def remove(self, number):
        # with open(filename, 'w') as csvfile:
        #     cvswriter = csv.DictWriter(csvfile, fieldnames=fields)
        #     rows.remove(int(number))
        #     cvswriter.writeheader()
        #     cvswriter.writerows(rows)

        print(number, "=> Not Removed from list Yet")

    def open(self):
        print(currentValue, "=> Here is your favorite Tabs")
        for row in rows:
            if row[2] == "o":
                webbrowser.open_new_tab(row[1])

    def play(self):
        print(currentValue, "=> Playing")
        # TODO

    def show_list(self):
        print("-Your URL List-")
        for row in rows:
            print(row[0], "=>",  "*open* " if row[2]
                  == "o" else "*play* ", row[1])


ba = BrowserAutomation()


try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-a", "--add"):
            # add url to csv
            ba.add(currentValue)
        elif currentArgument in ("-r", "--remove"):
            # remove url from csv
            ba.remove(currentValue)
        elif currentArgument in ("-o", "--open"):
            # open tabs from csv
            ba.open()
        elif currentArgument in ("-p", "--play"):
            # play url
            ba.play()
        elif currentArgument in ("-l", "--list"):
            # show csv list
            ba.show_list()

except getopt.error as err:
    # output error, and return with an error code
    print(str(err))
