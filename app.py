from math import sqrt

from flask import Flask, request, jsonify

app = Flask(__name__)


def recursive_len(test_data):
    if type(test_data) == list:
        return sum(recursive_len(subitem) for subitem in test_data)
    else:
        return 1


def checkSouth(x, y, original, data, counter):
    if counter == 0:
        return True
    if x == -1:
        return False
    else:
        try:
            print("bottom:", x, y, data[x][y], original, counter)
            return checkSouth(x + 1, y, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


def checkNorth(x, y, original, data, counter):
    if counter == 0:
        return True
    if x == -1:
        return False
    else:
        try:
            print("top:", x, y, data[x][y], original, counter)
            return checkNorth(x - 1, y, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


def checkWest(x, y, original, data, counter):
    if counter == 0:
        return True
    if y == -1:
        return False
    else:
        try:
            print("left:", x, y, data[x][y], original, counter)
            return checkWest(x, y - 1, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


def checkEast(x, y, original, data, counter):
    if counter == 0:
        return True
    if y == -1:
        return False
    else:
        try:
            print("right:", x, y, data[x][y], original, counter)
            return checkEast(x, y + 1, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


def checkSouthEast(x, y, original, data, counter):
    if counter == 0:
        return True
    elif x == -1 or y == -1:
        return False
    else:
        try:
            print("bottomright:", x, y, data[x][y], original, counter)
            return checkSouthEast(x + 1, y + 1, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


def checkSouthWest(x, y, original, data, counter):
    if counter == 0:
        return True
    elif x == -1 or y == -1:
        return False
    else:
        try:
            print("bottomleft:", x, y, data[x][y], original, counter)
            return checkSouthWest(x + 1, y - 1, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


def checkNorthWest(x, y, original, data, counter):
    if counter == 0:
        return True
    elif x == -1 or y == -1:
        return False
    else:
        try:
            print("topleft:", x, y, data[x][y], original, counter)
            return checkNorthWest(x - 1, y - 1, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


def checkNorthEast(x, y, original, data, counter):
    if counter == 0:
        return True
    elif x == -1 or y == -1:
        return False
    else:
        try:
            print("topright:", x, y, data[x][y], original, counter)
            return checkNorthEast(x - 1, y + 1, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


@app.route('/results', methods=['POST', 'GET'])
def result():
    res = []
    test_data = request.get_json()
    if sqrt(recursive_len(test_data)) == 8:
        for i, col in enumerate(test_data):
            for j, row in enumerate(col):
                if test_data[i][j] != '-':
                    if checkSouth(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "S"})
                        print("True", i, j)
                    if checkNorth(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "N"})
                        print("True", i, j)
                    if checkWest(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "W"})
                        print("True", i, j)
                    if checkEast(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "E"})
                        print("True", i, j)
                    if checkSouthEast(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "SE"})
                        print("True", i, j)
                    if checkNorthEast(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "NE"})
                        print("True", i, j)
                    if checkSouthWest(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "SW"})
                        print("True", i, j)
                    if checkNorthWest(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "NW"})
                        print("True", i, j)
                    print("False", i, j)
                    print("========")

    return jsonify(result=res)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
