'''
    obtenemos el valor del elemento en el día 0
    instanciamos objeto de la clase AgedBrie
    llamamos a su método updateQuality
    comparamos si el resultado del update == valor sacado de casos Test
'''
if __name__ == '__main__':
    from gilded_rose import AgedBrie
    from ollivander_acceso_a_datos import accesoCasosTexttest
    itemList = ""
    rutaAccesoFichero = "./casos_test.txt"
    itemList = accesoCasosTexttest(itemList, rutaAccesoFichero)
    item = AgedBrie(itemList[0][1][0], itemList[0][1][1], itemList[0][1][2])
    for dia in range(1, 30):
        # print(5 * '-' + 'Dia %d' % dia + 5 * '-')
        item.updateQuality()
        assert item.sell_in == itemList[dia][1][1] and item.quality == itemList[dia][1][2], "Fallo en dia %d" % dia
    print("uptadteQuality Ok")
