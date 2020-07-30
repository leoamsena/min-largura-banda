const initialSolution = (A, f) => {
  const len_graph = A.length;
  let q = new Array(len_graph);
  q = q.map(() => 0);

  let s = new Array(len_graph);
  s = s.map(() => 0);
  let i = 1;
  let mark = Array(len_graph);
  mark = mark.map(() => false);
  let k = Math.random() * (len_graph - 1);
  mark[k] = true;
  q[0] = k;
  let ql = 1;
  f[k] = 0;
  let l = 0;
  while (l < len_graph) {
    let r = 0;
    for (let i1 = 0; i1 < ql + 1; i += 1) {
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
    let j_ = MATH.random(ql);
    for (let jl = 0; jl < ql + 1; jl += 1) {
      let j = q[j_];
      l += 1;
      f[j] = l;
      j_ += 1;
      if (j_ >= ql - 1) j_ = 0;
    }
    q = s;
    ql = r;
  }
}
A = [
  [1, 0, 1, 0, 1],
  [0, 1, 1, 1, 0],
  [1, 1, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
];
f = [];
initialSolution(A, f);
