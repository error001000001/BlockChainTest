import hashlib

class BlockChain:
    #print("//////////// BlockChain ///////////////")
    def __init__(self):
        self.chain = []
        self.generar_bloque_genesis()
    def generar_bloque_genesis(self):
        #print("GENESIS: ")
        self.chain.append(Moneda("0", ['Genesis Block']))
    def crear_bloque_de_transaccion(self, trans_list):
        #print("NUEVO: ")
        bloque_hash_anterior = self.ultimo_bloque.bloque_hash
        self.chain.append(Moneda(bloque_hash_anterior, trans_list))
        #print("//////////// crear_bloque_de_transaccion ///////////////")
    def mostrar_cadena(self):
        for i in range(len(self.chain)):
            print(f"Datos {i + 1}:\n  {self.chain[i].bloque_datos}")
            print(f"Hash {i + 1}:\n  Nuevo: {self.chain[i].bloque_hash}")
            print("\n------------------------\n")

    @property
    def ultimo_bloque(self):
        return self.chain[-1]

class Moneda:
    def __init__(self, ant_hash, trans_list):
        self.ant_hash = ant_hash
        self.trans_list = trans_list
        self.bloque_datos = f"Data: {' - '.join(trans_list)} \n  Anterior: {ant_hash}"
        self.bloque_hash = hashlib.sha256(self.bloque_datos.encode()).hexdigest()
        #print("//////////// Moneda ///////////////")

t1 = "t1 to t2"
t2 = "t2 to t1"
t3 = "t3 to t4"
t4 = "t4 to t5"
t5 = "t5 to t6"
t6 = "t6 to t3"

miblockchain = BlockChain()

miblockchain.crear_bloque_de_transaccion([t1, t2])
miblockchain.crear_bloque_de_transaccion([t5])
miblockchain.crear_bloque_de_transaccion([t5])
miblockchain.crear_bloque_de_transaccion([t5])
miblockchain.mostrar_cadena()