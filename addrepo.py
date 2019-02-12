""" addrepo.py
    Script to help people add repos to the list easily.
"""

import json

proj_data = {
    'name': input('Name of the repo: '),
    'link': input('Link of the repo: '),
    'page': input('Page of the project(blank if don\'t have): ')
}
template = "## List\n* [{}]({})".format(proj_data['name'], proj_data['link'])

data_raw = open('data/repo.json')
data = json.load(data_raw)
data_raw.close()
data.append(proj_data)
data_raw = open('data/repo.json', 'w')
data_raw.write(json.dumps(data, sort_keys=True, indent=2))
data_raw.close()

fr = open('docs/README.md').read()
fr = fr.replace('## List', template)
fw = open('docs/README.md', 'w')
fw.write(fr)
fw.close()
