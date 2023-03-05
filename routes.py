from api import apiGeneral, apiSpecify, apiFinish

def routers(app) -> None:
  @app.route("/")
  def hello():
    return "Hello World!"

  @app.route("/todo", methods=["POST", "GET"])
  def todoGeneral():
    result = apiGeneral()
    return result

  @app.route("/todo/<id>", methods=["GET","PUT", "PATCH", "DELETE"])
  def todoSpecify(id):
    result = apiSpecify(id)
    return result

  @app.route("/todo/<id>/finish", methods=["PATCH"])
  def todoFinish(id):
    result = apiFinish(id)
    return result