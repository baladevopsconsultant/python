import json

try:
    commands={}
    with open('hostname.txt') as fh:
        for line in fh:
            heading, description=line.strip().split(':')
#        print("%s: %s" % (heading, description))
            commands[heading]=description.strip()
        print(json.dumps(commands, indent=2, sort_keys=True))
except ValueError:
    pass

