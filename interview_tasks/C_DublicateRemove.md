![img_2.png](images_description/img_2.png)
```python
n = int(input())
unique = [None]
for i in range(n):
    curr = int(input())
    if curr != unique[-1]:
        print(curr)
        unique.append(curr)
```