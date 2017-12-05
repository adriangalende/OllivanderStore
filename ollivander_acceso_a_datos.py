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
                '''
                for item in linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem - 1):
                    try:
                        int(item)
                    except Exception:
                        pass
                    else:
                        item = int(item)
                    finally:
                        casosTestDia.append(item)
                '''
                item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem - 1)
                item[1] = int(item[1])
                item[2] = int(item[2])
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
    matrizCasosTestString = transformarIntAString(matrizCasosTest[:])
    try:
        if not isinstance(ficheroVolcadoCasosTest, str):
            raise ValueError
        stdout = open(ficheroVolcadoCasosTest, 'w')
    except ValueError:
            print("La ruta de acceso al fichero ha de ser un string")
    else:
        for (offset, casosTestDia) in enumerate(matrizCasosTestString):
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



# Helpers

def transformarIntAString(matrizCasosTest):
    '''
    devuelve en memoria lista con la misma estructura que matrizCasosTest
    pero con los tipos que corresponde a cada item para poder volcar en fichero de texto

        inputs:
            matrizCasosTest lista
            matrizCasosTestFormateada =>
                [
                    [
                        [name,sellIn,quality], # String, integer, integer
                    ],

        output:
            matrizCasosTestFormateada =>
                [
                    [
                        [name,sellIn,quality], # String, String, String
                    ],

    '''
    matrizCasosTestFormateada = []
    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        casosDia = []
        for item in casosTestDia:
            item[1] = str(item[1])
            item[2] = str(item[2])
            casosDia.append(item)
        matrizCasosTestFormateada.append(casosDia)
    return matrizCasosTestFormateada;




if __name__ == "__main__":

    rutaAccesoFichero = "./casos_tets.txt"
    # rutaAccesoFichero = "stdout_bug_conjured.gr"

    matrizCasosTest = []
    matrizCasosTestFormateada = []

    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

    mostrarCasosTest(matrizCasosTest)

    # devuelve lista con los tipos adecuados
    # transformarStringaInt(matrizCasosTest)

    ficheroVolcadoCasosTest = "./stdout.txt"

    crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest)



    #Test
    # String: +5 Dexterity Vest, int: 10, int: 20
    #print(type(transformarStringaInt(matrizCasosTest)[0][0][0])) >> Str
    #print(type(transformarStringaInt(matrizCasosTest)[0][0][1])) >> int
    #print(type(transformarStringaInt(matrizCasosTest)[0][0][0])) >> int
