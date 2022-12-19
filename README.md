# Biblioteca_AlgoritmicaII
Grupo 1

Integrantes:
- Santa Cruz Pachas Edward Grover
- Ortiz Quispe Akcel Eduardo
- Triveño Ruffner Daniel Huber

Ejecución:
    El programa inicializa las funciones desde el archivo Principal.py

Login: Sistema de cuentas que daría inicio al programa
    Clase_Admin: Sistema para añadir, borrar y mostrar los libros que albergará la biblioteca
    Clase_Clientes: Sistema para añadir borrar y mostrar los usuarios que accederán a los libros de nuestra biblioteca
    Credenciales: 
        Para admin:
            usuario: admin 
            contraseña: 123
        Para Clientes:
            usuario: user 
            contraseña: 123

Recursos Usados:
    - Python 3.10.7
    - DB Browser

Librerías usadas:
    - SQLite3
        Instalar Window: Escribir en terminal "pip Install pysqlite3"
        Instalar Linux: Escribir en terminal: "sudo apt install sqlite3"
    - ABC
    - werkzeug
        Instalar Windows: pip install werkzeug
        Instalar Ubuntu: "sudo apt-get install python-werkzeug" 

Nuevas funcionalidades:
    Pedido:
        Esta nueva clase sirve y llama a métodos para la busqueda de determinados libros y verificar la disponibilidad, además del pedido y reserva de estos, pero, antes, se verifica que el cliente, mediante la búsqueda de su DNI, esté en nuestra base de datos.
        Funciones:
        Buscar:
            Búsqueda de libros en la base de datos mediante el ingreso del nombre o parte de este.
        Pedir:
            Pedido de libros, pero antes, se verifica la disponibilidad, si es que no está disponible se recomienda reservar el libro.
        Reservar:
            Se reserva libros que SOLO no estén disponibles en el stock, es decir, su valor sea igual a 0.

        
