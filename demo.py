import os
from dichotomy import nlr_gen
from dichotomy import BinaryTreeList
from dichotomy import LevelIterator


def run_with_range(a, b):
    print("{} - {}".format(a, b))

    tree_gv = "graph {\n"

    gen = nlr_gen(a, b, None)

    tree = BinaryTreeList()

    for center_node, parent_node in gen:
        tree.addnode(center_node, parent_node)
        if parent_node is not None:
            tree_gv += '\t"{}" -- "{}"\n'.format(parent_node, center_node)

    for idx, value in LevelIterator(tree):
        print(value)

    tree_gv += "}\n"
    f = open("./output/tree_{}-{}.gv".format(a, b), "w")
    f.write(tree_gv)
    f.close()
    print()


def main():
    print(os.getcwd())
    run_with_range(0, 10)
    run_with_range(1, 10)

if __name__ == '__main__':
    main()
