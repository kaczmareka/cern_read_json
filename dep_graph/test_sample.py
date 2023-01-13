import json_to_graph


"""
Tests of the json_to_graph_function function.
"""

def test_output_type():
    to_print = json_to_graph.json_to_graph_function('tmp\\deps2.json')
    assert isinstance(to_print, str)


def test_output_content():
    to_print = json_to_graph.json_to_graph_function('tmp\\deps.json')
    splited_to_print = to_print.split("\n")
    assert splited_to_print == ['-pkg1', '  -pkg2', '    -pkg3',
                                '  -pkg3', '-pkg2', '  -pkg3', '-pkg3']