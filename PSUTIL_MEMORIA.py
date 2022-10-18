import time
import psutil

print('\n')
print(psutil.virtual_memory())#retorna calores estatísticos sobre o uso de memória principal
m = psutil.virtual_memory()
print(m.total)#memoria total em bytes
print(m.total / 1024** 3)#memoria disponivel em gigabytes
print(m.percent)#percentual de uso de memoria

print(psutil.swap_memory())