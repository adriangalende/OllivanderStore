from ollivander_acceso_a_datos import *
from Items import *

def obtenerDatosMatriz():
    return matrizCasosTest[0]



if __name__ == "__main__":

    rutaAccesoFichero = "stdout.gr.txt"

    matrizCasosTest = []

    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)
    tiposItems = {
        "Aged Brie": "AgedBrie()",
        "Sulfuras, Hand of Ragnaros":"Sulfuras()",
        "Backstage passes to a TAFKAL80ETC concert":"BackStage()"
    }
    itemList = []
    index = 0
    for item in obtenerDatosMatriz():
        if item[0] in tiposItems:
            itemList.append(eval(tiposItems[item[0]]))
        else:
            pass
        index += 1

    print(itemList)
