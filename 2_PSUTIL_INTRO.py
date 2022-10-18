import psutil

#lista dos processos sendo executados na máquina
print(psutil.pids())
print('------------------------------------------------------------------------------------------------------------------------')
print(len(psutil.pids()))
print('------------------------------------------------------------------------------------------------------------------------')

#verifica se processo existe
pid = 472
print(psutil.pid_exists(pid))
print('------------------------------------------------------------------------------------------------------------------------')

#process_iter(): interador sobre os processos da maquina
for p in psutil.process_iter():
    print(p)
print('------------------------------------------------------------------------------------------------------------------------')
    