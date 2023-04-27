
class Ordenador:
    
    def __init__(self, fabricante, modelo, anio, precio):
        self.fabricante = fabricante
        self.modelo = modelo 
        self. anio = anio
        self. precio = precio
        
    def encender(self):
        self.estado = True
        
    def aplicar_descuento(self, descuento):
        if (descuento > 0 and descuento < 0.9):
            self.precio = self.precio = self.precio * descuento
        
        
        
ordenador1 = Ordenador("Asus", "A55A",2008, 495 )
ordenador1.precio *= 0.9
    
    
      