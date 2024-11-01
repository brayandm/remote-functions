from flask import Flask, request, jsonify
import cloudpickle
import base64

app = Flask(__name__)


@app.route("/execute", methods=["POST"])
def execute_function():
    data = request.get_json()
    func_serialized = base64.b64decode(data["function"])
    args_serialized = data["args"]

    try:

        func = cloudpickle.loads(func_serialized)

        args = [cloudpickle.loads(base64.b64decode(arg)) for arg in args_serialized]

        result = func(*args)
        print("Result:", result)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5779)
