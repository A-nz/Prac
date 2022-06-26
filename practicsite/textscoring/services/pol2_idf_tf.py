from collections import Counter
import math
import pymorphy2
import re

morph = pymorphy2.MorphAnalyzer()
morph1 = pymorphy2.MorphAnalyzer()

norm_line_list = None
norm_line1_list = None


def text_line(line: str):
    line_split = (re.findall(r'\w+', line))

    # global norm_line_list
    # return line_split
    return line_split


def norm(word: str):
    p = morph.parse(word)[0]
    return p.normal_form


def line_norm(splited_line: list[str]):
    norm_line_list = []
    for i in range(len(splited_line)):
        norm_line_list.append(norm(splited_line[i]))
    # print(norm_line_list)
    return norm_line_list

    # line_norm()


def tf_count(text: list):
    line_norm(text)
    tf_text = Counter(text).most_common(3)
    return tf_text


def compute_tfidf(corpus: list[list:str]):
    def compute_tf(text):
        tf_text = Counter(text)
        for i in tf_text:
            tf_text[i] = tf_text[i] / float(len(text))
        return tf_text

    def compute_idf(word, corpus):
        return math.log10(len(corpus) / sum([1.0 for i in corpus if word in i]))

    documents_list = []
    for text in corpus:
        tf_idf_dictionary = {}
        computed_tf = compute_tf(text)
        for word in computed_tf:
            tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)
        documents_list.append(tf_idf_dictionary)
    return documents_list


# corpus = norm_both_lists
#
# print(compute_tfidf(corpus))


#if __name__ == "__main__":
#    line1 = 'Когда Вася вышел на лужайку, он увидел много кроликов. Один из кроликов так напугал Васю, что тот потерял дар речи! После этого Вася не выходил на лужайку. На лужайках зайцы больше не боялись Вась.'
#    line2 = "В начале было слово! Пусть вас не пугает Вася, он не кролик. Кролики правят этим миром, как и этой лужайкой. На то воля Васи."
#
#     text1 = line_norm(text_line(line1))
#     text2 = line_norm(text_line(line2))
#
#     print(tf_count(text1))
#     print(tf_count(text2))
#
#     norm_both_lists = [text1, text2]
#     print(compute_tfidf(norm_both_lists))