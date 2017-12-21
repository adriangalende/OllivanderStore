'''
    obtenemos el valor del elemento en el día 0
    instanciamos objeto de la clase AgedBrie
    llamamos a su método updateItem
    comparamos si el resultado del update == valor sacado de casos Test
'''
from Items import NormalItem


class AgedBrie(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def updateItem(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSellIn()



if __name__ == '__main__':
    from ollivander_acceso_a_datos import accesoCasosTexttest
    itemList = ""
    rutaAccesoFichero = "./stdout.gr.txt"
    itemList = accesoCasosTexttest(itemList, rutaAccesoFichero)
    queso = AgedBrie(itemList[0][1][0], itemList[0][1][1], itemList[0][1][2])
    for items in itemList[1:]:
        for item in items:
            if item[0] == queso.getName():
                queso.updateItem()
                assert queso.getSellIn() == item[1] and queso.getQuality() == item[2], "Error en día %d" % itemList.index(items)
    print("todos casos test pasados!")
