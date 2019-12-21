import sys
def main():
    print("Input_file_1", sys.argv[1])
    print("Input_file_2",sys.argv[2])
    print("Output_file",sys.argv[3])
    f1 = open(sys.argv[1])
    f2 = open(sys.argv[2])
    fw = open(sys.argv[3],'w')
    count = 0
    while True:
        line1 = f1.readline().strip()
        if not line1:
            break
        line2 = f2.readline().strip()
        if not line1==line2:
            fw.write(line1+":"+line2)
            count +=1
    fw.write("COUNT"+str(count))
    f1.close()
    f2.close()
    fw.close()


if __name__=="__main__":
    main()