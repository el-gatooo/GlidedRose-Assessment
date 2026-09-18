# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # ---- Normal items ----

    def test_normal_item_degrades_by_one_before_sell_date(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_normal_item_degrades_by_two_after_sell_date(self):
        items = [Item("+5 Dexterity Vest", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    def test_normal_item_quality_never_negative(self):
        items = [Item("+5 Dexterity Vest", 5, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_normal_item_quality_never_negative_after_sell_date(self):
        items = [Item("+5 Dexterity Vest", 0, 1)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    # ---- Aged Brie ----

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_increases_twice_as_fast_after_sell_date(self):
        items = [Item("Aged Brie", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(12, items[0].quality)

    def test_aged_brie_quality_never_above_50(self):
        items = [Item("Aged Brie", 5, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    def test_aged_brie_quality_never_above_50_after_sell_date(self):
        items = [Item("Aged Brie", 0, 49)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    # ---- Sulfuras ----

    def test_sulfuras_never_changes_quality_or_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_never_changes_when_sell_in_negative(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    # ---- Backstage passes ----

    def test_backstage_passes_increase_by_one_when_far_out(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_increase_by_two_when_10_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_increase_by_two_boundary_at_11(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(21, items[0].quality)  # 11 days -> still +1

    def test_backstage_passes_increase_by_three_when_5_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_passes_quality_never_above_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_passes_drop_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 40)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
