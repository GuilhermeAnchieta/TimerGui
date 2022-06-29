import pyautogui as py
from time import sleep


time = 0
while True:
    ask = py.confirm(text='→ O que você deseja fazer?\n\nAtenção: só é possível fazer um novo agendamento\n'
                          'caso o agendamento anterior tenha sido cancelado.',
                     title='   == Menu ==', buttons=['Iniciar novo temporizador', 'Cancelar temporizador', 'Dev'])
    if ask == "Iniciar novo temporizador":
        try:
            time = py.prompt(text='== Digite o tempo restante até o pc ser desligado ==\n\n(Horas : minutos)',
                             title='Comfigurar tempo', default='00 : 00')
            horas = time[0:time.index(':')]
            minutos = time[time.index(':') + 1:]
            horas = int(horas)
            minutos = int(minutos)
            horas *= 3600
            minutos *= 60
            tottime = horas + minutos
            if tottime <= 600:
                py.alert(text='→ O tempo minimo é de mais de 10 minutos , retornando ao menu.', title='ERRO!!!',
                         button='OK')
                continue
            py.hotkey("win", "r")
            sleep(0.3)
            py.write("cmd")
            py.press("enter")
            sleep(0.3)
            py.write(f"shutdown -s -t {tottime}")
            py.press("enter")
            sleep(0.3)
            py.hotkey("altleft", "f4")
            break
        except ValueError:
            if time is None:
                break
            else:
                py.alert(text='O tempo deve ser adicionado no seguinte modelo: "00 : 00" ( Horas : minutos )',
                         title='ERRO!!!', button='OK')
        except AttributeError:
            break
    elif ask == "Cancelar temporizador":
        py.hotkey("win", "r")
        sleep(0.3)
        py.write("cmd")
        py.press("enter")
        sleep(0.3)
        py.write(f"shutdown -a")
        py.press("enter")
        sleep(0.3)
        py.hotkey("altleft", "f4")
        break
    elif ask == 'Dev':
        py.alert(text='Gmail: guilherme.anchietass@gmail.com\n\nGitHub: https://github.com/GuilhermeAnchieta\n\n'
                      'linkedin: https://www.linkedin.com/in/guilherme-anchieta-silva-siqueira-de-almeida-b2192a232/',
                 title='Desenvolvedor', button='OK')
    else:
        break
