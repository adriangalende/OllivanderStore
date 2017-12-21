'''
    obtenemos el valor del elemento en el día 0
    instanciamos objeto de la clase AgedBrie
    llamamos a su método updateItem
    comparamos si el resultado del update == valor sacado de casos Test
'''
from Items import NormalItem


class AgedBrie(NormalItem):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

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
    item = AgedBrie(itemList[0][1][0], itemList[0][1][1], itemList[0][1][2])

    for dia in range(1, len(itemList)):
        # print(5 * '-' + 'Dia %d' % dia + 5 * '-')
        item.updateItem()
        assert item.getSellIn() == itemList[dia][1][1] and item.getQuality() == itemList[dia][1][2], "Fallo en dia %d" % dia
    print("uptadteQuality Ok")
