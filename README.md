Create a RESTful API service using the language and frameworks of your choice to be deployed on a CentOS 7 VM. It should accept a POST request with an JSON body that is an array of arrays representing a 8x8 grid. Each square on the 8x8 grid has either a red checker, a black checker, or no checker on it. (These are not placed according to the rules of checkers, but can be placed on any of the 64 squares.)
[
  ["R","R","B","-","B","B","B","-"],
  ["B","R","B","B","B","B","-","-"],
  ["B","R","B","B","R","R","-","B"],
  ["R","R","R","-","-","R","R","R"],
  ["B","B","B","R","-","-","-","B"],
  ["-","R","B","B","B","B","-","B"],
  ["R","B","-","B","R","B","-","R"],
  ["B","R","-","R","B","-","-","-"]
]
The service should return a JSON array of objects with the locations on the grid where there are 4 checkers of the same color (red or black) in a consecutive line, horizontally, vertically, or diagonally. It should return the location in zero-indexed X and Y coordinates, cardinal direction, and color.
[
  {"x": 1, "y": 0, "color": "R", "direction": "S"},
  {"x": 2, "y": 1, "color": "B", "direction": "E"},
  {"x": 2, "y": 5, "color": "B", "direction": "E"},
  {"x": 1, "y": 4, "color": "B", "direction": "SE"}
]
Provide a method that can be used to deploy this application on three CentOS 7 virtual machines. Use whatever tools you feel are appropriate.
Include a README describing what you have built and how to deploy it.