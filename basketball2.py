# Parse Basketball Reference

import re
from urllib.request import urlopen
player_file = open('players_sg.txt', 'r')

players = player_file.readlines()

for n in range(0, len(players)):

	player = players[n].strip()
	player_name = []
	player_name = player.split(" ")
	first_name = player_name[0].replace(".","")
	last_name = player_name[1].strip(',')

	url = ("http://www.basketball-reference.com/players/" + last_name[0:1] + "/" + last_name[0:5] + first_name[0:2] + "01.html").lower()
	print(url)
	f = urlopen(url)
	player_html = f.read().decode("utf-8")
	html_list = player_html.split('\n')

	games = 0
	fgp = 0
	threepm = 0
	ftp = 0
	reb = 0
	ast = 0
	stl = 0
	blk = 0
	tov = 0
	pts = 0
	
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
	
	if games == 0:
		url = ("http://www.basketball-reference.com/players/" + last_name[0:1] + "/" + last_name[0:5] + first_name[0:2] + "02.html").lower()
		print(url)
		f = urlopen(url)
		player_html = f.read().decode("utf-8")
		html_list = player_html.split('\n')
		
		for i in range(0, len(html_list)):
			line = html_list[i]
			
			if "id=\"per_game.2012" in line:
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
	
	if games == 0:
		url = ("http://www.basketball-reference.com/players/" + last_name[0:1] + "/" + last_name[0:5] + first_name[0:2] + "02.html").lower()
		print(url)
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
		
	fantasy_csv = open('fantasy_sg.csv', 'a')
	fantasy_csv.write("\"" + str(player) + "\",\"" + str(games) + "\",\"" + str(fgp) + "\",\""  + str(threepm) + "\",\"" + str(ftp) + "\",\""  + str(reb) + "\",\""  + str(ast) + "\",\""  + str(stl) + "\",\""  + str(blk) + "\",\""  + str(tov) + "\",\"" + str(pts) + "\"\n")