f = open('/data/lisa/data/NLU/wordnet3.0/train-WordNet3.0-relations+syn-anto_words.lst','r')

dat = f.readlines()
f.close()

idx2concept = {}
concept2idx = {}


for idx,i in enumerate(dat):
    idx2concept.update({idx:i[:-1]})
    concept2idx.update({i[:-1]:idx})

import cPickle

f = open('idx2concept.pkl','w')
g = open('concept2idx.pkl','w')

cPickle.dump(idx2concept,f,-1)
cPickle.dump(concept2idx,g,-1)
f.close()
g.close()

f = open('/data/lisa/data/NLU/wordnet3.0/WordNet3.0-definitions.txt','r')
dat = f.readlines()
f.close()

concept2def = {}


for idx,i in enumerate(dat):
    name,dum,defi = i[:-1].partition(' : ')
    concept2def.update({name:defi})


f = open('concept2def.pkl','w')

cPickle.dump(concept2def,f,-1)
f.close()


def parseline(line):
    lhs,rel,rhs = line.split('\t')
    lhs = lhs.split(' ')
    rhs = rhs.split(' ')
    return lhs,rel,rhs


f = open('/data/lisa/data/NLU/wordnet3.0/train-WordNet3.0-relations+syn-anto.txt','r')

dat = f.readlines()
f.close()

import scipy.sparse

posl = scipy.sparse.lil_matrix((len(idx2concept.keys()),len(dat)),dtype='float32')
posr = scipy.sparse.lil_matrix((len(idx2concept.keys()),len(dat)),dtype='float32')
poso = scipy.sparse.lil_matrix((len(idx2concept.keys()),len(dat)),dtype='float32')

for idx,i in enumerate(dat):
    lhs,rel,rhs = parseline(i[:-1])
    print lhs,rel,rhs
    posl[concept2idx[lhs[0]],idx]=1
    posr[concept2idx[rhs[0]],idx]=1
    poso[concept2idx[rel],idx]=1

f = open('WordNet3.0-train-lhs.pkl','w')
g = open('WordNet3.0-train-rhs.pkl','w')
h = open('WordNet3.0-train-rel.pkl','w')

cPickle.dump(posl,f,-1)
cPickle.dump(posr,g,-1)
cPickle.dump(poso,h,-1)

f.close()
g.close()
h.close()

f = open('/data/lisa/data/NLU/wordnet3.0/test-WordNet3.0-relations+syn-anto.txt','r')

dat = f.readlines()
f.close()

import scipy.sparse

posl = scipy.sparse.lil_matrix((len(idx2concept.keys()),len(dat)),dtype='float32')
posr = scipy.sparse.lil_matrix((len(idx2concept.keys()),len(dat)),dtype='float32')
poso = scipy.sparse.lil_matrix((len(idx2concept.keys()),len(dat)),dtype='float32')

for idx,i in enumerate(dat):
    lhs,rel,rhs = parseline(i[:-1])
    print lhs,rel,rhs
    posl[concept2idx[lhs[0]],idx]=1
    posr[concept2idx[rhs[0]],idx]=1
    poso[concept2idx[rel],idx]=1

f = open('WordNet3.0-test-lhs.pkl','w')
g = open('WordNet3.0-test-rhs.pkl','w')
h = open('WordNet3.0-test-rel.pkl','w')

cPickle.dump(posl,f,-1)
cPickle.dump(posr,g,-1)
cPickle.dump(poso,h,-1)

f.close()
g.close()
h.close()
    