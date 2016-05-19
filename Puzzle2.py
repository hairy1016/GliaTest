import sys

def main():
    inp = 1000
    m3 = 0
    m5 = 0
    result = 0
    ans = 0
    while 5**m5 <= inp:
        while result <=inp:
            ans = ans + result
            m3 = m3 + 1
            result = 3**m3 * 5**m5
        m3 = 0
        m5 = m5 + 1
        result = 3**m3 * 5**m5

    print(ans)

if __name__=="__main__":
    main()