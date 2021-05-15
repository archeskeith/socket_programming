def ifVowel(word):
	#prompts the function if the first letter of the word is a Vowel
	newword = ""
	for i in range(len(word)):
		newword+=word[i]
	if(word[len(word)-1]!='w' or word[len(word)-1]!='y'):
		newword+="yay"
	else:
		newword+="ay"
	return newword

def ifY(word):
	#prompts the function if the first letter of the word is Y/y
	newword = ""
	if(len(word)>1):
		for i in range(1,len(word)):
			newword+=word[i]

		if(word[len(word)-1]!='w' or word[len(word)-1]!='y'):

			newword+="yay"

		else:
			newword+='ay'
	else:
		newword+=word[0]
	return newword

def ifCons(word,vowels):
	#prompts the function if the first letter of the word is a Consonant
	newword = ""
	if(len(word)>1):
		if(word[1]!='y' or word[1]!='Y'):
			cons = ""
			index = 0 
			for i in range(len(word)):
				if(word[i] not in vowels and word[i]!='y'):
					cons+=word[i]
					index = i
				else:
					break


			for i in range(index+1,len(word)):
				newword+=word[i]

			newword+=cons
			newword+="ay"

		elif(word[1]=='y' or word[1]=='Y'):
			for i in range(1,len(word)):
				newword+=word[i]
			newword+=word[0]
			newword+="ay"
	else:
		newword+=word[0]
	return newword

def wordperword(word):

	#checks which function each word is suitable to be in 
	vowels = ['a','e','i','o','u','A','E','I','O','U']

	if(word[0] in vowels):
		return ifVowel(word)
		
	elif(word[0]=='y'):
		return ifY(word)
	else:
		return ifCons(word,vowels)

def main():
	fullsentence = input()
	arry = fullsentence.split()
	newArry = []

	#converts each and every word in the loop
	for x in arry:
		newArry.append(wordperword(x))
	

	for y in newArry:
		print(y,end=" ")
	


#REFERENCES:
#A quick Guide for translating to Pig Latin with Examples: https://bunnystudio.com/blog/library/translation/a-quick-guide-for-translating-to-pig-latin-with-examples/#:~:text=Pig%20Latin%20is%20a%20pseudo-language%20or%20argot%20where,word%20%E2%80%98pig%E2%80%99%20would%20become%20igp%2Bay%20which%20becomes%20igpay.
#Python Socket Programming Tutorial: https://www.youtube.com/watch?v=3QiPPX-KeSc