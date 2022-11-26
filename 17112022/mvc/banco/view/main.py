from model.pessoaFisica import PessoaFisica
from model.pessoaJurifica import PessoaJuridica
from controller.juridico import create_pj, read_pj
from controller.fisico import create_psf, read_psf


def menu():

    menu = 1

    while (menu != 0):
        menu_inicial = int(input("Digite a opção\n1 - Pessoa Fisica\n2 - Pessoa Juridica \n 3 - Sair \n:>"))
        
        match menu_inicial:
            case 1:
                menu = int(input("1 - Pessoa Fisica\n2 - Listar Conta \n:>"))

                match menu:
                    case 1:
                       
                        pessoaFisica = PessoaFisica()
                        pessoaFisica.titular = "BANCO"
                        pessoaFisica.cpf = "000000000"
                        pessoaFisica.saldo_inicial = 90000
                        
                        opcaoStitular = int(input("Cadastrar Segundo Titular: \n 1 - Sim \n 2 - Não \n 3 - Sair \n:>"))
                        
                        if opcaoStitular == 1:  
                            
                            pessoaFisica.segundo_titular = input("Digite o segundo titular: ")
                                                
                            create_psf(pessoaFisica)
                        
                        elif opcaoStitular == 2:
                            
                            print("Flw, vlw")
                            break                        
                        
                    case 2: 
                        
                        listarcontas = read_psf()
                        for x in listarcontas:
                            print(x)
                    
                    case 3:
                        
                        break
                    
                    case _:
                        print("Opção Inválida. Tente novamente.") 
                        
            case 2:
                
                menu = int(input("1 - Pessoa Juridica\n2 - Listar Conta \n 3 - Sair"))
                
                match menu:
                    case 1:
                       
                        Pessoajuridica = PessoaJuridica()
                        Pessoajuridica.titular = "Bradesco"
                        Pessoajuridica.cnpj = "1223423423"
                        Pessoajuridica.saldo_inicial = 90234
                        
                        opcaoStitular = int(input("Cadastrar Segundo Titular: \n1 - Sim \n 2 - Não \n 3 - Sair"))
                        opcaoStitular = 1
                        if opcaoStitular == 1:  
                            
                            Pessoajuridica.segundo_titular = input("Digite o segundo titular: ")
                        
                            create_pj(Pessoajuridica)
                        
                        elif opcaoStitular == 2:
                            
                            print("Flw, vlw")
                            break         
                            
                        
                    case 2: 
                        
                        listarcontas = read_pj()
                        for x in listarcontas:
                            print(x)
                            
                    case 3:
                        
                        break
            
            case 3:
                print("Flw, vlw")
                break
            