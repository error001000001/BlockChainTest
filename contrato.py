class contrato:
    owner_dir = ""
    obj_dir = []
    monto = []

    def __init__(self, dir, obj):
        self.owner_dir = dir
        self.obj_dir.append(obj)

    def comprar(self, price):
        self.monto.append(price)
        
    def addObjeto(self, obj):
        self.obj_dir.append(obj)

    def mostrar(self):
        print('direccion usr: ',self.owner_dir)
        print('direccion obj: ',self.obj_dir)

objeto = contrato('0x0f95930x95938f93920', {'0x949':39})
objeto.addObjeto({'0xf5929': 44})
objeto.mostrar()
