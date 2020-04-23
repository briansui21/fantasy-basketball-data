# Parse Basketball Reference

import re
from urllib.request import urlopen
player_file = open('players.txt')

player = input("Player Name: ")
player_name = []
player_name = player.split(" ")
first_name = player_name[0]
last_name = player_name[1]

url = ("http://www.basketball-reference.com/players/" + last_name[0:1] + "/" + last_name[0:5] + first_name[0:2] + "01.html").lower()
f = urlopen(url)
player_html = f.read().decode("utf-8")
html_list = player_html.split('\n')

for i in range(0, len(html_list)):
	line = html_list[i]
	if "id=\"per_game.2013" in line:
		games = re.split('<|>',html_list[i+6])[2]
		fgp = re.split('<|>',html_list[i+11])[2]
		threepm = re.split('<|>',html_list[i+12])[2]
		ftp = re.split('<|>',html_list[i+17])[2]
		reb = re.split('<|>',html_list[i+20])[2]
		ast = re.split('<|>',html_list[i+21])[2]
		stl = re.split('<|>',html_list[i+22])[2]
		blk = re.split('<|>',html_list[i+23])[2]
		tov = re.split('<|>',html_list[i+24])[2]
		pts = re.split('<|>',html_list[i+26])[2]

fantasy_csv = open('fantasy.csv', 'a')
fantasy_csv.write("\"" + player + "\",\"" + games + "\",\"" + fgp + "\",\""  + threepm + "\",\"" + ftp + "\",\""  + reb + "\",\""  + ast + "\",\""  + stl + "\",\""  + blk + "\",\""  + tov + "\",\"" + pts + "\"\n")