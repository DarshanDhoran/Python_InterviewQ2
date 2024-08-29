# Write a python program to count frequency of words appearing in a string
def freq_words():
    str = input("Enter a string ")
    li =str.split()
    print(li)
    dict = {}
    for i in li:
        if i not in dict.keys():
            dict[i]=0
        dict[i] = dict[i] + 1
    print(dict)
freq_words()