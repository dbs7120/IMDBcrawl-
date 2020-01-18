import sys
import nltk
import time

count_t = time.time()

input_file_name = sys.argv[1]
output_file_name = "count.txt"

fp = open(input_file_name, 'rt', encoding='UTF8')
op = open(output_file_name, 'wt', encoding='UTF8')

words = nltk.word_tokenize(fp.read())

# 단일문자제거
words = [word for word in words if len(word) > 1]

# 숫자제거
words = [word for word in words if not word.isnumeric()]

# 소문자화
words = [word.lower() for word in words]

# 빈도체크
fdist = nltk.FreqDist(words)

for word, frequency in fdist.most_common(100):
    # print(u'{};{}'.format(word, frequency))
    op.write((u'{}  {}'.format(word, frequency))+'\n')

# time 모듈을 통해 실행시간 측정(초단위)
print('Running Time(second) : %.02f' % (time.time() - count_t))