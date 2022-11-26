import datetime
import time


def horariasaudacao():
    data_hoje = datetime.date.today()
    seconds = 1666303373.8327155
    horario_local = time.ctime(seconds)
    return print("O horiario atual é {} , o dia de hoje é {}".format(horario_local ,data_hoje ))

horariasaudacao()



            
                
                 






