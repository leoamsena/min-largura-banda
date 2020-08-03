# Trabalho de CPA - 2020/1 UFLA

Trabalho para a disciplina de CPA desenvolvido para obtenção de créditos parciais.

## Resultados

Matrizes da base SuiteSparse utilizadas nos testes bem como seus resultados de largura de banda:

### Matrizes simétricas

| Nome da matriz | Tempo (s) | Largura de banda Inicial | Largura de banda final | Redução (\%) |
| -------------- | --------: | -----------------------: | ---------------------: | -----------: |
| 1138_bus       |  0.225985 |                     1030 |                    131 |    87.281553 |
| 494_bus        |  0.087860 |                      428 |                     82 |    80.841121 |
| 662_bus        |  0.121076 |                      335 |                    118 |    64.776119 |
| 685_bus        |  0.139368 |                      550 |                    102 |    81.454545 |
| ash292         |  0.103602 |                       24 |                     32 |   -33.333333 |
| ash85          |  0.024645 |                       39 |                     13 |    66.666667 |
| bcspwr01       |  0.009920 |                       38 |                      6 |    84.210526 |
| bcspwr02       |  0.010113 |                       34 |                     13 |    61.764706 |
| bcspwr03       |  0.039614 |                      115 |                     17 |    85.217391 |
| bcspwr04       |  0.063220 |                      265 |                     50 |    81.132075 |
| bcspwr05       |  0.082327 |                      435 |                     67 |    84.597701 |
| bcspwr06       |  0.338240 |                     1341 |                    121 |    90.976883 |
| bcspwr07       |  0.316466 |                     1487 |                    141 |    90.517821 |
| bcspwr08       |  0.450846 |                     1494 |                    135 |    90.963855 |
| bcspwr09       |  0.398750 |                     1663 |                    133 |    92.002405 |
| bcspwr10       |  1.801263 |                     5189 |                    285 |    94.507612 |
| bcsstk01       |  0.018724 |                       35 |                     27 |    22.857143 |
| bcsstk02       |  0.090255 |                       65 |                     65 |     0.000000 |
| bcsstk04       |  0.076396 |                       47 |                     54 |   -14.893617 |
| bcsstk05       |  0.062431 |                       28 |                     25 |    10.714286 |
| bcsstk06       |  0.189395 |                       47 |                     50 |    -6.382979 |
| bcsstk07       |  0.267027 |                       47 |                     50 |    -6.382979 |
| bcsstk09       |  0.620724 |                       62 |                    114 |   -83.870968 |
| bcsstk13       |  2.008737 |                     1250 |                    546 |    56.320000 |
| bcsstk19       |  0.275076 |                      567 |                     22 |    96.119929 |
| bcsstk23       |  1.161146 |                      449 |                    422 |     6.013363 |
| bcsstk24       |  3.585217 |                     3333 |                    251 |    92.469247 |
| bcsstk26       |  0.759668 |                      233 |                    245 |    -5.150215 |
| bcsstk27       |  1.154377 |                       56 |                     66 |   -17.857143 |
| bcsstk28       |  4.395130 |                      524 |                    412 |    21.374046 |
| bcsstk33       | 12.501105 |                      932 |                    748 |    19.742489 |
| bcsstm07       |  0.299051 |                       47 |                     55 |   -17.021277 |
| bcsstm27       |  1.378963 |                       56 |                     66 |   -17.857143 |
| can_1054       |  0.354900 |                     1030 |                    123 |    88.058252 |
| can_1072       |  0.358545 |                     1048 |                    178 |    83.015267 |
| can_144        |  0.044055 |                      142 |                     18 |    87.323944 |
| can_161        |  0.048374 |                       79 |                     18 |    77.215190 |
| can_187        |  0.053546 |                       63 |                     23 |    63.492063 |
| can_229        |  0.057518 |                      172 |                     37 |    78.488372 |
| can_24         |  0.007812 |                       21 |                      7 |    66.666667 |
| can_256        |  0.081824 |                      251 |                    123 |    50.996016 |
| can_268        |  0.082716 |                      263 |                     98 |    62.737643 |

### Matrizes assimetricas

| Nome da matriz | Tempo (s) | Largura de banda Inicial | Largura de banda final | Redução (\%) |
| -------------- | --------: | -----------------------: | ---------------------: | -----------: |
| arc130         |  0.058474 |                      125 |                    102 |    18.400000 |
| bp_0           |  0.268857 |                      820 |                    420 |    48.780488 |
| bp_1000        |  0.353051 |                      820 |                    479 |    41.585366 |
| bp_1200        |  0.394193 |                      820 |                    549 |    33.048780 |
| bp_1400        |  0.342148 |                      820 |                    547 |    33.292683 |
| bp_1600        |  0.385671 |                      820 |                    539 |    34.268293 |
| bp_200         |  0.268264 |                      820 |                    506 |    38.292683 |
| bp_400         |  0.303673 |                      820 |                    530 |    35.365854 |
| bp_600         |  0.294642 |                      820 |                    541 |    34.024390 |
| bp_800         |  0.315754 |                      820 |                    542 |    33.902439 |
