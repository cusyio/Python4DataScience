# SPDX-FileCopyrightText: 2021 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

from functools import lru_cache
from time import sleep

import httpx


@lru_cache(maxsize=1000)
def nominatim_search(address, format="json", limit=1, **kwargs):
    """Thin wrapper around the Nominatim search API.
    For the list of parameters see
    https://nominatim.org/release-docs/develop/api/Search/#parameters
    """
    search_url = "https://nominatim.openstreetmap.org/search?"
    params = {"q": address, "format": format, "limit": limit, **kwargs}
    r = httpx.get(search_url, params=params)
    # Raise an exception if the status is unsuccessful
    r.raise_for_status()

    sleep(1)
    return r.json()
