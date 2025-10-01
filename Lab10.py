from nltk import Nonterminal, PCFG

# Define toy PCFG 1
toy_pcfg1 = PCFG.fromstring("""
  S -> NP VP [1.0]
  VP -> V NP [0.5] | VP PP [0.5]
  PP -> P NP [1.0]
  V -> "saw" [1.0]
  NP -> "John" [0.5] | "Mary" [0.5]
  P -> "with" [1.0]
""")

# Define toy PCFG 2
toy_pcfg2 = PCFG.fromstring("""
  S -> NP VP [1.0]
  VP -> V NP [0.7] | V [0.3]
  V -> "saw" [1.0]
  NP -> "John" [0.5] | "Mary" [0.5]
""")

tokens = "Joseph has seen John with the telescope.".split()
print("Grammar 1:")
print(toy_pcfg1)

tokens1 = "Joseph saw John with the telescope.".split()
print("\nGrammar 2:")
print(toy_pcfg2)
