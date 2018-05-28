
from Items import NormalItem


class Sulfuras(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def setQuality(self, valor):
        self.quality = 80

    def setSellIn(self):
        pass

    def updateItem(self):
        self.setSellIn()


if __name__ == '__main__':
    from ollivander_acceso_a_datos import accesoCasosTexttest
    itemList = ""
    rutaAccesoFichero = "./stdout.gr.txt"
    itemList = accesoCasosTexttest(itemList, rutaAccesoFichero)
    sulfuras = Sulfuras(itemList[0][4][0], itemList[0][4][1], itemList[0][4][2])
    for items in itemList[1:]:
        for item in items:
            if item[0] == sulfuras.getName() and item[1] == sulfuras.getSellIn():
                print(sulfuras)
                sulfuras.updateItem()
                assert sulfuras.getSellIn() == item[1] and sulfuras.getQuality() == item[2], "Error en día %d" % itemList.index(items)
    print("todos casos test pasados!")
