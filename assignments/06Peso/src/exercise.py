def main():
    #escribe tu código abajo de esta línea
    pass
    pesoIn = float(input('Dame el peso inicial: '))
    pesoFn = float(input('Dame el peso final: '))
    mesesMet = int(input('Dame la cantidad de meses: '))
    pesoxmes = (pesoIn-pesoFn) / mesesMet
    print('Lo que debes bajar por mes es: ' + str(pesoxmes))




if __name__ == '__main__':
    main()
