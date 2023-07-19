# -*- coding: utf-8 -*-

"""
requests.compat
~~~~~~~~~~~~~~~

This module handles import compatibility issues between Python 2 and
Python 3.
"""

try:
    import chardet
except ImportError:
    import charset_normalizer as chardet

import sys

# -------
# Pythons
# -------

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
is_py2 = _ver[0] == 2

#: Python 3.x?
is_py3 = _ver[0] == 3

try:
    import simplejson as json
except ImportError:
    import json

# ---------
# Specifics
# ---------

if is_py2:
    # Keep OrderedDict for backwards compatibility.
    from collections import Callable, Mapping, MutableMapping, OrderedDict
    from urllib import (
        getproxies,
        getproxies_environment,
        proxy_bypass,
        proxy_bypass_environment,
        quote,
        quote_plus,
        unquote,
        unquote_plus,
        urlencode,
    )

    import cookielib
    from Cookie import Morsel
    from StringIO import StringIO
    from urllib2 import parse_http_list
    from urlparse import urldefrag, urljoin, urlparse, urlsplit, urlunparse

    builtin_str = str
    bytes = str
    str = unicode
    basestring = basestring
    numeric_types = (int, long, float)
    integer_types = (int, long)

elif is_py3:
    # Keep OrderedDict for backwards compatibility.
    from collections import OrderedDict
    from collections.abc import Callable, Mapping, MutableMapping
    from http import cookiejar as cookielib
    from http.cookies import Morsel
    from io import StringIO
    from urllib.parse import (
        quote,
        quote_plus,
        unquote,
        unquote_plus,
        urldefrag,
        urlencode,
        urljoin,
        urlparse,
        urlsplit,
        urlunparse,
    )
    from urllib.request import (
        getproxies,
        getproxies_environment,
        parse_http_list,
        proxy_bypass,
        proxy_bypass_environment,
    )

    builtin_str = str
    str = str
    bytes = bytes
    basestring = (str, bytes)
    numeric_types = (int, float)
    integer_types = (int,)
