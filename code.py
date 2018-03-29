import networkx as nx
from random import randint, shuffle
import sys

fil = input()
cnt = input()
while (cnt != fil):
    cnt += 1
    file = open('test' + str(cnt), 'w+')
    n, m = randint(9000, 10000), randint(10000, 100000)
    while(10*n<m):
        n, m = randint(9000, 10000), randint(10000, 100000)
    print cnt
    file.write(str(n) + '\n')
    #k= randint(1, 100)
    #file.write(str(k) +'\n')
    file.write(str(m) + '\n')
    # g=nx.generators.full_rary_tree(2,n)
    deg = [0 for i in xrange(n + 1)]
    # parent=[i for i in xrange(n+1)]
    adj = [[] for i in xrange(n + 1)]
    for i in xrange(2, n + 1):
        p = randint(i - 15, i - 1)
        if p < 1:
            p = randint(1, i - 1)
        file.write(str(p) + ' ' + str(i) +' '+str(randint(1,1000))+ '\n')
        adj[p].append(i)
        adj[i].append(p)
        deg[p] += 1
        deg[i] += 1
    nd = 1
    for i in xrange(m - n + 1):
        val=i%3
        if val==0:
            p,q = randint(1, n / 4),randint(n / 4 + 1, 2*n/4)
            if p != q:
                while (p in adj[q]) or deg[p] > 25 or deg[q] > 25:
                    p,q = randint(1, n / 4),randint(n / 4 + 1, 2*n/4)
        elif val==1:
            p,q = randint(2*n / 4 + 1, 3*n/4),randint(2*n / 4 + 1, 3*n/4)
            if p != q:
                while (p in adj[q]) or deg[p] > 25 or deg[q] > 25:
                    p,q = randint(2*n / 4 + 1, 3*n/4),randint(2*n / 4 + 1, 3*n/4)
        else:
            p,q = randint(3*n / 4+ 1, n),randint(3*n / 4 + 1, n)
            if p != q:
                while (p in adj[q]) or deg[p] > 25 or deg[q] > 25:
                    p,q =  randint(3*n / 4+ 1, n),randint(3*n / 4 + 1, n)

        '''
        if nd>n:
            nd=1
        set=0
        p=randint(nd-300,nd-1)
        if p<1:
            p=randint(nd+1,nd+300)
            set=1
        while (nd in adj[p]) or deg[p]>20 or deg[nd]>20:
            if set==1:
                p=randint(nd+1,nd+300)
            else:
                p=randint(nd-300,nd-1)'''
        str1=str(p)+' '+str(q)+' '+str(randint(1,1000))+'\n'
        file.write(str1)
        deg[p] += 1
        deg[q] += 1
        adj[p].append(q)
        adj[q].append(p)
    file.close()

    '''
    print g.edges()
    e=g.edges()
    shuffle(e)
    for i,j in e:
        file.write(str(i+1)+' '+str(j+1)+'\n')
    lt=len(e)
    for i in xrange(m-lt):
        p,q=randint(1,n),randint(1,n)
        file.write(str(p)+' '+str(q)+'\n')
    file.close()'''
