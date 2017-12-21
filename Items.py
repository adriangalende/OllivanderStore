from Interfaz import Interfaz


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item, Interfaz):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    # getters & setters

    def getName(self):
        return self.name

    def getQuality(self):
        return self.quality

    def getSellIn(self):
        return self.sell_in

    def setSellIn(self):
        self.sell_in -= 1

    def setQuality(self, valor):
        if self.quality + valor > 50:
            # quality can't be bigger than 50 ( general )
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality += valor
        else:
            # quality can't be negative
            self.quality = 0

    # methods

    def updateItem(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            # Once the sell by date has passed, Quality degrades twice as fast
            self.setQuality(-2)
        self.setSellIn()


if __name__ == "__main__":
    items = []
    items.append(NormalItem("Aged Brie", 2, 0))
    items.append(NormalItem("+5 Dexterity Vest", 10, 20))
    for item in items:
        assert isinstance(item.getName(), str) and isinstance(item.getSellIn(), int) and isinstance(item.getQuality(), int), "El objeto tipo item debe ser (str, int, int)"
        print(item)
