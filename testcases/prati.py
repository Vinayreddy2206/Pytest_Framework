# list1 = [1,2,3,4,5,6,7,8,9]
# result = [sum(list1[i:i+3]) for i in range(0,len(list1),3)]
# print(result)

# dict1 = {"d":10,"b":20,"c":15}
# items = list(dict1.items())
# print(items)
#
# for i in range(len(items)):
#     for j in range(i+1,len(items)):
#         if items[i][0] > items[j][0]:
#             items[i],items[j] = items[j],items[i]
#
# print(dict(items))


# dict1 = {"a":1,"b":2}
# dict2 = {"b":3,"d":4}
# dict3 = {}
# for key,value in dict1.items():
#     dict3[key] = value
# for key,value in dict2.items():
#     if key in dict3:
#         dict3[key] += value
#     else:
#         dict3[key] = value
# print(dict3)

dict1 = {"a":23,"c":34,"f":12,"g":89,"r":2}
#
# list1 =list(dict1.items())
# print(list1)
#
# for i in range(0,len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i][0]>list1[j][0]:
#             list1[i],list1[j] = list1[j],list1[i]
#
# print(dict(list1))

# dict1["d"] =40
# print(dict1)

# dict1 = {"a":1,"b":2}
# # dict2 = {"b":3,"c":4}
# # keey = " "
# #
# # for key in dict1:
# #     if key in dict2:
# #         keey = key
# # print(keey)

# dict1 = {"a":10,"b":20,"c":15}
# max_value = 0
# max_key = ""
# for key,value in dict1.items():
#     if value > max_value:
#         max_value = value
#         max_key = key
# print(max_key)

# list1 = ["a","b","c"]
# list2 = [1,2,3]
# dict1 = zip(list1,list2)
# print(dict(dict1))


# str1 = "My name is winteck"
# words = str1.split()
# reverse_words = words[::-1]
# reverse_str = " ".join(reverse_words)
# print(reverse_str)


str1 = "My name is winteck"
# # print(str1.split())
# dict1 = {}
# for i in str1:
#     dict1[i] = str1.count(i)
# print(dict1)

# leen = 0
# second_leen = 0
#
# list1 = str1.split()
# for i in list1:
#     if len(i) > leen:
#         second_leen = leen
#         leen = len(i)
#
#     if len(i) > second_leen and len(i) != leen:
#         second_leen = len(i)
#
# print(second_leen)

# str1 = "malayalam"
# rev_str = str1[::-1]
# if str1 == rev_str:
#     print("it is palandrom")
# else:
#     print("it's not a palandrom")

# list1 = []
#
# for i in range(2,100):
#     for j in range(2,i):
#         if i % j ==0:
#             break
#     else:
#         if len(list1) < 10:
#             list1.append(i)
#
# print(list1)

# """Generate fibanocci series till 100"""
#
# def fibbanic_series(limit):
#     fib_series = []
#     a,b =0,1
#     while a <=limit:
#         fib_series.append(a)
#         a,b =b,a+b
#     print(fib_series)
# fibbanic_series(100)

"""find given string is anagram or not"""

# def anagram_words(str1,str2):
#     str1 = str1.replace(" ","").lower()
#     str2 = str2.replace(" ","").lower()
#     if sorted(str1) == sorted(str2):
#         print("given word is anagram")
#     else:
#         print("given not is anagram")
# anagram_words("vinay","vinay")

str1 = "My name is winteck and my country is india"

"""Find most repeated substring in main string str1"""











