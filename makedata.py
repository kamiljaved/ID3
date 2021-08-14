import json
import sys, getopt
from random import randint

def main(argv):
    attr_file = None
    data_file = None
    append = True
    random = False
    randCount = 0

    usage = f'USAGE: {sys.argv[0]} (Optional: -a <AttributeFile> -d <DataFile> -n [overwrite old])'

    try:
        (opts, args) = getopt.getopt(argv,"ha:d:nr:",["attr=","data="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt == '-n':
            append = False
        elif opt == '-r':
            random = True
            randCount = int(arg)
        elif opt in ("-a", "--attr"):
            attr_file = arg
        elif opt in ("-d", "--data"):
            data_file = arg

    filetext = ''

    attributes = {}
    if attr_file is None:
        print("---Attributes not provided. Generate Attributes.---")
        attr_file = input('Enter a name for Attribute File: ')

        KnownAttributeCount = 0
        while True:
            name = ""
            if KnownAttributeCount < 1:
                name = input(f'Enter Known Attribute {KnownAttributeCount+1} Name: ')
            else:
                name = input(f'Enter Known Attribute {KnownAttributeCount+1} Name (- to Finish): ')
                if name == "-": break
            KnownAttributeCount += 1
            attributes[KnownAttributeCount] = {}
            attributes[KnownAttributeCount]["Name"] = name
            attributes[KnownAttributeCount]["Values"] = []
            valCount = 0
            while True:
                val = ""
                if valCount < 2:
                    val = input(f'Enter {name} Value {valCount+1}: ')
                else:
                    val = input(f'Enter {name} Value {valCount+1} (- to Finish): ')
                    if val == "-": break
                valCount += 1
                attributes[KnownAttributeCount]["Values"].append(val)    
        
        attributes["Target"] = {}
        name = input(f'Enter Target Attribute Name: ')
        attributes["Target"]["Name"] = name
        attributes["Target"]["Values"] = []
        valCount = 0
        while True:
            val = ""
            if valCount < 2:
                val = input(f'Enter (Target) {name} Value {valCount+1}: ')
            else:
                val = input(f'Enter (Target) {name} Value {valCount+1} (- to Finish): ')
                if val == "-": break
            valCount += 1
            attributes["Target"]["Values"].append(val)

        attributes["KnownAttributeCount"] = KnownAttributeCount

        attributes_json = json.dumps(attributes, indent=4, sort_keys=False)

        input(f"Press Enter to Write Attribute File {attr_file} (or Ctrl-C to Abort)")

        with open(attr_file, 'w') as file:
            file.write(attributes_json)

    else:
        with open(attr_file, 'r') as file:
	        filetext = file.read()

        attributes = json.loads(filetext)
        
    data = {}
    trCount = 0
    vdCount = 0
    if data_file is not None and append is True:
        with open(data_file, 'r') as file:
	        filetext = file.read()

        data = json.loads(filetext)
        trCount = len(data["Training Set"])
        vdCount = len(data["Validation Set"])
        print(data)
        print(trCount)
    else:
        data["Training Set"] = {}
        data["Validation Set"] = {}

    if data_file is None:
        data_file = input('Enter a name for Data File: ')

    p = input("Select Prefix for Data Name: ")
    if p is not '':
        p = p[0].upper()
    print(p)

    print("---Generate Training Data---")
    while True:
        exit = False
        addCount = 0
        ex = {}
        name = p + str(trCount + 1)
        print(f">>> Enter Data for Tr. Ex. {name} (- to Finish)")
        for x in range(1, attributes['KnownAttributeCount']+1):
            vals = f"{attributes[str(x)]['Name']}:  "
            e = 0
            for v in attributes[str(x)]['Values']:
                vals += f'   ({e}: {v})'
                e += 1
            print(vals)
            if random:
                sel = randint(0, len(attributes[str(x)]['Values'])-1)
            else:
                sel = input(f"Select {attributes[str(x)]['Name']}: ")
            if sel == "-": 
                exit = True
                break
            ex[attributes[str(x)]['Name']] = attributes[str(x)]['Values'][int(sel)]
            addCount += 1
            if random:
                if addCount == randCount: break
        if exit == True: break

        vals = f"{attributes['Target']['Name']}:  "
        e = 0
        for v in attributes['Target']['Values']:
            vals += f'   ({e}: {v})'
            e += 1
        print(vals)
        sel = input(f"Select Target Value: ")
        if sel == "-": break
        ex[attributes['Target']['Name']] = attributes['Target']['Values'][int(sel)]

        trCount += 1
        data['Training Set'][name] = ex.copy()


    data_json = json.dumps(data, indent=4, sort_keys=False)

    input(f"Press Enter to Write Data File {attr_file} (or Ctrl-C to Abort)")

    with open(data_file, 'w') as file:
        file.write(data_json)

    return

if __name__ == "__main__":
    main(sys.argv[1:])