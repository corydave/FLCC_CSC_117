def main():
    loop_demo_list()
    loop_demo_range()

def loop_demo_range():

    for x in range(20):
        # Print [0, 20)
        print(x, ' ', end='')

    for x in range(10, 30):
        # Print [10, 30)
        print(x)


    for x in range(10, 30, 3):
        print(x)

def loop_demo_list():
    children = ["Dave", "John", "Jennifer", "Katie"]

    for name in children:
        print(name)

main()
