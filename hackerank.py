You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:

The sum of the lengths of all the words do not exceed 
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, .
The next  lines each contain a word.

Output Format

Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1





n = int(input())
words = []


#capture all given words from input
for i in range(0, n): 
    word = input()
    words.append(word)
    
distinct_words = []
already_exists = False 

for i in range(0, n):
     
    word = words[i]
    already_exists = False 
    
    for k in range(0, len(distinct_words)): 
        if word == distinct_words[k]: 
            already_exists = True
            break 
        
            
    if already_exists == False:         
        distinct_words.append(word)
            
            
print(len(distinct_words))
    
#count each occurence of distinct word

for i in range(0, len(distinct_words)): 
    word = distinct_words[i]
    count = 0 
    
    for k in range(0, len(words)): 
        
        if word == words[k]: 
            count = count + 1
            
    print(count,"", end = "")
