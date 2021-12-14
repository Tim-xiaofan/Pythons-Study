#!/usr/bin/python3
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import sys
import argparse
import matplotlib
matplotlib.use('TkAgg')

class MyParser(argparse.ArgumentParser):
        def error(self, message):
            print(message)
            self.print_help()
            print("example : ./{}".format(self.prog), " --edges \"(C,B) (C,D) (B,A) (D,E)\"\t")
            exit(2)

def get_option():
    parser = MyParser(description='draw a tree accordding to edges')
    parser.add_argument('-e', '--edges', metavar='edges', required=True, 
                        dest='edges',help='edges of the tree')
    parser.add_argument('-i', '--image', metavar='image', required=False, 
                        dest='image',help='image file name, defall is \"tree.png\"')
    args = parser.parse_args()
    return args

def edge2tuple(e):
    e = e.replace("(", "")
    e = e.replace(")", "")
    e = e.replace(" ", "")
    e = e.split(',')
    #print("e:", e)
    return (e[0], e[1])
    
#av = (C,B) (C,D) (B,A) (D,E)
def av2list(edges):
    temp = edges.split()
    elist = []
    for i in temp:
        elist.append(edge2tuple(i))
    return elist

def main():
    args = get_option()
    G = nx.DiGraph()
    elist = av2list(args.edges)
    #elist = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
    print("elist : ", elist)
    G.add_edges_from(elist) 
    # write dot file to use with graphviz
    # run "dot -Tpng test.dot >test.png"
    #nx.nx_agraph.write_dot(G,'test.dot')
    # same layout using matplotlib with labels
    plt.title('draw_networkx')
    pos=graphviz_layout(G, prog='dot')
    nx.draw(G, pos, with_labels=True, arrows=False)
    plt.savefig("tree.png")
    plt.show()
if __name__ == "__main__":
    main()
