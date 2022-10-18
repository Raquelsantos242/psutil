import subprocess

#cria um processo e espera que ele termine sua execução
#antes de retornar ao programa que o criou.

print(subprocess.run("notepad"))

#passando parâmetros
subprocess.run(['notepad', 'C:/Users/Raquel.santos/arq1.txt'])

#cria um processo e retorna imediatamente ao programa que o criou
p = subprocess.Popen('calc')
print('PID do processo criado:', p.pid)

#passando parâmetros
subprocess.Popen(['notepad', 'C:/Users/Raquel.santos/arq1.txt'])
print('PID do processo criado:', p.pid)

