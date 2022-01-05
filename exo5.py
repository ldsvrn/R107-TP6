
def isPalindrome(str):
    return str == str[::-1]


def toAlpha(string="e"):
    ret = ""
    for i in string.lower():
        if i.isalpha():
            ret += i
    return ret


def remSpecial(string):
    e = ('é', 'è', 'ë', 'ê')
    ret = ""
    for i in string:
        if i in e:
            ret += 'e'
        else:
            ret += i
    return ret


message = remSpecial(toAlpha(input("Entrez un mot ou une phrase: ")))

if isPalindrome(message):
    print("Le message est un Palindrome! ", message)
else:
    print("Le message n'est pas un Palindrome...", message)