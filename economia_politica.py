def EconomiaPolitca(Xo, Xd,P_valores):
    # pasa 2 listas llamadas Xo y Xd, cada una se convierte a enteros para luego ser desenpaquetadas
    # y cada dato guardado en una variable que va a hacer las respectivas cuentas y luego hacer un grafico
    for XO in Xo:
        print("desempaquetado")
        dato_incognita_Xo = ""
        Xo_p = ""
        otro_dato_Xo = ""
    for XD in Xd:
        print("desempaquetado")
        dato_incognita_Xd = ""
        Xd_p = ""
        otro_dato_Xd = ""
    for P_valor in P_valores:
        print("desempaquetar")
        valor1 = ""
        valor2 = ""
    if P_valores == "":
        incognita = dato_incognita_Xo + dato_incognita_Xd
        otro = otro_dato_Xo + otro_dato_Xd
        valor_p = otro / incognita
        resultado = dato_incognita_Xo * valor_p + otro_dato_Xo
        return f"el valor del P es:{valor_p} y el valor de la oferta es:{resultado}, aca es donde esta el punto de equilibrio"
    elif P_valores == []:
        resultado1 = dato_incognita_Xo * valor1 + otro_dato_Xo 
        resultado2 = dato_incognita_Xo * valor2 + otro_dato_Xo
        return f"los valores del precio son {valor1} y {valor2}, su oferta es {resultado1} y {resultado2}"
    else:
        return "que haces"
    