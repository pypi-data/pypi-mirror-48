# -*- coding: utf-8 -*-

# Copyright 2019 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for Shopify instances"""

from .common import Extractor, Message, SharedConfigMixin, generate_extractors
from .. import text
import time
import re


class ShopifyExtractor(SharedConfigMixin, Extractor):
    """Base class for Shopify extractors"""
    basecategory = "shopify"
    filename_fmt = "{product[title]}_{num:>02}_{id}.{extension}"
    archive_fmt = "{id}"

    def __init__(self, match):
        Extractor.__init__(self, match)
        self.item_url = self.root + match.group(1)

    def request(self, url, method="GET", expect=range(400, 500), **kwargs):
        tries = 0
        kwargs["expect"] = expect
        while True:
            response = Extractor.request(self, url, method, **kwargs)
            if response.status_code not in (429, 430):
                return response
            tries += 1
            waittime = 2 ** (tries + 2)
            self.log.warning(
                "HTTP status %s: %s - Waiting for %d seconds",
                response.status_code, response.reason, waittime)
            time.sleep(waittime)

    def items(self):
        data = self.metadata()
        yield Message.Version, 1
        yield Message.Directory, data

        headers = {"X-Requested-With": "XMLHttpRequest"}
        for url in self.products():
            response = self.request(url + ".json", headers=headers)
            if response.status_code >= 400:
                self.log.warning('Skipping %s ("%d: %s")',
                                 url, response.status_code, response.reason)
                continue
            product = response.json()["product"]
            del product["image"]

            for num, image in enumerate(product.pop("images"), 1):
                text.nameext_from_url(image["src"], image)
                image.update(data)
                image["product"] = product
                image["num"] = num
                yield Message.Url, image["src"], image

    def metadata(self):
        """Return general metadata"""
        return {}

    def products(self):
        """Return an iterable with all relevant product URLs"""


class ShopifyCollectionExtractor(ShopifyExtractor):
    """Base class for collection extractors for Shopify based sites"""
    subcategory = "collection"
    directory_fmt = ("{category}", "{collection[title]}")
    pattern_fmt = r"(/collections/[\w-]+)/?(?:\?([^#]+))?(?:$|#)"

    def __init__(self, match):
        ShopifyExtractor.__init__(self, match)
        self.params = match.group(2)

    def metadata(self):
        return self.request(self.item_url + ".json").json()

    def products(self):
        params = text.parse_query(self.params)
        params["page"] = text.parse_int(params.get("page"), 1)
        search_re = re.compile(r"/collections/[\w-]+/products/[\w-]+")

        while True:
            page = self.request(self.item_url, params=params).text
            urls = search_re.findall(page)

            if not urls:
                return
            for path in urls:
                yield self.root + path
            params["page"] += 1


class ShopifyProductExtractor(ShopifyExtractor):
    """Base class for product extractors for Shopify based sites"""
    subcategory = "product"
    directory_fmt = ("{category}", "Products")
    pattern_fmt = r"((?:/collections/[\w-]+)?/products/[\w-]+)"

    def products(self):
        return (self.item_url,)


EXTRACTORS = {
    "fashionnova": {
        "root": "https://www.fashionnova.com",
        "pattern": r"(?:www\.)?fashionnova\.com",
        "test-product": (
            ("https://www.fashionnova.com/products/essential-slide-red", {
                "pattern": r"https?://cdn\.shopify.com/",
                "count": 3,
            }),
            ("https://www.fashionnova.com/collections/flats/products/name"),
        ),
        "test-collection": (
            ("https://www.fashionnova.com/collections/mini-dresses", {
                "range": "1-20",
                "count": 20,
            }),
            ("https://www.fashionnova.com/collections/mini-dresses/?page=1"),
            ("https://www.fashionnova.com/collections/mini-dresses#1"),
        ),

    },
}

generate_extractors(EXTRACTORS, globals(), (
    ShopifyProductExtractor,
    ShopifyCollectionExtractor,
))
