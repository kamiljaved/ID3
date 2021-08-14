from tree import Node
from math import log2

ID3_METHOD_GainInformation = 0
ID3_METHOD_GainRatio = 1

def ID3(examples, targetAttribute, attributes, method=ID3_METHOD_GainInformation):
    
    node = Node("NULL", Node.ATTRIBUTE)

    target = targetAttribute["Name"]
    tavs = targetAttribute["Values"]

    sorted = {}

    for tav in tavs:
        sorted[tav] = {}
        for ex in examples.items():
            if ex[1][target] == tav:
                sorted[tav][ex[0]] = ex[1]

        # return if all examples are of this class
        if (len(sorted[tav]) == len(examples)):
            return Node(tav, Node.LEAF)
    
    if len(attributes) == 0:
        len_max = 0
        label = 'NULL'
        for tav in tavs:
            val_len = len(sorted[tav])
            if val_len > len_max:
                len_max =  val_len
                label = tav

        return Node(label, Node.LEAF)

    # calculate entropy of data
    En_S = 0
    tav_max = -1
    tav_most_common = ''
    for tav in tavs:
        if len(sorted[tav]) > tav_max:
            tav_max = len(sorted[tav])
            tav_most_common = tav
        p_i = len(sorted[tav])/len(examples)
        if p_i != 0:
            En_S -= p_i*log2(p_i)

    max_gain = -1
    max_gain_attr_name = ''
    max_gain_attr_vals = {}

    # select the best Attribute for this Node
    for attr in attributes:
        GainI_S_A = En_S
        SplitI_S_A = 0
        GainR_S_A = 0
        Gain_S_A = 0

        vals = attributes[attr]
    
        sorted_2 = {}

        for val in vals:
            sorted_2[val] = {}
            for ex in examples.items():
                if ex[1][attr] == val:
                    sorted_2[val][ex[0]] = ex[1]

            if len(sorted_2[val]) == 0:
                continue
            sorted_3 = {}
            En_Sv = 0


            for tav in tavs:
                sorted_3[tav] = {}
                for ex in sorted_2[val].items():
                    if ex[1][target] == tav:
                         sorted_3[tav][ex[0]] = ex[1]

                p_i = len(sorted_3[tav])/len(sorted_2[val])
                if p_i != 0:
                    En_Sv -= p_i*log2(p_i)
            p_Sv = (len(sorted_2[val])/len(examples))
            GainI_S_A -= p_Sv*En_Sv
            if method == ID3_METHOD_GainRatio:
                SplitI_S_A -= p_Sv*log2(p_Sv)
                GainR_S_A = GainI_S_A / SplitI_S_A

        print(f'{attr:<12}:   {GainI_S_A:.4f}   {SplitI_S_A:.4f}   {GainR_S_A:.4f}')

        if method == ID3_METHOD_GainInformation:
            Gain_S_A = GainI_S_A
        elif method == ID3_METHOD_GainRatio:
            Gain_S_A = GainR_S_A

        if Gain_S_A > max_gain:
            max_gain = Gain_S_A
            max_gain_attr_name = attr 
            max_gain_attr_vals = sorted_2

    vals = attributes[max_gain_attr_name]

    node.setLabel(max_gain_attr_name)

    for val in vals:
        examples_vi = max_gain_attr_vals[val]
        subnode = Node(val, Node.VALUE)
        if len(examples_vi) == 0:
            subnode.addSubNode(Node(tav_most_common, Node.LEAF))
        else:
            attributes_vi = attributes.copy()
            attributes_vi.pop(max_gain_attr_name)
            subnode.addSubNode(ID3(examples_vi, targetAttribute, attributes_vi, method))
        node.subnodes.append(subnode)

    return node