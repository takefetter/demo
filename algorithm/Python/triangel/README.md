#algorithm triangle.py 
## 题目内容：

每行输入三角型的三条边，判断三角形的形状。假设输入的三边边长均>0。
## 输入格式:

三角型的3条边的长度（int型）。

## 输出格式：

等边三角形：equilateral\n
直角三角形:	Right-angled\n
等腰三角形：isoceles\n
不构成三角形：Unable\n
一般三角形：General\n

## 遇到的问题与解决方案
输入的数字实际上为str,需要使用int()对元素逐个转化,否则会遇到只有输入三条边相同时才符合预期输出equilateral\n
其他情况均为Unable.