from . import json_to_graph


def main():
    """
    Main function of the dep_graph module.
    Uses the json_to_graph function to print 
    the dependency graph to stdout.
    File path is hardcoded to 'tmp\deps.json'.
    """
    to_print=json_to_graph.json_to_graph_function('tmp\\deps.json')
    print(to_print)


if __name__=="__main__":
    main()
