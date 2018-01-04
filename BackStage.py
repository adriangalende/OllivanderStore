from Items import NormalItem


class BackStage(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def updateItem(self):
        '''
        increases in Quality as its SellIn value approaches;
        Quality increases by 2 when there are 10 days or less and by 3 when
        there are 5 days or less but
        Quality drops to 0 after the concert
         '''

        if self.sell_in > 10:
            self.setQuality(1)
        elif self.sell_in > 5:
            self.setQuality(2)
        elif self.sell_in > 0:
            self.setQuality(3)
        else:
            self.quality = 0
        self.setSellIn()




if __name__ == '__main__':
    from ollivander_acceso_a_datos import accesoCasosTexttest
    itemList = ""
    rutaAccesoFichero = "./stdout.gr.txt"
    itemList = accesoCasosTexttest(itemList, rutaAccesoFichero)
    entradas = BackStage(itemList[0][5][0], itemList[0][5][1], itemList[0][5][2])
    for items in itemList:
        for item in items:
            if item[0] == entradas.getName() and item[1] == entradas.getSellIn():
                print(entradas)
                assert entradas.getSellIn() == item[1] and entradas.getQuality() == item[2], "Error en día %d" % itemList.index(items)
                entradas.updateItem()
    print("todos casos test pasados!")
