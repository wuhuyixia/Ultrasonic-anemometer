# 超声波

当超声波频率在`40kHz——500kHz` 区间时，超声波在空气中传播的能量最强，而随着频率增加，
衰减幅度会大幅增加

但考虑到200kHz的超声波具有较短的波长（约1.7毫米在空气中），这使得它能够提供更高的空间分辨率。
这对于精确测量风速和风向非常有利，特别是当需要检测小尺度的气流变化时。

同时，高频率的超声波可以更好地避免环境噪声的干扰，特别是在工业环境中，高频信号更容易从背景噪声中分离出来

## 超声波的选型
本设计采用的是福州大禹电子科技有限公司所生产的`DYA-200-01DC`型号超声波
![](\Picture\DYA-200-01DC.jpg)
tb链接，购买时可以后台私信商家，可以减价
~~~
 http://e.tb.cn/h.gxDR1J2RhR9jVYU?tk=oWdU3n2VKAD 
~~~
后面打算尝试`40kHz`等型号

## 200kHzPWM波的生成

~~~
https://blog.csdn.net/qq_45237293/article/details/111997424
~~~
PWM波计算公式
~~~
PMW的频率=时钟频率/（自动重装值+1）*（预分频值+1）
STM的最大时钟频率为72MHz = 72 000 000 Hz
比如：

    TIM_TimeBaseInitTypeDef TIM_TimeBaseInitStructure;
	TIM_TimeBaseInitStructure.TIM_ClockDivision = TIM_CKD_DIV1;
	TIM_TimeBaseInitStructure.TIM_CounterMode = TIM_CounterMode_Up;
	TIM_TimeBaseInitStructure.TIM_Period = 100 - 1;		//ARR
	TIM_TimeBaseInitStructure.TIM_Prescaler = 720 - 1;		//PSC
	TIM_TimeBaseInitStructure.TIM_RepetitionCounter = 0;
	TIM_TimeBaseInit(TIM2, &TIM_TimeBaseInitStructure);

上式的PWM频率 = 72 000 000/（100-1+1）*（720-1+1）=1000Hz
周期 = 1/f = 1/1000 = 1ms
占空比 = CCR / (ARR + 1)
~~~
我们要生成200khz的PWM
~~~
    TIM_TimeBaseStructure.TIM_Period = 359;  // 自动重装载值ARR
    TIM_TimeBaseStructure.TIM_Prescaler = 0;  // 预分频系数PSC
    TIM_TimeBaseStructure.TIM_ClockDivision = 0;  // 时钟分割
    TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;  // 向上计数模式
    TIM_TimeBaseInit(TIM2, &TIM_TimeBaseStructure);
    
    TIM_OCInitStructure.TIM_Pulse = 180;		//CCR

PWM= 72 000 000/1*360 = 200 000
占空比 = 180/360 = 50%
~~~
你可以任意配置一个端口输出PWM波，我们用示波器可以观察到下图

![](\Picture\200kHzPWM-1.jpg)
![](\Picture\200kHzPWM-2.jpg)

## 10个PWM波的生成
~~~
// 定义脉冲计数器和目标脉冲数
volatile uint16_t pulseCounter = 0;
#define PULSE_COUNT 10

// 中断服务例程 (ISR) 用于更新脉冲计数器
void TIM1_UP_IRQHandler(void)
{
    if (TIM_GetITStatus(TIM1, TIM_IT_Update) != RESET)
    {
        // 清除中断标志
        TIM_ClearITPendingBit(TIM1, TIM_IT_Update);

        // 更新脉冲计数器
        pulseCounter++;

        // 如果达到了目标脉冲数，则停止定时器
        if (pulseCounter >= PULSE_COUNT)
        {
         
        }
    }
}
~~~

## PWM设置



## tip(bilibili)
示波器的矫正
~~~
BV1AT411e7i9
~~~
示波器使用操作入门到精通
~~~
BV15Z42147SP
~~~

