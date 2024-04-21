from nbtlib import parse_nbt


def getPartsFlag(nbts):
    comp = parse_nbt(nbts)
    tags = dict()
    for i in comp['BlockEntityTag']['Patterns']:
        tags[i['Pattern']] = i['Color']
    return tags


#print(getPartsFlag('{BlockEntityTag:{Patterns:[{Color:14,Pattern:"cre"},{Color:4,Pattern:"sku"},{Color:13,Pattern:"flo"},{Color:12,Pattern:"mc"}]}}'))
