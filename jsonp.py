import json
import yaml
import os

"""
-------------
JSON Publish
-------------

"""
def jsonstart(filepath,htp):
    """
    docstring
    """
    h.AddRes("HeyTranser",leastLang)
    h.AddRes("Hello,World!",leastLang)
    h.AddRes("Welcome!",leastLang)
    p=h.ReturnDict()
    for idi in p['Res']:
        del p['Res'][idi]['Item']['Tag']
        del p['Res'][idi]['Item']['TransTime']
        del p['Res'][idi]['Item']['IsClock']
        del p['Res'][idi]['Item']['Checker']
        del p['Res'][idi]['Item']['CheckTime']
        #del p['Res'][idi]['Item']['TransResource']
        p['Res'][idi]['Item']['TransResource']=p['Res'][idi]['Item']['TransResource']

    readydict={
    'Resource':p['Res'],
    'Contributor':p['ProjectConfig']['Contributor'],
    'Author':p['ProjectConfig']['Author'],
    'Member':p['ProjectConfig']['Member'],
    'ProjectName':p['ProjectConfig']['ProjectName']
        }

    generate_json =json.dumps(readydict,sort_keys=False,indent=4,separators=(',',': '))

    print(readydict,type(readydict))

    f1 = open("test.json","w+")
    f1.write(generate_json)
    f1.close