import itertools

def main():
    list1 = ['a', 'b']
    list2 = ['c', 'd']
    for i in itertools.product(list1, list2):
        print(i)

if __name__ == '__main__':
    main()
