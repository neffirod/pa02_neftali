#Neftali Rodriguez, 05/06/17



def isPangram(sentence):
    sentence.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in alpha:
        if i not in sentence:
            return False
        else:
            return True



       
def isPalindrome(text): 
    text1 = text.lower()
    text2 = text1.replace(" ", "").replace(",", "").replace(".", "").replace("'", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "")
    y = text2[::-1]
    if text2==y:
        return True
    else:
        return False

        

def findVowel(text):
	text = list(text)
	vowel= ['a','e', 'i', 'o']
	cons = ['b', 'c', 'd', 'f', 'g', 'h','j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's','t', 'v', 'w', 'x', 'z']
	if ('u') in text:
		if ('q') in text and text.index('u') == text.index('q') + 1:
			cons.append('u')
		else:
			vowel.append('u')
	else:
		vowel = vowel
		cons = cons
	if ('y') in text:
		if text.index('y') == 0:
			cons.append('y')
		else:
			vowel.append('y')
	else:
		vowel= vowel
		cons=cons
	for i in text:
		if i in vowel:
			pos = text.index(i)
			newword= text[pos:] + text[:pos] + ['ay']
			final = ''.join(newword)
			return(final) 

    




def firstVowel(text):
    text = list(text)
    vowel = ['a','e', 'i', 'o', 'u']
    if text[0] in vowel:
        new = text + ['way']
        fin= ''.join(new)
        return(fin)
    else:
        return(findVowel(text))



def pigWord (text):
    for i in text:
        if text == text.upper():
            new = text.lower()
            new1 = (firstVowel(new))
            return(new1.upper())
        elif text[0]== text[0].upper():
            low=text.lower()
            low1=firstVowel(low)
            w=low1[0].upper() + low1[1:]
            return (w)
        if text== text.lower():
            return (firstVowel(text))
        else:
            return (text)

def pigLatin (text):
    text=text.split(' ')
    nonalpha= ('!,?,:')

    emptys=''
    for i in text:
        if i.isalpha():
            emptys+= pigWord(i)
        else:
            emptys += pigWord(i)
        emptys += ' '
    emptys= emptys[:-1]
    return emptys


