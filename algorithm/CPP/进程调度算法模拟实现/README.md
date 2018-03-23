常见的进程调度算法有：先来先服务 （FCFS，first come first served） 、
最短作业优先（SJF, Shortest Job First） 、
时间片轮转算法（RR，Round-Robin） 、
多级反馈队列(Multilevel Feedback Queue) 、
最高响应比优先法(HRRN，Highest Response Ratio Next) 
在本C++程序中模拟实现了FCFS，SJF和RR算法，
还有一个简单的优先级算法（仅有优先级的比较，类似于短作业优先算法），
排序部分都使用的冒泡排序（我知道时间复杂度很大）