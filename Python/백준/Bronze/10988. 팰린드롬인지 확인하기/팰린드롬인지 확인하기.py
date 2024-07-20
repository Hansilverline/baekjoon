word = input()
reversed_word = word[::-1]
is_palindrome = True

if len(word) < 1 : 
    is_palindrome = False

for i in range(int(len(word)/2)) :
    if word[i] != reversed_word[i] : 
        is_palindrome = False
        break
    else :
        is_palindrome = True

print(int(is_palindrome))