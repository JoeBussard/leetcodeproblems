    
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        symbols = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse = dict()
        for i in range(26):
            morse[alpha[i]] = symbols[i]
        
        uniques = set()
        for word in words:
            transformed = ""
            for letter in word:
                transformed += morse[letter]
            uniques.add(transformed)
        return len(uniques)
        
