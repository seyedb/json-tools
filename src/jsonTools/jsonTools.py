import json
from collections import OrderedDict

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
