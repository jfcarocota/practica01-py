the_list = []

#for x in range(10):
#    the_list.append(1 if x % 2 == 0 else 0)
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)
