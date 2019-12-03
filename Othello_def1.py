# Autor : Luis Valencia 14-11335

# Variables iniciales
PlayerOneBlack = 1
PlayerTwoWhite = 2
turno = 0

# Funcion para crear el tablero
def crearTablero():
    tablero = [ [0 for j in range(0, 8)] for i in range(0, 8)]
    tablero[3][4] = tablero[4][3] = PlayerOneBlack
    tablero[4][4] = tablero[3][3] = PlayerTwoWhite


    a = ""
    for k in range(8):
        for j in range(8):
            a+=str(tablero[k][j])+str("  ")
        print (a)
        a=""

    return tablero

# Funcion cambiar jugador
def cambiarJugador(turn):
    if turn == 0:
        turn = 1
    elif turn == 1:
        turn = 0
    return turn

def quedanFichas(tablero):
    quedaFicha = True
    for i in range(0, 8):
        for j in range(0, 8):
            if tablero[i][j] == 0:
                break
            else:
                quedaFicha = False

    return quedaFicha


# Funcion para definir si una jugada es valida o no
def esValida(tablero, columna, fila, turno):
    valido = False

    if fila > 8 or columna > 8:
        pass
    else:
        if tablero[fila][columna] != 0:
            pass
        else:
            if turno == 0:
                tu_pieza = PlayerOneBlack
                oponente = PlayerTwoWhite
            elif turno == 1:
                tu_pieza = PlayerTwoWhite
                oponente = PlayerOneBlack

            for x, y in [ [1, 1], [0, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1] ]:
                if valido == True:
                    break
                columna_tablero, fila_tablero = columna, fila
                columna_tablero = columna_tablero + x
                
                fila_tablero = fila_tablero + y
                
                if fila_tablero > 7 or columna_tablero > 7:
                    continue

                if tablero[fila_tablero][columna_tablero] == oponente:
                    while tablero[fila_tablero][columna_tablero] == oponente:
                        columna_tablero = columna_tablero + x
                        fila_tablero = fila_tablero + y
                        if columna_tablero > 7 or fila_tablero > 7:
                            break
                        elif tablero[fila_tablero][columna_tablero] == tu_pieza:
                            valido = True
                            break

                if fila_tablero > 7 or columna_tablero > 7:
                    continue
        
    return valido

# Piezas verticalez que se consumen luego de la jugada
def consumoVertical(tablero, columna, fila, turno):
    consumoVertical = []
    consumoVerticalUp = []
    consumoVerticalUpFinal = []
    consumoVerticalDown = []
    consumoVerticalDownFinal = []

    if turno == 0:
        tu_pieza = PlayerOneBlack
        oponente = PlayerTwoWhite
    elif turno == 1:
        tu_pieza = PlayerTwoWhite
        oponente = PlayerOneBlack

    tablero_fila_up = fila + 1
    
    if tablero_fila_up < 8:
        if tablero[tablero_fila_up][columna] == oponente:
            while tablero[tablero_fila_up][columna] == oponente:
                consumoVerticalUp.append([tablero_fila_up, columna])
                tablero_fila_up = tablero_fila_up + 1
                if tablero_fila_up > 8:
                    continue
                elif tablero[tablero_fila_up][columna] == tu_pieza:
                    consumoVerticalUpFinal = consumoVerticalUp
                    break

    tablero_fila_down = fila - 1

    if tablero[tablero_fila_down][columna] == oponente:
        while tablero[tablero_fila_down][columna] == oponente:
            consumoVerticalDown.append([tablero_fila_down, columna])
            tablero_fila_down = tablero_fila_down - 1
            if tablero_fila_down < 0:
                continue
            elif tablero[tablero_fila_down][columna] == tu_pieza:
                consumoVerticalDownFinal = consumoVerticalDown
                break
    


    consumoVertical = consumoVerticalUpFinal + consumoVerticalDownFinal
    

    return consumoVertical



        

# Piezas horizontales que se consumen luego de la jugada

def consumoHorizontal(tablero, columna, fila, turno):
    consumoHorizontal = []
    consumoHorizontalRight = []
    consumoHorizontalRightFinal = []
    consumoHorizontalLeft = []
    consumoHorizontalLeftFinal = []


    if turno == 0:
        tu_pieza = PlayerOneBlack
        oponente = PlayerTwoWhite
    elif turno == 1:
        tu_pieza = PlayerTwoWhite
        oponente = PlayerOneBlack

    tablero_columna_right = columna + 1
    tablero_columna_left = columna - 1

    if tablero[fila][tablero_columna_right] == oponente:
        while tablero[fila][tablero_columna_right] == oponente:
            consumoHorizontalRight.append([fila, tablero_columna_right])
            tablero_columna_right = tablero_columna_right + 1
            if tablero_columna_right > 8:
                break
            elif tablero[fila][tablero_columna_right] == tu_pieza:
                consumoHorizontalRightFinal = consumoHorizontalRight
                break
    
    if tablero[fila][tablero_columna_left] == oponente:
        while tablero[fila][tablero_columna_left] == oponente:
            consumoHorizontalLeft.append([fila, tablero_columna_left])
            tablero_columna_left = tablero_columna_left - 1
            if tablero_columna_left > 8:
                break
            elif tablero[fila][tablero_columna_left] == tu_pieza:
                consumoHorizontalLeftFinal = consumoHorizontalLeft
                break

    consumoHorizontal = consumoHorizontalRightFinal + consumoHorizontalLeftFinal

    return consumoHorizontal
    


