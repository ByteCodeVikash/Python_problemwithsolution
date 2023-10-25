def character(text):
   
    char_counts = {}

    
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    
    sorted_char_counts = sorted(char_counts.items())

    return sorted_char_counts

if __name__ == "__main__":
    
    text = "This is a sample text. This text contains some sample words. Sample words are repeated to test the program."

    
    char = character(text)

    
    print("Character:")
    for char, count in char:
        print(f"('{char}' {count})", end=' ')
