import json
from collections import OrderedDict
import deepdiff

def sort_json(json_file, field_name, reverse=False):
    """Sorts a JSON object loaded from a file by field value.

    Args:
        json_file (str): path to the input file.
        field_name (str): the name of the key, based on which the JSON object is going to be sorted.
        reverse (bool): sort in the descending or ascending order.
    Returns:
        (json obj) the sorted JSON object.
    """
    with open(json_file, 'r') as fid:
        dout = json.loads(fid.read())

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
    with open(a_json, 'r') as a_fid:
        a_dict = json.loads(a_fid.read())

    with open(b_json, 'r') as b_fid:
        b_dict = json.loads(b_fid.read())

    return deepdiff.DeepDiff(a_dict, b_dict, ignore_order=ignore_order)
