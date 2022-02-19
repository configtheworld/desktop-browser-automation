# desktop-browser-automation

Little python script for open multiple tabs and play the youtube musics you want to start your day. Its customizable with default urls and command-line options.

### Usage

```bash
python3 index.py -a <url>
# > => Added to list: <url>

python3 index.py -l
# > -Your URL List-
# 1 => *open*  <url>
# 2 => *open*  <url2>
# 3 => *open*  <url3>

python3 index.py -o
#> => Here is your favorite Tabs
```

### Arguments

- add
  - -a or --add <url>
- remove
  - -r or --remove <index> (index visible form list)
- open
  - -o or --open
- play
  - -p or --play
- list
  - -l or --list
