const initialSolution = (A) => {
  const len_graph = A.length;

  let f = new Array(len_graph);

  let q = new Array(len_graph);
  q = q.map(() => 0);

  let s = new Array(len_graph);
  s = s.map(() => 0);
  let i = 1;
  let mark = Array(len_graph);
  mark = mark.map(() => false);
  let k = Math.round(Math.random() * (len_graph - 1));
  mark[k] = true;
  q[0] = k;
  let ql = 1;
  f[k] = 0;
  let l = 0;
  while (l < len_graph + 1) {
    let r = 0;
    for (let i1 = 0; i1 < ql; i1 += 1) {
      i = q[i1];
      for (let j1 = 0; j1 < A[i].length; j1 += 1) {
        let j = A[i][j1];
        if (!mark[j]) {
          r += 1;
          s[r] = j;
          mark[j] = true;
        }
      }
    }
    let j_ = Math.round(Math.random() * ql);
    for (let jl = 0; jl < ql + 1; jl += 1) {
      let j = q[j_];
      l += 1;
      f[j] = l;
      j_ += 1;
      if (j_ >= ql - 1) j_ = 0;
    }
    const newVet = [];
    for (let aux = 0; aux < len_graph; aux += 1) {
      if (q[aux] !== undefined) newVet[aux] = q[aux];
      if (s[aux] !== undefined) newVet[aux] = s[aux];
      if (q[aux] === undefined && s[aux] === undefined) newVet[aux] = undefined;
    }
    q = newVet;
    ql = r;
  }

  console.log(f);
};
const A = [
  [1, 0, 1, 0, 1],
  [0, 1, 1, 1, 0],
  [1, 1, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
];
const f = [];
initialSolution(A, f);
