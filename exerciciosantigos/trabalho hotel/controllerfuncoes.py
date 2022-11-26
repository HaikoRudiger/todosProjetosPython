
def salvar(hotel_cliente):
    with open('cadastro.txt', 'a') as arquivo:
        arquivo.write(str(hotel_cliente)+"\n")

def relatorio():
    with open('cadastro.txt', 'r') as arquivo:
        print(arquivo.read())


def procurarHospedes(clienteFind): 
    arquivo = open("cadastro.txt", "r") 
    for line in arquivo:      
        if clienteFind == eval(line)['nome']:     
            print("Encontrado")
    if clienteFind != eval(line)['nome']:
        print("Cliente não encontrado")




def fazerCheckout(chekout):
    index=0
    flag=0
    arquivo = open("cadastro.txt", "r") 
    for line in arquivo:
        index +=1
        if chekout == eval(line)['nome']:
            chave = index
            flag =1
    arquivo.close()
    if flag == 0:
        print("Cliente não encontrado")

    else:
        try:
            with open('cadastro.txt', 'r') as fr:
                # reading line by line
                lines = fr.readlines()


                # pointer for position
                ptr = 1

                # opening in writing mode
                with open('cadastro.txt', 'w') as fw:
                    for line in lines:

                        # we want to remove 5th line
                        if ptr != chave:
                            fw.write(line)
                        ptr += 1
            print("Deleted")

        except:
            print("Oops! someting error")