import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import sys

G = nx.DiGraph()

def av2list(av):
    count = len(av) -1
    if(count % 2 != 0):
        print("invalid edges")
        exit(1)
    #for x in av:
    #    print(x)
    elist = []
    i = 1
    while i < count:
        elist.append((av[i], av[i+1]))
        i = i + 2
    #print("elist : ", elist)
    return elist

def main():
    elist = av2list(sys.argv)
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
    plt.savefig("bitree.png")
    plt.show()
if __name__ == "__main__":
    main()