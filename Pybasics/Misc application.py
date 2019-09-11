# Using list and Lambda /Function

Table_list = ['Ara', 'Tha', 'Vig', 'Sud', 'Ani']   # consider it as list of table names
# print(len(Table_list))
# print(Table_list[1])


def tablename_query(): # using function
    for i in range(len(Table_list)):
        querystring = 'Select * from ' + Table_list[i]
        print(querystring)


# function call

tablename_query()