# Piezas diagonales que se consumen luego de la jugada
def consumoDiagonal(tablero, columna, fila, turno):
    consumoDiagonal = []
    consumoDiagonalRightUp = []
    consumoDiagonalRightUpFinal = []
    consumoDiagonalRightDown = []
    consumoDiagonalRightDownFinal = []
    consumoDiagonalLeftUp = []
    consumoDiagonalLeftUpFinal = []
    consumoDiagonalLeftDown = []
    consumoDiagonalLeftDownFinal = []


    if turno == 0:
        tu_pieza = PlayerOneBlack
        oponente = PlayerTwoWhite
    elif turno == 1:
        tu_pieza = PlayerTwoWhite
        oponente = PlayerOneBlack

    tablero_diagonal_up = fila + 1
    tablero_diagonal_right = columna + 1
    tablero_diagonal_left = columna - 1
    tablero_diagonal_down = fila - 1
    
    if tablero_diagonal_up < 8:
        if tablero[tablero_diagonal_up][tablero_diagonal_right] == oponente:
            while tablero[tablero_diagonal_up][tablero_diagonal_right] == oponente:
                consumoDiagonalRightUp.append([tablero_diagonal_up, tablero_diagonal_right])
                tablero_diagonal_up = tablero_diagonal_up + 1
                tablero_diagonal_right = tablero_diagonal_right + 1
                if tablero_diagonal_right > 8 or tablero_diagonal_up > 8:
                    break
                elif tablero[tablero_diagonal_up][tablero_diagonal_right] == tu_pieza:
                    consumoDiagonalRightUpFinal = consumoDiagonalRightUp
                    break
        
        if tablero[tablero_diagonal_up][tablero_diagonal_left] == oponente:
            while tablero[tablero_diagonal_up][tablero_diagonal_left] == oponente:
                consumoDiagonalLeftUp.append([tablero_diagonal_up, tablero_diagonal_left])
                tablero_diagonal_up = tablero_diagonal_up + 1
                tablero_diagonal_left = tablero_diagonal_left - 1
                if tablero_diagonal_left < 0 or tablero_diagonal_up > 8:
                    break
                elif tablero[tablero_diagonal_up][tablero_diagonal_right] == tu_pieza:
                    consumoDiagonalLeftUpFinal = consumoDiagonalLeftUp
                    break

    if tablero_diagonal_right < 8:
        if tablero[tablero_diagonal_down][tablero_diagonal_right] == oponente:
            while tablero[tablero_diagonal_down][tablero_diagonal_right] == oponente:
                consumoDiagonalRightDown.append([tablero_diagonal_down, tablero_diagonal_right])
                tablero_diagonal_down = tablero_diagonal_down - 1
                tablero_diagonal_right = tablero_diagonal_right + 1
                if tablero_diagonal_right > 8 or tablero_diagonal_down < 0:
                    break
                elif tablero[tablero_diagonal_down][tablero_diagonal_right] == tu_pieza:
                    consumoDiagonalRightDownFinal = consumoDiagonalRightDown
                    break
        
        if tablero[tablero_diagonal_down][tablero_diagonal_left] == oponente:
            while tablero[tablero_diagonal_down][tablero_diagonal_left] == oponente:
                consumoDiagonalLeftDown.append([tablero_diagonal_down, tablero_diagonal_left])
                tablero_diagonal_down = tablero_diagonal_down - 1
                tablero_diagonal_left = tablero_diagonal_left - 1
                if tablero_diagonal_left < 0 or tablero_diagonal_down < 0:
                    break
                elif tablero[tablero_diagonal_down][tablero_diagonal_left] == tu_pieza:
                    consumoDiagonalLeftDownFinal = consumoDiagonalLeftDown
                    break
    
    consumoDiagonal = consumoDiagonalLeftDownFinal + consumoDiagonalLeftUpFinal + consumoDiagonalRightDownFinal + consumoDiagonalRightUpFinal
    
    print(consumoDiagonal)
    return consumoDiagonal

# Piezas que se consumen en total luego de realizar la jugada
def consumo(tablero, columna, fila, turno):
    consumoTotal = []
    consumoTotal = consumoVertical(tablero, columna, fila, turno) + consumoHorizontal(tablero, columna, fila, turno) + consumoDiagonal(tablero, columna, fila, turno)

    return consumoTotal

# Funcion para mostrar la jugada realizada
def reflejarJugada(tablero, columna, fila, turno):
    if turno == 0:
        jugada = 1
    elif turno == 1:
        jugada = 2

    tablero[fila][columna] = jugada
    jugadaReflejada = consumo(tablero, columna, fila, turno)

    
    if len(jugadaReflejada) > 0:
        for x, y in jugadaReflejada:
            tablero[x][y] = jugada
    else:
        return False

    a = ""
    for k in range(8):
        for j in range(8):
            a+=str(tablero[k][j])+str("  ")
        print (a)
        a=""

    return tablero

# Funcion para pedir la jugada a los jugadores
def obtenerJugada():

    fila = int(input("Ingrese la fila en la que desea jugar: "))
    columna = int(input("Ingrese la columna en la que desea jugar: "))

    jugadaObtenida = [fila, columna]

    return jugadaObtenida

    



turno = 0
tablero = crearTablero()

# Comienzo y bucle del juego
while True:
    jugadaObtenida = obtenerJugada()
    if esValida(tablero, jugadaObtenida[1], jugadaObtenida[0], turno) == True:
        reflejarJugada(tablero, jugadaObtenida[1], jugadaObtenida[0], turno)
        turno = cambiarJugador(turno)
    elif esValida(tablero, jugadaObtenida[1], jugadaObtenida[0], turno) == False:
        print("La jugada no es valida.")

    



