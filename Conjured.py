from Items import NormalItem


class Conjured(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def updateItem(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSellIn()


if __name__ == '__main__':
    from ollivander_acceso_a_datos import accesoCasosTexttest
    itemList = ""
    rutaAccesoFichero = "./stdout.gr.txt"
    itemList = accesoCasosTexttest(itemList, rutaAccesoFichero)
    conjured = Conjured(itemList[0][8][0], itemList[0][8][1], itemList[0][8][2])
    for items in itemList[1:]:
        for item in items:
            if item[0] == conjured.getName():
                conjured.updateItem()
                assert conjured.getSellIn() == item[1] and conjured.getQuality() == item[2], "Error en día %d" % itemList.index(items)
    print("todos casos test pasados!")
