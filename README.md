This is a python file for fetching the information of WWDC session videos.

Before running, please use `pip` to install `BeautifulSoup4` and `reqeusts`:
```
sudo pip install BeautifulSoup4
sudo pip install requests
```

And you can use the following commands:
```sh
# This will fetch the informations about the sessions of WWDC1028
python crawler.py

# You can input the year whatever you want.
python crawler.py year
```

After running `crawler.py`, you will get two file:
- WWDC[year]_Session_title.md
- WWDC[year]_session_content.md 


