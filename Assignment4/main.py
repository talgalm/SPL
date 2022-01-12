import sys

from DTO import Hat, Supplier, Order
from Repository import _Repository


# Configuration fil


def main(args):
    repo = _Repository()
    repo.create_tables()
    configFile = args[3]
    with open(configFile) as inputfile:
        inputfile.readline()
        for line in inputfile:
            if len(line.split(',')) == 4:
                repo.hats.insert(
                    Hat(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
            else:
                repo.supplier.insert(Supplier(line.split(',')[0], line.split(',')[1]))
    configFile = args[4]
    with open(configFile) as inputfile:
        for line in inputfile:
            repo.orders.insert(Order(line.split(',')[0], line.split(',')[1], line.split(',')[2]))


if __name__ == '__main__':
    main(sys.argv)
