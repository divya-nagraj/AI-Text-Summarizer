def summarize_text(text, sentence_count=2):
    sentences = text.split(".")
    
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    summary = ". ".join(sentences[:sentence_count])
    
    return summary + "."


def show_statistics(text):
    words = text.split()
    characters = len(text)

    print("\nText Statistics")
    print("----------------")
    print("Number of words:", len(words))
    print("Number of characters:", characters)


print("===================================")
print("      AI TEXT SUMMARIZER")
print("===================================")

text = input("\nEnter a paragraph:\n")

if text.strip():
    show_statistics(text)

    summary = summarize_text(text)

    print("\nSummary")
    print("----------------")
    print(summary)

else:
    print("Please enter some text.")
