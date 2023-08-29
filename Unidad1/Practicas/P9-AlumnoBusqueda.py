class Alumno():
    def __init__(self, nombre, semestre, carrera, rfc, no_control):
        self.nombre = nombre;
        self.semestre = semestre;
        self.carrera = carrera;
        self.rfc = rfc;
        self.no_control = no_control;
        
    def buscarNombre(arreglo, valor):
        for i in arreglo:
            if i.nombre == valor:
                i.mostrar_datos();
    
    def buscarSemestre(arreglo, valor):
        for i in arreglo:
            if i.semestre == valor:
                i.mostrar_datos();
    
    def buscarCarrera(arreglo, valor):
        for i in arreglo:
            if i.carrera == valor:
                i.mostrar_datos();

    def buscarRfc(arreglo, valor):
        for i in arreglo:
            if i.rfc == valor:
                i.mostrar_datos();

    def buscarNoControl(arreglo, valor):
        for i in arreglo:
            if i.no_control == valor:
                i.mostrar_datos();

    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}");
        print(f"Semestre: {self.semestre}");
        print(f"Carrera: {self.carrera}");
        print(f"RFC: {self.rfc}");
        print(f"No. Control: {self.no_control}");

def main():
    
    arreglini = [];
    persona1 = Alumno("Ebeth", 3, "Tic's", "MECE0102165F5", 22590434);
    persona2 = Alumno("Ebeth", 4, "Sistemas", "MECE01000165f5", 22592922)
    arreglini.append(persona1);
    arreglini.append(persona2);

    #arreglini.append([Alumno("Ebeth", 3, "Tic's", "MECE0102165F5", 22590434)]);
    print("\n###__ MENU __###");
    print("1) Agregar un nuevo alumno")
    print("2) Buscar por nombre")
    print("3) Buscar por semestre")
    print("4) Buscar por carrera");
    print("5) Buscar por rfc");
    print("6) Buscar por No. Control");
    opcion = int (input("--> "));
    
    if opcion == 1:
        pass
    elif opcion ==2:
        nombre = str (input("\nIngresa el Nombre: "));
        Alumno.buscarNombre(arreglini, nombre);
    elif opcion == 3:
        semestre = int (input("\nIngresa el Semestre: "));
        Alumno.buscarSemestre(arreglini, semestre);
    elif opcion == 4:
        carrera = str (input("\nIngresa la Carrera: "));
        Alumno.buscarCarrera(arreglini, carrera);
    elif opcion == 5:
        rfc = str (input("\nIngresa el RFC: "));
        Alumno.buscarRfc(arreglini, rfc);
    elif opcion == 6:
        no_control = int (input("\nIngresa el No. Control: "))
        Alumno.buscarNoControl(arreglini, no_control);
    else:
        print("\n¡Error!, opcion no reconocida")
        
        while (opcion < 1 or opcion > 5):
            print("Ingresa otra opcion: ");
            opcion = int (input("--> "));
    
if __name__ == "__main__":
    main();