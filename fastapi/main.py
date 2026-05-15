# SPDX-FileCopyrightText: 2021 cusy GmbH
#
# SPDX-License-Identifier: BSD-3-Clause

"""FastAPI application for items."""

from pydantic import BaseModel

from fastapi import FastAPI


app = FastAPI()


class Item(BaseModel):
    """Defines the Item type with the attributes name, price and is_offer.

    Args:
        name (str): The name of the item.
        price (float): The price of the item.
        is_offer (bool): Is the item on offer? Defaults to None.

    """

    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
