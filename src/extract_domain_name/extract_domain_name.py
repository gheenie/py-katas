import re

def extract_domain_name(url):
	match = re.search(r'\w+.com', url)

	if match == None: return ''

	return match.group()
