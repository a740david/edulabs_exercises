import re

#1
# txt=input("enter the word: ")
#
# x = re.match("[A-Z][a-z]*", txt)
# print(x)

#"ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"
#"ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"
#2
# def match_dna():
#     txt=input("insert the text: ")
#     match = re.match('.*TATAA[ACGT]{3}TT.*', txt)
#     print(match)

#3
# def search_dna():
#     txt = input("insert the text: ")
#     search = re.search('TATAA[ACGT]{3}TT', txt)
#     print(search)

#4
# def match_two_digit():
#     txt=input("insert the text: ")
#     match=re.match('[1-9]{2}[a-zA-z]{2}.*$',txt)
#     print(match)

5
def two_tate_or_mor():
    txt = input("insert the text: ")
    match=re.match('.*TATAA[ACGT]{3}TT.*'+'.*TATAA[ACGT]{3}TT.*',txt)
    print(match)







if __name__=='__main__':

    # match_dna()
    # search_dna()
    # match_two_digit()
    two_tate_or_mor()

