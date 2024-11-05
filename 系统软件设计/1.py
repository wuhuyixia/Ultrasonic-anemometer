import numpy as np
import matplotlib.pyplot as plt

# 定义频率和周期
frequency = 200e3 # Hz
period = 1/frequency # seconds

# 创建时间轴
t = np.arange(0, 10*period, period/1000) # 10个周期，采样率为原频率的1000倍

# 设定占空比
duty_cycle = 0.5 # 50%

# 计算PWM波形
pwm_signal = np.where(t % period <= duty_cycle*period, 1, 0)

# 绘制波形
plt.figure(figsize=(10, 4))
plt.plot(t, pwm_signal)
plt.title('200kHz PWM Waveform')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()