from lxml import etree
from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('./templates'))

tree = etree.parse("data.xml")
root = tree.getroot()

template = env.get_template('entry.html')
entry_num = 100
for entry in root:
    fh = open("./output/%d.html" % entry_num,'w')
    text = entry[2].text
    fh.write(template.render(
            title = entry[0].text,
            date = entry[1].text,
            text = text.replace('\n','</p><p>')))
    entry_num += 1
