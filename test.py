from configparser import ConfigParser
filename='config.ini'
parser = ConfigParser()
parser.read(filename, encoding="utf-8")
section = "api"
db = {}
if parser.has_section(section):
    items = parser.items(section)
    print(items)