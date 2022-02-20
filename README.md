# desktop-browser-automation

Little python script for open multiple tabs and play the youtube musics you want to start your day. Its customizable with default urls and command-line options.

### Install

```
pip3 install -r requirements.txt
```

### Usage

```
# simple usage example
python3 index.py -a https://www.google.com/search?q=Answer+to+the+Ultimate+Question+of+Life%2C+the+Universe%2C+and+Everything
python3 index.py -s https://www.youtube.com/watch?v=dQw4w9WgXcQ
python3 index.py --all
```

### Arguments

add url :`-a or --add <url>`

add song: `-s or --song <url>`

remove: ` -r or --remove <index> (index visible form list)`

open: ` -o or --open`

play: `-p or --play`

open and play: `-d or --all`

list: `-l or --list`

help: `-h or --help`
