'''
Returns a dictionary with items indexed in the order that they appear in list passed. 
dictionary item nammed 'count' is the number of items
'''

def parseArgs(args):
    itemType = ""
    items={'count':0}
    for arg in args:
        if arg == "-L" or arg == "--label":
            items['count'] += 1
            items[items['count']] = ['label']
            itemType = "label"

        elif arg == "-B" or arg == "--button":
            items['count'] += 1
            items[items['count']] = ['button']
            itemType = "button"
        
        elif itemType == "":
            continue

        else:
            items[items['count']].append(arg)

    return(items)