from math import sqrt

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello :D Welcome to the Checkers Direction Identifier!!'


# recursive function to check if there are 4 same checkers in south direction
def checkSouth(x, y, original, data, counter):
    if counter == 0:
        return True
    if x == -1:
        return False
    else:
        try:
            return checkSouth(x + 1, y, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


# recursive function to check if there are 4 same checkers in north direction
def checkNorth(x, y, original, data, counter):
    if counter == 0:
        return True
    if x == -1:
        return False
    else:
        try:
            return checkNorth(x - 1, y, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


# recursive function to check if there are 4 same checkers in west direction
def checkWest(x, y, original, data, counter):
    if counter == 0:
        return True
    if y == -1:
        return False
    else:
        try:
            return checkWest(x, y - 1, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


# recursive function to check if there are 4 same checkers in east direction
def checkEast(x, y, original, data, counter):
    if counter == 0:
        return True
    if y == -1:
        return False
    else:
        try:
            return checkEast(x, y + 1, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


# recursive function to check if there are 4 same checkers in south-east direction
def checkSouthEast(x, y, original, data, counter):
    if counter == 0:
        return True
    elif x == -1 or y == -1:
        return False
    else:
        try:
            return checkSouthEast(x + 1, y + 1, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


# recursive function to check if there are 4 same checkers in south-west direction
def checkSouthWest(x, y, original, data, counter):
    if counter == 0:
        return True
    elif x == -1 or y == -1:
        return False
    else:
        try:
            return checkSouthWest(x + 1, y - 1, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


# recursive function to check if there are 4 same checkers in north-west direction
def checkNorthWest(x, y, original, data, counter):
    if counter == 0:
        return True
    elif x == -1 or y == -1:
        return False
    else:
        try:
            return checkNorthWest(x - 1, y - 1, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


# recursive function to check if there are 4 same checkers in north-east direction
def checkNorthEast(x, y, original, data, counter):
    if counter == 0:
        return True
    elif x == -1 or y == -1:
        return False
    else:
        try:
            return checkNorthEast(x - 1, y + 1, original, data, counter - 1) and data[x][y] == original
        except IndexError:
            return False


# recursive funtion to find the lenght of the json data in order to check if it is of 8x8 matrix
def length(test_data):
    if type(test_data) == list:
        return sum(length(item) for item in test_data)
    else:
        return 1


# function which appends the x,y,color,direction key values to the result json data
@app.route('/results', methods=['POST', 'GET'])
def result():
    res = []
    test_data = request.get_json()
    if sqrt(length(test_data)) == 8:
        for i, col in enumerate(test_data):
            for j, row in enumerate(col):
                if test_data[i][j] != '-':
                    if checkSouth(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "S"})
                    if checkNorth(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "N"})
                    if checkWest(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "W"})
                    if checkEast(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "E"})
                    if checkSouthEast(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "SE"})
                    if checkNorthEast(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "NE"})
                    if checkSouthWest(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "SW"})
                    if checkNorthWest(i, j, row, test_data, 4):
                        res.append({"x": i, "y": j, "color": row, "direction": "NW"})
    return jsonify(result=res)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
