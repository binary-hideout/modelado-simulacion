

if Ret==True:
    NumRet = NumRet + 1
    ToFaltaCajas = ToFaltaCajas + (TAsigC-TC)
    To1 = To1 + (TAsigC-TC)
    To2 = To2 + (TAsigC-TC)
    Reloj = Reloj + (TAsigC-TC)
    TC = TAsigC
else:
        #parte 3 
    if (Fila1 != 0) & (Fila2 <= 5):
        Ts2 = Ts2 - delta
        if Ts2 == 0:
            if LCajas == 0:
                Fila2 = Fila2 + 1
            else:
                LCajas = LCajas - 1
                Na2 = Na2 + 1
                Fila1 = Fila1 - 1
                Ts2 = poisson()
    else:
        To2 = To2 + delta
    if Fila1 <= 5:
        Ts1 = Ts1 - delta
        if Ts1 == 0:
            Fila1 = Fila1 + 1
            Na1 = Na1 + 1
            Ts1 = poisson()
    else:
        To1 = To1 + delta

    if (LCajas == 0) & (Fila1 > 5) & (Fila2 >5):
        Ret = True
        #salida 4
while Reloj>=TLimite:
    print(To1, To2, Na1, Na2)
#paso 5    