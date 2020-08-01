import networkx as nx
import random
from typing import Any
import heapq
from itertools import combinations
from typing import Tuple

from pymhlib.solution import SetSolution, TObj
from pymhlib.settings import get_settings_parser
from pymhlib.scheduler import Result
from pymhlib.demos.graphs import create_or_read_simple_graph


class VNSBandMinimizationIntsnace():
    """
    Attributes
        - graph: the graph for which we want to find a minimum vertex cover
        - n: number of nodes
        - m: number of edges
    """
    def __init__(self, name: str):
        """Create or read graph with given name."""
        self.graph = create_or_read_simple_graph(name)
        self.n = self.graph.number_of_nodes()
        self.m = self.graph.number_of_edges()

    def __repr__(self):
        """Write out the instance data."""
        return f"n={self.n} m={self.m}\n"


class VNSBandMinimizationSolution(SetSolution):
    to_maximize = False
    def __init__(self, inst: VertexCoverInstance):
        super().__init__(inst=inst)

    def remove_redundant(self) -> bool:
        """Scheduler method that checks for each node in the current vertex cover if it can be removed.
        The nodes are processed in random order.
        :return: True if solution could be improved
        """
        s = self.s
        x = list(s)
        random.shuffle(x)
        for u in x:
            for v in self.inst.graph.neighbors(u):
                if v not in s:
                    break
            else:
                s.remove(u)
        if len(s) < len(x):
            self.invalidate()
            return True
        return False

    def shaking(self, par: Any, _result: Result):
        """Add par so far unselected nodes and apply remove_redundant."""
        s = self.s
        x = set(range(self.inst.n)).difference(s)
        to_add = random.sample(x, max(len(x), par))
        for u in to_add:
            s.add(u)
        self.remove_redundant()
