import pytest

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"

from gilded_rose import GildedRose

def update_and_return(name, sell_in, quality):
    items = [Item(name, sell_in, quality)]
    inv = GildedRose(items)
    inv.update_quality()
    return items[0]

def test_standard_item_degradation():
    item = update_and_return("Standard Item", 10, 20)
    assert item.sell_in == 9
    assert item.quality == 19

def test_quality_degrades_twice_after_sell_date():
    item = update_and_return("Standard Item", 0, 10)
    assert item.sell_in == -1
    assert item.quality == 8

def test_quality_never_negative():
    item = update_and_return("Standard Item", 5, 0)
    assert item.quality == 0

def test_aged_brie_increases_quality():
    item = update_and_return("Aged Brie", 2, 0)
    assert item.quality == 1

def test_aged_brie_max_quality_50():
    item = update_and_return("Aged Brie", 2, 50)
    assert item.quality == 50

def test_sulfuras_constant():
    item = update_and_return("Sulfuras, Hand of Ragnaros", 0, 80)
    assert item.sell_in == 0
    assert item.quality == 80

def test_backstage_increase_by_1():
    item = update_and_return("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    assert item.quality == 21

def test_backstage_increase_by_2():
    item = update_and_return("Backstage passes to a TAFKAL80ETC concert", 10, 20)
    assert item.quality == 22

def test_backstage_increase_by_3():
    item = update_and_return("Backstage passes to a TAFKAL80ETC concert", 5, 20)
    assert item.quality == 23

def test_backstage_drops_to_zero():
    item = update_and_return("Backstage passes to a TAFKAL80ETC concert", 0, 20)
    assert item.quality == 0
