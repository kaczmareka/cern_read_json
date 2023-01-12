import json #built-in Python module
from collections import OrderedDict #built-in Python module

def function(file_path):
    #read json file to a Python dictionary
    with open(file_path) as json_file:
        json_content = json.load(json_file)
    #convert dictionary to OrderedDict, to have also indexes easily available
    ordered_json_content=OrderedDict(json_content)
    #get the keys of the dictionary
    keys=list(ordered_json_content.keys())

    def print_name(values, indent, to_print):
        for value in values:
            if value in keys:
                to_print+=str("  "*indent+f"-{value}"+"\n")
                indent+=1
                to_print=print_name(ordered_json_content[value],indent, to_print)
                indent-=1
            else:
                to_print+=str("  "*indent+f"-{value}"+"\n")
        return to_print

    to_print =""

    returned=print_name(keys,0, to_print)
    return returned

def main():
    variable=function('tmp\deps2.json')
    print(variable)

if __name__=="__main__":
    main()
