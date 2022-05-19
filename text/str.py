vowels='aeiou'
str='energy'
count={}.fromkeys(vowels,0)
for ch in str:
    if ch in count:
        count[ch]+=1

print(count)

def palindrom(x):
    rev=x[::-1]
    if x==rev:
        print('yes palindrom!')
    else:
        print('nope..! not a palindrom')

palindrom('racecar')

def word_str(str):
    count=1
    for i in range(len(str)):
        if str[i]==' ':
            count+=1
    
    print(count)
word_str('hello world! how are you')