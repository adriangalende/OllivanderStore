def accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero):
    '''
        inputs:
            matrizCasosTest list
            rutaAccesoFichero String

        Busca linea a linea en fichero de texto que se encuentra en el argumento rutaAccesoFichero
        La estructura de este fichero es la siguiente:

            ---- dia 0 ---
            name,sellIn,quality
            String: nombre del item, Integer: vender en, Integer: calidad
            ---- dia 1 ---
            name,sellIn,quality
            String: nombre del item, Integer: vender en, Integer: calidad

        Por lo tanto, utilizamos 3 filtros de busqueda por este orden:

            encuentra la palabra "day":  #cabecera inicio de cada uno de los dias
                casosTestDia = []
            si no, si la linea es un salto de linea: # ya no encuentra mas items
                matrizCasosTest = [casosTestDia[]]
            si no, si encuentra la palabra "name": # hemos encontrado la cabecera items
                numeroPropiedadesItem = len(linea.split(','))
            si no: # la linea corresponde a un item
                item = lista con los valores de la linea divididos por el caracter ","
                casosTestDia = [item x]
        outputs:
            Devuelve una lista que contiene una lista de listas con los items de cada dia
            matrizCasosTest =>
                [
                    Dia0[
                            [name,sellIn,quality],
                            [name,sellIn,quality],
                            [name,sellIn,quality],
                            [name,sellIn,quality],
                            [name,sellIn,quality]
                        ],
                    Dia1[
                            [name,sellIn,quality],
                            [name,sellIn,quality],
                            [name,sellIn,quality],
                            [name,sellIn,quality],
                            [name,sellIn,quality]
                        ],
                    Dia n...

    '''
    try:
        if not isinstance(rutaAccesoFichero, str):
            raise ValueError
        fichero = open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        print("Fichero no encontrado")
        return []
    except ValueError:
        print("El nombre del fichero ha de ser un string")
        return []
    else:
        matrizCasosTest = []
        numeroPropiedadesItem = 0
        for linea in fichero:
            if linea.find("day") != -1:
                casosTestDia = []
            elif linea == "\n":
                matrizCasosTest.append(casosTestDia)
            elif linea.find("name") != -1:
                numeroPropiedadesItem = len(linea.split(','))
            else:
                item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem - 1)
                casosTestDia.append(item)
        fichero.close()
        return matrizCasosTest


def crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest):
    '''
        inputs:
            ficheroVolcadoCasosTest String # ruta de acceso a fichero para casos test
            matrizCasosTest lista #contiene lista de listas, que contiene una lista de items

        recorre matrizCasosTest utilizando la tupla:
            (offset, casosTestDia) => indice de la lista, lista con lista de items
            #escribe cabecera separadora convirtiendo el indice que recibe de offset a string
            ----- Dia x -----
            recorre casosTestDia
                escribe en el archivo de texto la unión de cada una de las listas por ","
                y añade un salto de línea para el próximo item

                ["name","sellIn","quality"] ==> name,sellIn,quality \n
                ["nombreItem"," x"," x"] ==> nombreitem, x, x \n

        Output:
            Si el archivo que está en la ruta no existe, lo crea
            si ya existía lo sobreescribe con el siguiente formato
            ----- Dia x -----
            name,sellIn,quality
            nombreitem, x, x

        '''

    try:
        if not isinstance(ficheroVolcadoCasosTest, str):
            raise ValueError
        stdout = open(ficheroVolcadoCasosTest, 'w')
    except ValueError:
            print("La ruta de acceso al fichero ha de ser un string")
    else:
        for (offset, casosTestDia) in enumerate(matrizCasosTest):
            stdout.write('-' * 5 + " Dia %d: " % offset + '-' * 5 + '\n')
            for item in casosTestDia:
                stdout.write(','.join(item) + '\n')
        stdout.close()


def mostrarCasosTest(matrizCasosTest):
    '''
        inputs:
            matrizCasosTest lista

        output:
            muestra por consola los items que contiene la lista matrizCasosTest
            

    '''

    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)


if __name__ == "__main__":

    rutaAccesoFichero = "./casos_tets.txt"
    # rutaAccesoFichero = "stdout_bug_conjured.gr"

    matrizCasosTest = []

    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

    mostrarCasosTest(matrizCasosTest)

    ficheroVolcadoCasosTest = "./stdout.txt"

    crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest)
