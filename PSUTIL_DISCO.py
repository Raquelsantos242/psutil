import time
import psutil

print(psutil.disk_partitions())#todos os discos físicos
print()
print(psutil.disk_usage(path='C:'))#info de armazenamento por partição
print()
d = psutil.disk_usage(path='C:')
print(d.total)#tamanho do disco c: em bytes
print(d.total / 1024 ** 3)#tamanho do disco c: em gigabytes
print()
print(d.used)#quantidade usada em bytes
print(d.used / 1024 ** 3)#quantidade usada em gigabytes
print()
print(d.free)#quant livre em bytes
print(d.free / 1024 ** 3)#quant livre em gigabytes
print()
print(psutil.disk_io_counters())#leitura e escrita em disco