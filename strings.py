
# Strings are sequence of character enclosed with quotes,
# ex : 'Melwin', "Melwin Dsouza", "1234" etc...

# 1. Creation of strings
# a) single line strings
s1 = 'Melwin'
s2 = "This is python programming language"
print(s1)
print(s2)
# b) multi line strings
s3 = '''
Hello World !!!
This is melwin here.
Welcome to python programming lecture.
''' 
print(s3)

# 2. Accessing the string characters
s4 = "Melwin Dsouza"
print(s4)
print("Starting leter : ",s4[0])
print("Ending letter : ",s4[-1])
print("At index 4 : ",s4[4])
print("Staring three letters : ",s4[:3])
print("Ending three letters : ",s4[-3:])
print("Excluding start three letters : ",s4[3:])
print("Excluding end three letters : ",s4[:-3])
print("From index 3 to 6 : ",s4[3:7])

# Methods in strings in python
s5 = "This is a coding lecture"
print(s5)
# 1. len(str) - returns the no of character in the string
print("The length of above string is : ",len(s5))
# 2. lower() - return a copy of the string converted to lowercase.
print("The above string in lowercase is : ",s5.lower())
# 3. upper() - return a copy of the string converted to uppercase.
print("The above string in lowercase is : ",s5.upper())
# 4. capitalize() - Return a capitalized version of the string. More specifically, make the first character have uppercase and the rest lowercase.
print("The above string in capitalize is : ",s5.capitalize())
print(s5)
# 5. title() - Return a version of the string where each word is titlecased.More specifically, words start with uppercased characters and all remainingcased characters have lower case.
print("The above string in title  is : ",s5.title())
# 6. strip() - Return a copy of the string with leading and trailing whitespace removed.
s6 = "Python   "
print(s6, len(s6))
print("The strip of above string is : ",s6.strip(),len(s6.strip()))
# 7. split() - Return a list of the substrings in the string, using sep as the separator string.
s7 = "Java is coding language"
print(s7)
print("Spliting the above string gives : ",s7.split())
print("Spliting the above string gives : ",s7.splitlines())
# 8. join(list,tuple,etc..) - Concatenate any number of strings.
list1 = ["M","e","l","w","i","n"]
print(list1)
print("Joining the caharacters in the above list to form a string gives : ","".join(list1))
s8 = "This is a good lecture"
print(s8)
# 9. startswith(sub) - Return True if the string starts with the specified substring, False otherwise.
print("Is string starts with Python : ",s8.startswith("Python"))
# 10. endsswith(sub) - Return True if the string endss with the specified substring, False otherwise.
print("Is string starts with lecture : ",s8.endswith("lecture"))
s9 = "melwin123"
print(s9)
# 11. isdigit() - returns true if all the character in the string is digit else false
print("Is all digits in the above string : ",s9.isdigit())
# 12. isalpha() - returns true if all the character in the string is alphabet else false
print("Is all alphabet in the above string : ",s9.isalpha())
# 13. isalnum() - returns true if there is a mixture od alphabet and digits in the given string else false
print("Is there a mixture of alpha and num in the above string : ",s9.isalnum())
s10 = "Python is best progamming language. Python is beginner friendly also"
print(s10)
# 14. count(sub) - Counts all occurrence of given sub string
print("The occurrence of 'Python' in the above string is : ",s10.count("Python"))
# 15. find(sub) - returns the index of first occurrence of given substrings
print("The index of 'Python' in the above string is : ",s10.index("Python"))
# 16. replace(old_sub,new_sub) - 
s11 = "Java is my favourite language"
print(s11)
print("After replacing java with python the new string is : ",s11.replace("Java","Python"))

# Some important questions that can be asked in the interview

# 1. Reverse a string
s1 = "Mumbai"
print("The orginal string is : ",s1)
print("After the reversal the string is : ",s1[::-1])

# 2. check palindrome or not
s1 = "madam"
print("The string is : ",s1)
s2 = s1[::-1]
if s1 == s2:
    print("string is palindrome")
else:
    print("string is not palindrome")

# 3. check vowles in the string
s1 = "apple"
sum = 0
for ch in s1:
    if ch in "aeiou":
        sum = 1
if sum == 1:
    print("Vowels is present")
else :
    print("Vowels is not present")

# 4. find the length of string without len function
s1 = "Melwin"
print("The string is : ",s1)
count = 0
for ch in s1:
    count = count + 1
print("The length of above string is : ",count)

# 5. Count Occurrences of Each Character
s1="Banana"
print("the string is : ",s1)
freq = {}
for ch in s1:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

# 6. Find first non repating character
s1 = "Apple"
print("the string is : ",s1)
for ch in s1:
    if s1.count(ch)==1:
        print(ch)
        break

# 7. Remove repeating character while maintaining the sequence
s1 = "Programming"
print("The strings is : ",s1)
remove = ""
for ch in s1:
    if ch not in remove:
        remove = remove + ch
print(remove)

# 8. Check anagrams bwteen two strings ("Anagrams means same character with same frequency")
s1 = "listen"
s2 = "silent"
print("The String1 is : ",s1)
print("The String2 is : ",s2)
if sorted(s1) == sorted(s2):
    print("Anagrams")
else :
    print("Not Anagrams")

# 9. Find most frequent character in the string
s1 = "mississpi"
print("The string is : ",s1)
freq = {}
for ch in s1:
    if ch in freq:
        freq[ch]+=1
    else :
        freq[ch]=1
print('The most frequent character is :',max(freq)," with no of times equal to :",freq[max(freq)])

# 10. Compress String 
s1 = "aaabbcdddeffe"
compressed = ""
count = 1
for i in range(len(s1)):
    if i+1<len(s1) and s1[i]==s1[i+1]:
        count = count + 1
    else :
        compressed += s1[i] + str(count)
        count = 1
print(compressed)

