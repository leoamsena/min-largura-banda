const initialSolution = (lista_ajacencia) => {
    const len_graph = lista_ajacencia.length;

    let guarda_labels = new Array(len_graph);

    let sequenica_nos_visitados = new Array(len_graph);
    sequenica_nos_visitados = sequenica_nos_visitados.map(() => 0);

    let s = new Array(len_graph);
    s = s.map(() => 0);
    let i = 1;
    let no_visitado = Array(len_graph);
    no_visitado = no_visitado.map(() => false);
    let k = Math.round(Math.random() * (len_graph - 1));
    no_visitado[k] = true;
    sequenica_nos_visitados[0] = k;
    let cardinalidade_vertice = 1;
    guarda_labels[k] = 0;
    let label = 0;
    while (label < len_graph + 1) {
        let marcados_true_ultima_iteracao = 0;
        for (let i1 = 0; i1 < cardinalidade_vertice; i1 += 1) {
            i = sequenica_nos_visitados[i1];
            for (let j1 = 0; j1 < lista_ajacencia[i].length; j1 += 1) {
                let j = lista_ajacencia[i][j1];
                if (!no_visitado[j]) {
                    marcados_true_ultima_iteracao += 1;
                    s[marcados_true_ultima_iteracao] = j;
                    no_visitado[j] = true;
                }
            }
        }
        let j_ = Math.round(Math.random() * cardinalidade_vertice);
        for (let jl = 0; jl < cardinalidade_vertice + 1; jl += 1) {
            let j = sequenica_nos_visitados[j_];
            label += 1;
            guarda_labels[j] = label;
            j_ += 1;
            if (j_ >= cardinalidade_vertice - 1) j_ = 0;
        }
        const newVet = [];
        for (let aux = 0; aux < len_graph; aux += 1) {
            if (sequenica_nos_visitados[aux] !== undefined) newVet[aux] = sequenica_nos_visitados[aux];
            if (s[aux] !== undefined) newVet[aux] = s[aux];
            if (sequenica_nos_visitados[aux] === undefined && s[aux] === undefined) newVet[aux] = undefined;
        }
        sequenica_nos_visitados = newVet;
        cardinalidade_vertice = marcados_true_ultima_iteracao;
    }

    console.log(guarda_labels);
};
const lista_ajacencia = [
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
];
const guarda_labels = [];
initialSolution(lista_ajacencia, guarda_labels);