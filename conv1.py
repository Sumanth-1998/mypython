def ck(t):

    str=''
    dic={}
    for m in t:
        str=str+m[0]+'='+m[1]+","
        dic[m[0]]=m[1]
    str=str[0:len(str)-1]
    print(str)
    print(dic)



