from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

def read_file() -> list:
    with open('paragraphs.txt') as file:
        paragraphs = file.readlines()
    return paragraphs


def get_stop_words() -> dict:
    stop_words = set(stopwords.words('english'))
    stop_words_dict = {word: 0 for word in stop_words}

    return stop_words_dict


def remove_stop_words(pragraphs: list) -> tuple[list ,dict]:
    updated_paragraphs = []
    remove_stop_words_count = {}
    for paragraph in pragraphs:
        words:list = paragraph.split()
        for i in range(0,len(words)):
            if get_stop_words().get(words[i].lower()) != None:
                remove_stop_words_count[words[i]] = remove_stop_words_count.get(words[i],0) + 1
                words[i] = ''
        sentence = ' '.join(words)
        updated_paragraphs.append(sentence + '\n')
    return (updated_paragraphs, remove_stop_words_count)


def write_file(content):
    with open('paragraphs_without_stop_words.txt', 'w') as file:
        file.writelines(content)


write_file(remove_stop_words(read_file())[0])
print(remove_stop_words(read_file())[1])

# print(get_stop_words())
