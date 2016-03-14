import requests

repos = requests.get('https://api.github.com/users/briancly/repos')
val = 0
languages = {}

for repo in repos.json():
	resp = requests.get('https://api.github.com/repos/briancly/' + repo['name'] + '/languages')
	for language in resp.json():
		val += resp.json()[language]
		if language in languages:
			languages[language] += resp.json()[language]
		else:
			languages[language] = resp.json()[language]

for key,value in languages.items():
	print key + ': ' + str(100*value/val) + '%'