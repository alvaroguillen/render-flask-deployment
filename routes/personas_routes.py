from controllers import personas_controller

def registrar_rutas(app):
    #Mostrar datos
    app.add_url_rule("/", view_func = personas_controller.obtener_personas, methods = ["GET"], endpoint = "inicio")
    #Crear registro
    app.add_url_rule("/crear-registro", view_func = personas_controller.crear_registro, methods = ["POST"])
    #Eliminar registro
    app.add_url_rule("/eliminar-registro/<int:id>", view_func = personas_controller.eliminar_registro, methods = ["POST"])
    #Consultar registro
    app.add_url_rule("/consultar", view_func = personas_controller.consultar_registro, methods = ["GET"], endpoint = 'consultar_registro')
    #Consultar lista de registros
    app.add_url_rule("/lista-registros", view_func = personas_controller.mostrar_lista_registros, methods = ["GET"], endpoint = 'ver_registro')
    #Buscar contacto
    app.add_url_rule("/busqueda-persona", view_func = personas_controller.buscar_contacto, methods = ["POST"], endpoint = 'buscar_contacto')
    #Mostrar persona
    app.add_url_rule("/persona/<cedula>", view_func = personas_controller.mostrar_persona, methods = ["GET"], endpoint = 'mostrar_persona')
