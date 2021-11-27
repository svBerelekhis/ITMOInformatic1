import yaml, json

inputfile = open('input.json', 'r', encoding="utf-8")
outputfile = open('output.yaml', 'w')
outputfile.write(yaml.dump(json.load(inputfile)))