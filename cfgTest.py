from staticfg import CFGBuilder
import argparse
import networkx as nx
from networkx.drawing.nx_pydot import read_dot
import pydot


## TODO Convert a dot file into each multiple subgraph
def convertDotToMultpleFile():
    with open("output/exampleCFG") as fp:
        count = 0
        for num, line in enumerate(fp, 1):
            count = count + 1
            if "subgraph" in line:
                file_path = "output/subgraph" + str(count) + ".dot"
                new_file = open(file_path, "w+")
                new_line = line.replace("subgraph", "digraph")
                new_file.write(new_line)
                while True:
                    next_line = next(fp)
                    new_file.write(next_line)
                    if "}" in next_line:
                        break
                new_file.close()


def detect_cycles():
    G = nx.DiGraph(read_dot('/home/asanjel/thesis/ParallelPy/output/subgraph20.dot'))
    print(G.adj)
    C = nx.simple_cycles(G)
    for i in C:
        print(i)


def main():
    # cfg = CFGBuilder().build_from_file(name='fib.py', filepath='/home/asanjel/thesis/ParallelPy/example.py')
    # cfg.build_visual('output/exampleCFG', 'dot')
    convertDotToMultpleFile()
    detect_cycles()


if __name__ == "__main__":
    main()
