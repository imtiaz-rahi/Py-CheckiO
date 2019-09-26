# https://py.checkio.org/mission/calls-home/publications/StefanPochmann/python-3/125
def total_cost(C):
 t=p=m=0
 for c in C+('',):
    if c[:10]!=p:t+=m+max(0,m-100);m=0;p=c[:10]
    m-=-int('0'+c[20:])/60
 return t
