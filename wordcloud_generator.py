import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_word_cloud(input_text):
    wordcloud = WordCloud(width=800, height=400).generate(input_text)

    return wordcloud

if __name__ == "__main__":
    input_text = input("Enter the text data: ")
    
    if not input_text:
        print("No text data provided.")
    else:
        wordcloud = generate_word_cloud(input_text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
