import requests
import cloudpickle
import base64


def run(server_ip):
    def decorator(func):
        def wrapper(*args, **kwargs):

            func_serialized = base64.b64encode(cloudpickle.dumps(func)).decode("utf-8")

            args_serialized = [
                base64.b64encode(cloudpickle.dumps(arg)).decode("utf-8") for arg in args
            ]
            data = {"function": func_serialized, "args": args_serialized}

            response = requests.post(f"http://{server_ip}:5779/execute", json=data)

            if response.status_code == 200:
                result = response.json().get("result")
                return result
            else:
                error = response.json().get("error", "Unknown error")
                raise Exception(f"Server error: {error}")

        return wrapper

    return decorator
