def print_formatted(number):
    
    whiteSpace = len('{0:b}'.format(number))
    
    for i in range(1,number+1):
        
        end0 = []
        end1 = []
        end2 = []
        end3 = []
        
        [end0.append(' ') for x in range(0,whiteSpace-len(str(i)))]
        [end1.append(' ') for x in range(0,whiteSpace-len(oct(i)[2:])+1)]
        [end2.append(' ') for x in range(0,whiteSpace-len(hex(i)[2:])+1)]
        [end3.append(' ') for x in range(0,whiteSpace-len('{0:b}'.format(i))+1)]

        print('',end=''.join(end0))
        
        print(i,end=''.join(end1))

        print(oct(i)[2:],end=''.join(end2))

        print(hex(i)[2:].upper(),end=''.join(end3))
        
        print('{0:b}'.format(i))
       
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
