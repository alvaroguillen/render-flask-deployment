from controllers import personas_controller

def registrar_rutas(app):
    #Esta ruta se encarga de mostrar los datos
    app.add_url_rule("/", view_func = personas_controller.obtener_personas, methods = ["GET"])
    #Esta ruta se encarga de hacer un registro
    app.add_url_rule("/crear-registro", view_func = personas_controller.crear_registro, methods = ["POST"])
    #Esta ruta se encarga de eliminar un registro
    app.add_url_rule("/eliminar-registro/<int:id>", view_func = personas_controller.eliminar_registro, methods = ["POST"])
