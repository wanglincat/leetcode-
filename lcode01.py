def leetcode1():
    res={i:1 for i in p},
    l  =1
    for i,j in zip(p,p[1:]):
       l=l+1 if(ord(j)-ord(i))%26==1 else 1
       res[j]=max(res[j],l)                          //利用ASCII码表差来筛选字符串的头尾，超过就增位
    return sum(res.values())                         //输出合集