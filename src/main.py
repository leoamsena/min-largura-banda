from ReducaoLarguraBanda import ReducaoLarguraBanda as rlb
import time
import pandas as pd
import numpy as np

names = ["/HB/1138_bus", "/HB/494_bus", "/HB/662_bus", "/HB/685_bus", "/HB/abb313", "/HB/arc130", "/HB/ash219", "/HB/ash292", "/HB/ash331", "/HB/ash608", "/HB/ash85", "/HB/ash958", "/HB/bcspwr01", "/HB/bcspwr02", "/HB/bcspwr03", "/HB/bcspwr04", "/HB/bcspwr05", "/HB/bcspwr06", "/HB/bcspwr07", "/HB/bcspwr08", "/HB/bcspwr09", "/HB/bcspwr10", "/HB/bcsstk01", "/HB/bcsstk02", "/HB/bcsstk03", "/HB/bcsstk04", "/HB/bcsstk05", "/HB/bcsstk06", "/HB/bcsstk07", "/HB/bcsstk08", "/HB/bcsstk09", "/HB/bcsstk10", "/HB/bcsstk11", "/HB/bcsstk12", "/HB/bcsstk13", "/HB/bcsstk14", "/HB/bcsstk15", "/HB/bcsstk16", "/HB/bcsstk17", "/HB/bcsstk18", "/HB/bcsstk19", "/HB/bcsstk20", "/HB/bcsstk21", "/HB/bcsstk22", "/HB/bcsstk23", "/HB/bcsstk24", "/HB/bcsstk25", "/HB/bcsstk26", "/HB/bcsstk27",
         "/HB/bcsstk28", "/HB/bcsstk29", "/HB/bcsstk30", "/HB/bcsstk31", "/HB/bcsstk32", "/HB/bcsstk33", "/HB/bcsstm01", "/HB/bcsstm02", "/HB/bcsstm03", "/HB/bcsstm04", "/HB/bcsstm05", "/HB/bcsstm06", "/HB/bcsstm07", "/HB/bcsstm08", "/HB/bcsstm09", "/HB/bcsstm10", "/HB/bcsstm11", "/HB/bcsstm12", "/HB/bcsstm13", "/HB/bcsstm19", "/HB/bcsstm20", "/HB/bcsstm21", "/HB/bcsstm22", "/HB/bcsstm23", "/HB/bcsstm24", "/HB/bcsstm25", "/HB/bcsstm26", "/HB/bcsstm27", "/HB/beacxc", "/HB/beaflw", "/HB/beause", "/HB/blckhole", "/HB/bp_0", "/HB/bp_1000", "/HB/bp_1200", "/HB/bp_1400", "/HB/bp_1600", "/HB/bp_200", "/HB/bp_400", "/HB/bp_600", "/HB/bp_800", "/HB/can_1054", "/HB/can_1072", "/HB/can_144", "/HB/can_161", "/HB/can_187", "/HB/can_229", "/HB/can_24", "/HB/can_256", "/HB/can_268", "/HB/can_292"]
#names = ["/HB/1138_bus", "/HB/494_bus"]
d = [{}, {}]
for name in names:
    try:
        #name = "/HB/arc130"
        print("name = ", name)

        arq_name = name[name.rindex("/")+1:]
        grafo, simetrica = rlb.gerarGrafoNx(
            "/home/leoamsena/UFLA-2020-1/CPA/trab 4/downloadMatrix/" + name)
        rlb.salvarImagem(
            grafo, arq_name, "/home/leoamsena/UFLA-2020-1/CPA/trab 4/images/before")
        print("Matriz simetrica?", simetrica)
        tempo_inicial = time.time()
        larguraInicial = rlb.calcularLarguraBanda(grafo)
        print("Largura de banda incial:", larguraInicial)
        rcm = rlb.reverseCuthillMckee(grafo)
        tempo_final = time.time()
        print("tempo = ", tempo_final - tempo_inicial)
        rlb.salvarImagem(
            rcm, arq_name, "/home/leoamsena/UFLA-2020-1/CPA/trab 4/images/after")
        largura = rlb.calcularLarguraBanda(rcm)
        print("Largura de banda: ", largura)
        reducao = (100*(larguraInicial - largura))/larguraInicial
        d[simetrica][arq_name] = [tempo_final -
                                  tempo_inicial, larguraInicial, largura, reducao]

        #a = input()
    except Exception as ex:
        print(ex)
print("\n\n\n-------------RESULTADOS-------------\n")
columns = columns = [
    'Tempo (s)', 'Largura de banda Inicial', 'Largura de banda final', "Redução (%)"]
print("Simetricas: ")
print(pd.DataFrame.from_dict(
    data=d[1], orient='index', columns=columns))

print("\nAsimetricas: ")
print(pd.DataFrame.from_dict(
    data=d[0], orient='index', columns=columns))
