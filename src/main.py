from ReducaoLarguraBanda import ReducaoLarguraBanda as rlb
import time
import pandas as pd
import numpy as np


names = ['/HB/1138_bus', '/HB/494_bus', '/HB/662_bus', '/HB/685_bus', '/HB/abb313', '/HB/arc130', '/HB/ash219', '/HB/ash292', '/HB/ash331', '/HB/ash608', '/HB/ash85', '/HB/ash958', '/HB/bcspwr01', '/HB/bcspwr02', '/HB/bcspwr03', '/HB/bcspwr04', '/HB/bcspwr05', '/HB/bcspwr06', '/HB/bcspwr07', '/HB/bcspwr08', '/HB/bcspwr09', '/HB/bcspwr10', '/HB/bcsstk01', '/HB/bcsstk02', '/HB/bcsstk04', '/HB/bcsstk05', '/HB/bcsstk06', '/HB/bcsstk07', '/HB/bcsstk09',
         '/HB/bcsstk13', '/HB/bcsstk19', '/HB/bcsstk23', '/HB/bcsstk24', '/HB/bcsstk26', '/HB/bcsstk27', '/HB/bcsstk28', '/HB/bcsstk30', '/HB/bcsstk32', '/HB/bcsstk33', '/HB/bcsstm07', '/HB/bcsstm27', '/HB/bp_0', '/HB/bp_1000', '/HB/bp_1200', '/HB/bp_1400', '/HB/bp_1600', '/HB/bp_200', '/HB/bp_400', '/HB/bp_600', '/HB/bp_800', '/HB/can_1054', '/HB/can_1072', '/HB/can_144', '/HB/can_161', '/HB/can_187', '/HB/can_229', '/HB/can_24', '/HB/can_256', '/HB/can_268']
d = [{}, {}]
for name in names:
    try:
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
df = pd.DataFrame.from_dict(
    data=d[1], orient='index', columns=columns)
print(df)
print("latex: \n", df.to_latex(), "\n\n\\n")

print("\nAsimetricas: ")
df = pd.DataFrame.from_dict(
    data=d[0], orient='index', columns=columns)
print(df)
print("latex: \n", df.to_latex())
