def calculate_love_score(name1,name2):
    combined_name = (name1+name2).lower()
    letters_to_count = {'t': 0, 'r': 0, 'u': 0, 'e': 0, 'l': 0, 'o': 0, 'v': 0}
    for char in combined_name:
        if char in letters_to_count:
            letters_to_count[char]+=1 

            
    true_count = letters_to_count['t'] + letters_to_count['r'] + letters_to_count['u'] + letters_to_count['e']
    love_count = letters_to_count['l'] + letters_to_count['o'] + letters_to_count['v'] + letters_to_count['e']
    
    love_score = int(str(true_count)+ str(love_count))
    print(love_score)
        
calculate_love_score("Kanye West", "Kim Kardashian")