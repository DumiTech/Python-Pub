import library

print("Welcome to the secret auction program")

should_finish = False

total_persons = []
values_list = []
key_list = []

def add_new_person(name, bid, shall_continue):
    new_person = {}
    
    name = input("What is your name?\n")
    bid = int(input("What's your bid?\n $"))
    new_person = {
        name:bid
    }
    # print(new_person) #test
    total_persons.append(new_person)
    # print(new_person.keys())    #test
    # print(new_person.values())  #test
    
    values_list.append(new_person[name])
    # print(values_list)    #test
    
    
    for key in list(new_person.keys()):
        key_list.append(key)
    # print(key_list)   #test
    
    increment = 0
    
    shall_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if shall_continue == "yes": 
        should_finish = False
        print("\n"*50)
        add_new_person(name, bid, shall_continue)
    elif shall_continue == 'no':
        max = values_list[0]  #assuming that the first item is max
        for value in values_list:
            if value > max:
                max = value
                increment += 1
        print(f"The winner is {key_list[increment]} with a bid of ${max}")
        
        # print(total_persons)    #test
        should_finish = True
    else:
        print("There is 100% percentage that you did something wrong")
        print("This is the case where no one alter the code before me, lol.")
    

add_new_person(name='', bid='', shall_continue='')