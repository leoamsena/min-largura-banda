import random


def initialSolution(A, f):
    len_graph = len(A)
    print("len = ", len_graph)
    q = {}
    s = {}
    i = 1
    mark = {}
    for u in range(len_graph):
        mark[u] = False
    k = random.randint(0, len_graph - 1)
    mark[k] = True
    q[0] = k
    ql = 1
    f[k] = 0
    print("f1 = ", f)
    l = 0
    while l < len_graph:
        r = 0
        for i1 in range(ql + 1):
            print("i1 = ", i1)
            print("q = ", q)
            i = q[i1]

            for j1 in range(len(A[i])):

                j = A[i][j1]
                if not mark[j]:
                    r += 1
                    s[r] = j
                    mark[j] = True
        j_ = random.randint(0, ql)
        for jl in range(0, ql + 1):
            j = q[j_]
            l += 1
            f[j] = l
            print("f2 = ", f)
            j_ += 1
            if j_ >= ql - 1:
                j_ = 0
        print("s = ", s)
        q = s
        ql = r


A = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [
    1, 1, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]
f = {}
initialSolution(A, f)
print("f = ", f)
