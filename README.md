# 10/20 algorithm study

* 10/20 - 백준알고리즘 1157 문자열-단어공부 
  * https://www.acmicpc.net/problem/1157  

* 새로 배운 것
  * python3 for-else 구문
  * for와 함께 사용되는 else는 for 반복문에서 break가 실행되지 않고 끝까지 실행한 결과를 반환 
```python3
data = [2, 4, 5, 10, 3]
max_num = data[0]
for i in data:
    if i > max_num:
        max_num = i
    break
else:
    return max_num
```



