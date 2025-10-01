from nltk import CFG
toy_pcfg1 = CFG.fromstring("""
    S -> A B
    S -> C D
    A -> 'a'
    B -> 'b'
    C -> 'c'
    D -> 'd'
""")
import nltk
nltk.download('treebank')
from nltk.corpus import treebank
from nltk import treetransforms
from nltk import induce_pcfg
from nltk.parse import pchart
pcfg_prods = toy_pcfg1.productions()
pcfg_prod = pcfg_prods[2]
print('A PCFG production:', pcfg_prod)
print('pcfg_prod.lhs() =>', pcfg_prod.lhs())
print('pcfg_prod.rhs() =>', pcfg_prod.rhs())
print("Induce PCFG grammar from treebank data:")
productions = []
for item in treebank.fileids()[:2]:
    for tree in treebank.parsed_sents(item):
        # perform optional tree transformations, e.g.:
        tree.collapse_unary(collapsePOS = False)# Remove branches A-B-C into A-B+C
        tree.chomsky_normal_form(horzMarkov = 2)# Remove A->(B,C,D) into A->B,C+D->D
        productions += tree.productions()
from nltk import Nonterminal
S = Nonterminal('S')
grammar = induce_pcfg(S, productions)
print(grammar)
