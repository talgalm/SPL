import sys
from DTO import Hat, Supplier, Order
from Repository import repo


# Configuration fil


def main(args):
    repo.create_tables()
    parse_config("config.txt")
    parse_orders("orders.txt")
    #write output


def parse_config(config):
    with open(config) as inputfile:
        inputfile.readline()
        for line in inputfile:
            if len(line.split(',')) == 4:
                repo.hats.insert(
                    Hat(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
            else:
                    repo.supplier.insert(Supplier(line.split(',')[0], line.split(',')[1]))


def parse_orders(orders):
    mylist = list()
    with open(orders) as ordersFile:
        ordersFile.readline()
        i = 0
        for line in ordersFile:
            arg0 = line.split(',')[0]
            arg1 = line.split(',')[1]
            arg1 = arg1[0:len(arg1)-1]
            order = Order(i ,arg0 , arg1)
            i = i + 1
            repo.orders.insert(order)
            mylist.append(arg1)

        for topping in mylist:
            min = repo.hats.min(topping)[0]
            repo.hats.update(min,topping)
            repo.hats.deleteZero()

if __name__ == '__main__':
    main(sys.argv)
