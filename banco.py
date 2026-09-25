class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self._cuentas = {}

    def agregar_cuenta(self, cuenta):
        if cuenta.numero in self._cuentas:
            raise ValueError(f"Ya existe una cuenta con el número {cuenta.numero}")
        self._cuentas[cuenta.numero] = cuenta

    def buscar_cuenta(self, numero):
        return self._cuentas.get(numero)

    def transferir(self, numero_origen, numero_destino, monto):
        origen = self.buscar_cuenta(numero_origen)
        destino = self.buscar_cuenta(numero_destino)
        if origen is None or destino is None:
            raise ValueError("La cuenta de origen o de destino no existe")
        origen.extraer(monto)
        destino.depositar(monto)

    def total_depositado(self):
        return sum(cuenta.saldo for cuenta in self._cuentas.values())

    def listar_cuentas(self):
        for cuenta in self._cuentas.values():
            print(cuenta)
