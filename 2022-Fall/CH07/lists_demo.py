def main():
    # lists_demo()
    # lists_adding_demo()
    # lists_removing_demo()
    list_loop_demo()

def list_loop_demo():
   my_list = ['Quin', 'BB-8', 'Yogi', 'Maggie']

#    for doggo_name in my_list:
#        print(doggo_name) 

    
   my_list.reverse()
   print(my_list)

   my_list.sort()
   print(my_list)

def lists_removing_demo():
    my_list = ['Quin', 'BB-8', 'Yogi', 'Maggie']
    print(my_list)
    # my_list.remove('Yogi')
    # print(my_list)

    # my_list.pop(2)
    # print(my_list)

    my_list.pop()
    # my_list.pop()
    my_list.clear()
    print(my_list)

def lists_adding_demo():
    my_list = ['Quin', 'BB-8', 'Yogi', 'Maggie']
    my_list.append('Piper')
    my_list.insert(1, 'Josie')

    print(my_list)

def lists_demo():
    my_list = ["Quin", "BB-8", "Yogi", "Maggie"]
    # print(my_list)

    newest_doggo = my_list[1]
    print(newest_doggo)
    # print(my_list[-2])

    print(my_list[1:3])

    print(len(my_list))

main()
