# -*- coding: utf-8 -*-

MAX_QUALITY = 50
MIN_QUALITY = 0

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED_PREFIX = "Conjured"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_item(item)

    def _update_item(self, item):
        if item.name == SULFURAS:
            return

        if item.name == AGED_BRIE:
            self._increase_quality(item)
        elif item.name == BACKSTAGE_PASSES:
            self._age_backstage_pass(item)
        else:
            self._decrease_quality(item, self._degrade_amount(item))

        item.sell_in -= 1

        if item.sell_in < 0:
            if item.name == AGED_BRIE:
                self._increase_quality(item)
            elif item.name == BACKSTAGE_PASSES:
                item.quality = 0
            else:
                self._decrease_quality(item, self._degrade_amount(item))

    def _age_backstage_pass(self, item):
        self._increase_quality(item)
        if item.sell_in < 11:
            self._increase_quality(item)
        if item.sell_in < 6:
            self._increase_quality(item)

    @staticmethod
    def _degrade_amount(item):
        return 2 if item.name.startswith(CONJURED_PREFIX) else 1

    @staticmethod
    def _increase_quality(item, amount=1):
        item.quality = min(MAX_QUALITY, item.quality + amount)

    @staticmethod
    def _decrease_quality(item, amount=1):
        item.quality = max(MIN_QUALITY, item.quality - amount)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
