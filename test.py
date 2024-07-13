from flask import Flask, json

api = Flask(__name__)


@api.route("/<type>/<nr>", methods=["GET"])
def setSwitch(type, nr):
    print(type)
    print(nr)
    retData = ["OK"]
    return json.dumps(retData)


if __name__ == "__main__":
    api.run()
