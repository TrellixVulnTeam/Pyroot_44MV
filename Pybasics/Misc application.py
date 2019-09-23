# Using list and Lambda /Function
import re
Table_list = ['Ara', 'Tha', 'Vig', 'Sud', 'Ani']   # consider it as list of table names

# print(len(Table_list))
# print(Table_list[1])


# def tablename_query(): # using function
#     for i in range(len(Table_list)):
#         querystring = 'Select * from ' + Table_list[i]
#         print(querystring)


# function call

# tablename_query()


alpha_list = ['klaus.schumacher@ampega.de', 'oliver.priggemeyer@hamburgtrust.de',
              'aertle@intreal.com', 'FK@deutsche-investment.com',
              'm.koerner@cronbank.de', 'huber@bankhaus-mayer.de',
              'abcib.frankfurt@bank-abc.com', 'jens-christian.meier@akabank.de',
              'frankfurt@juliusbaer.com', 'marcus.kruber@westendbank.de',
              ]
newlist = []
print(len(alpha_list))
pattern1 = r'@[a-zA-Z]*-?[a-zA-Z]*?.de'
pattern2 = r'@[a-zA-Z]*-?[a-zA-Z]*?.com'
pattern3 = r'@[a-zA-Z]*.com'
pattern4 = r'@[a-zA-Z]*.de'
for i in range(len(alpha_list)):
    if re.search(pattern1, alpha_list[i]):
        newlist.append(re.sub(pattern1, '', alpha_list[i]))
    elif re.search(pattern2, alpha_list[i]):
        newlist.append(re.sub(pattern2, '', alpha_list[i]))
    elif re.search(pattern3, alpha_list[i]):
        newlist.append(re.sub(pattern2, '', alpha_list[i]))
    elif re.search(pattern4, alpha_list[i]):
        newlist.append(re.sub(pattern4, '', alpha_list[i]))



print(newlist)
print(len(newlist))


# for i in range(len(alpha_list)):
#     print(alpha_list[i].replace('@gmail.com', ''))

