class Informativo:
    mensagem = 'Primeira Aula'
    
    @classmethod
    def printar_informativo(cls):
        print(f'Informativo: {cls.mensagem}')
    
#main
obj1 = Informativo()
obj2 = Informativo()

obj1.printar_informativo()
obj2.printar_informativo()

Informativo.mensagem = 'Segunda aula'
obj1.printar_informativo()
obj2.printar_informativo()