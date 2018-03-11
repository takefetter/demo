# Photo_mosaic
  从[Python playground](https://github.com/electronut/pp) 中的photomosaic fork而来,可将图片改为马赛克的形式(模糊处理).
## 原理:  
       1.读取一些小块图像(getImages()函数),他们将取代原始图像中的小块
	   2.使用pillow读取图片,将图像分为M(行)*N(列)个小块(将图片分割成网格,splitImage()函数)
	   3.计算输入图像的平均颜色值(getAverageRGB()函数),
	   4.对于每个小块,从输入的小块图像中找到最佳匹配(getBestMatchIndex()函数)
	   5.将选择的输入图像安排在M*N的网格中(创建图像网格使用createImageGrid()函数)
	   6.创建最终的照片马赛克(createPhotomosaic函数)
	   7.控制照片马赛克的大小(因为如果基于目标图像中匹配的小块,盲目地将图片输入粘贴在一起,就会得到一个巨大的照片马赛克,比目标图像大得多
		     为了避免这种情况,调整输入图像的大小,以匹配网格中每个小块的大小.(使用img.thumbnail()方法调整图像)
## 使用方法(示例):
	python ./photo_mosaic/photo_mosaic.py --target-image ./photo_mosaic/image/59559639_p0.png --input-folder ./photo_mosaic/image --grid-size 4 4 --output-file ./photo_mosaic/output/59559639.png

输出效果如output中的图片.
