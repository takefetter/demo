
常见的内存分配算法有首次适应算法（First Fit，FF）、循环首次适应算法（Next Fit，NF）、
最佳适应算法（Best Fit，BF）、最差适应算法（Worst Fit，WF），本实验中实现了这4种算法，
使用C++语言实现。使用SIZE[MAX]代表内存，list s和n分别存储已分配的内存空间和未分配的空间。