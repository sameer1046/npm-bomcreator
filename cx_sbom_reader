import json
bom_file = open('bom.json',)
bom_data=json.load(bom_file)
for component in bom_data['components']:

    print(component.get('name'))
    print(component.get('version'))
    if 'licenses' in component:    
        for lic in component.get('licenses'):
            print(lic.get('license'))
    print(component.get('purl'))
    if 'externalReferences' in component:
        for externalReference in component.get('externalReferences'):
            print(externalReference.get('url'))
    print('\n')

bom_file.close()
