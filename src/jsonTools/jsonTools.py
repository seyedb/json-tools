import json
from collections import OrderedDict
import deepdiff

def _jsonToDict(json_file):
    """Reads in a JSON file and converts it into a dictionary.
    Args:
        json_file (str): path to the input file.
    Returns:
        (dict) a dictionary containing the data from the input JSON file.
    """
    with open(json_file, 'r') as fid:
        dout = json.loads(fid.read())

    return dout

def sort_json(json_file, field_name, reverse=False):
    """Sorts a JSON object loaded from a file by field value.

    Args:
        json_file (str): path to the input file.
        field_name (str): the name of the key, based on which the JSON object is going to be sorted.
        reverse (bool): sort in the descending or ascending order.
    Returns:
        (json obj) the sorted JSON object.
    """
    dout = _jsonToDict(json_file)
    json_keys = dout.keys()
    sorted_keys = sorted(json_keys, key=lambda k: dout[k][field_name], reverse=reverse)
    res = OrderedDict()
    for k in sorted_keys:
        res[k] = dout[k]

    return json.loads(json.dumps(res))

def compare_json(a_json, b_json, ignore_order=True):
    """Compares two JSON objects. Uses 'deepdiff.DeepDiff'.

    Args:
        a_json (str): path to the first .json file.
        b_json (str): path to the second .json file.
        ignore_order (bool): whether or not ignore ordering of fields.
    Returns:
        (dict) a dictionary reporting differences between the two JSON objects.
    """
    a_dict = _jsonToDict(a_json)
    b_dict = _jsonToDict(b_json)
    return deepdiff.DeepDiff(a_dict, b_dict, ignore_order=ignore_order)
