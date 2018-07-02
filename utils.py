import json


def get_json_arg(req_body, fields):
    """
    Gets argument from JSON
    """
    results = {}
    for i in fields:
        results[i] = json.loads(req_body).get(i)
    return results


def get_filtered(id, items):
    """
    Filters list to pick one item
    """
    result = [item for item in items if item['id'] == int(id)]
    return result
