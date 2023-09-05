# dependências externas:

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def reverse_lookup(d, v, all_occurrences=False):
    keys = []
    for k in d:
        if d[k] == v:
            if not all_occurrences:
                return k
            else:
                keys.append(k)
    return keys

# daqui pra baixo, cada inverted_histogram<N> refere-se à minha
# N-ésima tentativa de implementar da maneira mais simples possível
# a função inverted_histogram

def inverted_histogram1(s):
    d = histogram(s)
    inv = dict()

    for v in d.values():
        inv[v] = reverse_lookup(d, v, True) # desnecessário

    return inv



def inverted_histogram2(s):
    d = histogram(s)
    inv = dict()
    
    for v in d.values():
        inv[v] = []
        for k in d:
            if d[k] == v:
                inv[v].append(k)
    return inv



def invert_dict(d):
    inv = dict()

    for v in d.values():
        inv[v] = []
        for k in d:
            if d[k] == v:
                inv[v].append(k)
    return inv

def inverted_histogram3(s):
    return invert_dict(histogram(s))



print(inverted_histogram1("loopper"))
print(inverted_histogram2("loopper"))
print(inverted_histogram3("loopper"))
