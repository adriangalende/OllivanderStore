class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


if __name__ == "__main__":
    item = Item("Aged Brie", 2, 0)
    assert isinstance(item.name, str) and isinstance(item.sell_in, int) and isinstance(item.quality, int), "El objeto tipo item debe ser (str, int, int)"
    print(item)
