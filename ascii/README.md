# Picture to ascii

从[Python playground](https://github.com/electronut/pp) 中的ascii fork而来,可将图片转换为ascii码的形式.  
## 原理:  
       1.使用pillow读取图片并将图像转换为灰度  
	   2.将图像分为M(行)*N(列)个小块
	   3.修正M以匹配图像和字体的横纵比
	   4.计算每个小块图像的平均亮度,然后为每个小块查找合适的ASCII字符
	   5.汇集各行ASCII字符串,将它们打印到文件,形成最终图像