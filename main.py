import json
import sys, getopt
from id3 import  ID3, ID3_METHOD_GainInformation, ID3_METHOD_GainRatio
from tree import Node

def main(argv):
    attr_file = None
    data_file = None
    id3_method = ID3_METHOD_GainInformation
    usage = f'USAGE: {sys.argv[0]} -a <AttributeFile> -d <DataFile> (Optional: -r [use Gain-Ratio])'

    try:
        (opts, args) = getopt.getopt(argv,"ha:d:r",["attr=","data="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt == '-r':
            id3_method = ID3_METHOD_GainRatio
        elif opt in ("-a", "--attr"):
            attr_file = arg
        elif opt in ("-d", "--data"):
            data_file = arg

    if attr_file is None or data_file is None:
        print("Please provide Attribute and Data files.")
        print(usage)
        sys.exit()

    filetext = ''
    
    with open(attr_file, 'r') as file:
	    filetext = file.read()

    attributes = json.loads(filetext)

    targetAttribute = attributes["Target"]

    knownAttributes = {}
    for i in range(attributes["KnownAttributeCount"]):
        knownAttributes[attributes[str(i+1)]["Name"]] = attributes[str(i+1)]["Values"]


    with open(data_file, 'r') as file:
	    filetext = file.read()

    examples = json.loads(filetext)
    decision_tree = ID3(examples["Training Set"], targetAttribute, knownAttributes, id3_method)

    decision_tree.PrintTree()

    return

if __name__ == "__main__":
    main(sys.argv[1:])