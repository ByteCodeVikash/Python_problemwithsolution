#write a python program to find the most common elements and their count of a specific text ?


def elements(text):
    
    words = text.split()

    
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sort = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    return sort

if __name__ == "__main__":
    #  (you can replace this with your specific text)
    text = "This is a sample text. This text contains some sample words. Sample words are repeated to test the program."

    # Call the function to find the most common elements and their counts
    common_elements = elements(text)


    print("elements and their counts:")
    for element, count in common_elements:
        print(f"{element}: {count}")

