import string
def main():
    count = 0
    tokens = set()
    with open('Squad1_BPE_Input_File.txt','r',encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line = line.strip(string.punctuation)
            for word in line.split(" "):
                count += 1
                tokens.add(word)
    to_be_ana = ["bpe_vocab_5000_lower_xsh_result.txt",
                 "bpe_vocab_10000_lower_xsh_result.txt",
                 "bpe_vocab_30000_lower_xsh_result.txt",
                 ]
    for file_name in to_be_ana:
        new_file_name = file_name[:-4]+"_vocab.txt"
        fr = open(file_name,'r',encoding='utf-8')
        fw = open(new_file_name,'w',encoding='utf-8')
        fw.write("Squad1 tokens："+str(count)+'different tokens：'+str(len(tokens))+'\n')
        for frline in fr:
            frline = frline.strip().split()[1:]
            frline = "".join(frline)
            frline = frline.split(':')
            print("token",frline[0])
            if frline[0] in tokens:
                fw.write(" ".join(frline)+'\n')
        fw.close()
        fr.close()

if __name__ == "__main__":
    main()