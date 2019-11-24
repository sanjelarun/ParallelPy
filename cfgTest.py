from staticfg import CFGBuilder
import argparse
import networkx as nx
from networkx.drawing.nx_pydot import read_dot
import pydot


def detect_cycles():
    G = nx.DiGraph(read_dot('/home/asanjel/thesis/ParallelPy/output/exampleCFG'))
    print(G.nodes)
    C = nx.simple_cycles(G)
    for i in C:
        print(i)


def main():
    cfg = CFGBuilder().build_from_file(name='fib.py', filepath='/home/asanjel/thesis/ParallelPy/example.py')
    cfg.build_visual('output/exampleCFG', 'dot')
    detect_cycles()


if __name__ == "__main__":
    main()
