def summarize_text(text):
    sentences = text.split(".")

    summary = ". ".join(sentences[:2]).strip()

    return summary + "."


print("AI-Powered Text Summarizer")
print("---------------------------")

text = input("Enter a paragraph: ")

summary = summarize_text(text)

print("\nSummary:")
print(summary)v
