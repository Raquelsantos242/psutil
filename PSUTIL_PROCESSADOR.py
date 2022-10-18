import time
import psutil


print(psutil.cpu_times())
print()
print(psutil.cpu_times(percpu=True))#obter tempo por núcleo
print()
print(psutil.cpu_percent())
print()
for i in range(10):
    time.sleep(0.1)
    print(psutil.cpu_times_percent)
    
print()
print(psutil.cpu_percent(interval=1))#percentual de uso geral da CPU
print(psutil.cpu_percent(interval=1, percpu=True))# percentual de uso por núcleo de CPU
print()


print(psutil.cpu_count())#número de núcleos lógicos
print(psutil.cpu_count(logical=False))#número de núcleos reais
print(psutil.cpu_freq())#frequência em MHrz