def convert_a_to_b(a, b, c):
    a = list(a)
    b = list(b)
    c = list(c)
    for idx, chr in enumerate(zip(a, b)):
        ch_a, ch_b = chr
        if ch_a != ch_b:
            if ch_b in c:
                a.insert(idx, ch_b)
                c.remove(ch_b)
            else:
                return False
    return a == b
    
if __name__ == '__main__':
    a = 'ab'
    b = 'acxb'
    c = 'cax'
    print(convert_a_to_b(a=a, b=b, c=c))
