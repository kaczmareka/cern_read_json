import json #built-in Python module
from collections import OrderedDict #built-in Python module

def function(file_path):
    #read json file to a Python dictionary
    with open(file_path) as json_file:
        json_content = json.load(json_file)
    print(type(json_content))
    print(json_content)
    #convert dictionary to OrderedDict, to have also indexes easily available
    ordered_json_content=OrderedDict(json_content)
    #get the keys of the dictionary
    keys=list(ordered_json_content.keys())

    def print_name(values,indent):
        for value in values:
            if value in keys:
                print("  "*indent+f"-{value}")
                indent+=1
                print_name(ordered_json_content[value],indent)
                indent-=1
            else:
                print("  "*indent+f"-{value}")
        
    print_name(keys,0)

def main():
    print("Hello you!") #prints to stdout by definition, according to python documentation
    function('tmp\deps.json')

if __name__=="__main__":
    main()