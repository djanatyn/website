from lxml import etree
from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('./templates'))

tree = etree.parse("data.xml")
root = tree.getroot()

template = env.get_template('entry.html')
entry_num = 100
for entry in root:
    fh = open("%d.html" % entry_num,'w')
    fh.write(template.render(
            title = entry[0].text,
            date = entry[1].text,
            text = entry[2].text))
    entry_num += 1
