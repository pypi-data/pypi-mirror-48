from urllib.parse import urlsplit, urlunsplit, parse_qs, urlencode

import requests


def expand(url: str) -> str:
    """
    Expands shortened urls, otherwise returns same url. Raises requests exceptions if any.

    :param url: shortened url
    :return: expanded url
    """
    r = requests.get(url)
    return r.url


def replace(url: str, replace_dict: dict, strict=True):
    """
    :param url: string url
    :param replace_dict: dictionary of keys to replace with new values {param_name: new_value, param_name2: new_value2}
    :param strict: if True (default) will only replace existing params, if False will add new params to URL
    :return: string url
    """
    split_url = urlsplit(url)
    query = split_url.query
    query_dict = parse_qs(query)

    for k, v in replace_dict.items():
        if strict and k not in query_dict.keys():
            raise KeyError(
                f"{k}, set strict to false if you want to add a param to url."
            )
        query_dict[k] = [v]

    new_query = urlencode(query_dict, True)

    return urlunsplit(
        [
            split_url.scheme,
            split_url.netloc,
            split_url.path,
            new_query,
            split_url.fragment,
        ]
    )
