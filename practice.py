import re, collections
def get_stats(vocab):
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i],symbols[i+1]] += freq
    return pairs
def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    print('bigram:',bigram)
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        print('w_out',w_out)
        v_out[w_out] = v_in[word]
        return v_out
vocab = {'l o w </w>' : 5, 'l o w e r </w>' : 2, 'newest</w>':6,'widest</w>':3}
num_merges = 10
for i in range(num_merges):
    pairs = get_stats(vocab)
    print('pairs\n',pairs)
    best = max(pairs, key=pairs.get)
    vocab = merge_vocab(best, vocab)
    print("vocab\n",vocab)
    print('.',re.escape('.'))
