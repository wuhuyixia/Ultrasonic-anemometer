# PWM放大电路设计

我们由STM32生成的200kHz的PWM波幅值只有3.3V，无法驱动超声波换能器，详情看`超声波`文档

将这个脉冲信号经过超声波的发射电路进行电压放大。
这样升压过后的信号，经由电路传到超声波传感器上就可以驱动换能器发射超声波信号。

## 电路设计

### 仿真设计

![](\Picture\200kHz-drive.png)
![](\Picture\200khz-drive-V.png)
我们可以看到该电路实现了电压的放大

### 实际测量
`2024.10.24`

在实际设计中这部分我采用的是现有的模块利用`3-20V输入转3.3V/5V/12V`,希望可以实现
~~~
TB:http://e.tb.cn/h.gxDveQ6eBur50yr?tk=p7gD3n2Lm65 
http://e.tb.cn/h.gyfXNex1bLgmukG?tk=v24F3MCUEe8
~~~
