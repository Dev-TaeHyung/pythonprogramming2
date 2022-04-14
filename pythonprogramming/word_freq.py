#  word frequency
# - 2개의 파라미터 : 영문txt파일명, 정수
# - txt파일을 읽어옴 (open() )함수
# - 한줄씩 읽어오기 : readline()
# - string을 word 단위로 분리
# - word의 count로 dictionary생성
# - 두번째 파라미터 숫자의 상위count의 word를 화면에 보여줌
# - 화면에 count수의 내림차순으로 보여주고 종료
# - 보여주는 화면에서 word는 left 정렬 / count는 right 정렬

import sys
print(sys.argv[1])
fileName = sys.argv[1]
num = sys.argv[2]

f = open("memo.txt",'r')
content = f.readlines()  # 한줄씩 입력
wordCount = {}
for i in content:
     words = i.split()
     for word in words:
         wordCount[word] = wordCount.get(word,0)+1

word_list = sorted(wordCount.items(), key = lambda x:x[1], reverse = True)

cnt=0
for i in word_list:
    if(cnt > n):
        break
        cnt += 1
    print(f"{i[0].ljust(10)+ str(i[1]).rjust(10)}")
