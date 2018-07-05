# Checkers Direction Identifier

Checkers Direction Identifier is a RESTful API service using python micro web framework Flask which can be deployed on multiple CentOS 7 Virtual Machines.

The RESTful API accepts a **POST** request with a **JSON** body which is an array of arrays representing a 8x8 grid. Each square on the 8x8 grid has either a red checker, black checker, or no checker on it.

```
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

```

The service returns a **JSON** array of objects with the locations on the grid where there are 4 checkers of the same color (red or black) in a consecutive line, horizontally, vertically, or diagonally. It should return the location in zero-indexed X and Y coordinates, cardinal direction, and color.

```
[
  {"x": 1, "y": 0, "color": "R", "direction": "S"},
  {"x": 2, "y": 1, "color": "B", "direction": "E"},
  {"x": 2, "y": 5, "color": "B", "direction": "E"},
  {"x": 1, "y": 4, "color": "B", "direction": "SE"}
]

```

Each time a POST request is made, a new task is created.

* **End-points**:
    * **"/"**:
        Takes a GET request and returns a message "Hello :D Welcome to the Checkers Direction Identifier!!".
    * **"/results"**:
        Takes a POST request with json data and returns the identified checkers directions json data.
        A GET request to this end-point would return an empty json list.



## Getting Started

Clone the git repository from https://github.com/jayabhavana342/Checkers-RESTAPI.git

```
$ git clone https://github.com/jayabhavana342/Checkers-RESTAPI.git
$ cd production
$ cd vagrant

```

### Prerequisites

Before running the application these software's needs to be installed:

```
Git:
    sudo apt-get install git
VirtualBox:
    sudo apt-get install virtualbox
Vagrant:
    sudo apt-get install vagrant
Docker:
    sudo apt-get install docker.io
Python:
    sudo apt-get install python3.6
Virtualenv:
    sudo apt-get install virtualenv
Pip:
    sudo apt-get install python-pip

```

### Installing

#### Running on local computer (inside production folder)

Create a virtual environment and install the requirements in it:
```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r vagrant/requirements.txt

```
![image](https://user-images.githubusercontent.com/26471348/42347072-50895b82-806a-11e8-8080-d573ba9cd434.png)

Run the app:
```
$ cd app
$ python app.py

```
The application will start running on http://127.0.0.1:5000/


Run the below command to check the output:
```
$ curl -X POST -H "Content-Type:application/json" -d '[["R","R","B","-","B","B","B","-"],["B","R","B","B","B","B","-","-"],["B","R","B","B","R","R","-","B"],["R","R","R","-","-","R","R","R"],["B","B","B","R","-","-","-","B"],["-","R","B","B","B","B","-","B"],["R","B","-","B","R","B","-","R"],["B","R","-","R","B","-","-","-"]]' http://localhost:5000/results

```

#### Running on Virtual Machines (inside vagrant folder)

Open virtualbox from terminal:
```
$ virtualbox

```

To install application on Centos 7 Virtual Machines:
```
$ vagrant up --provision

```

The vagrant installs three CentOS 7 and software's from requirements.txt USING **Ansible** and **Docker**.
Once the virtual machines are initialized, Login to the ssh to access Virtual Machines one at a time:

```
$ vagrant ssh "centos1"
[vagrant@centos1 ~]$ cd app
[vagrant@centos1 ~]$ python3.6 app.py

```

```
$ vagrant ssh "centos2"
[vagrant@centos1 ~]$ cd app
[vagrant@centos1 ~]$ python3.6 app.py

```

```
$ vagrant ssh centos3"
[vagrant@centos1 ~]$ cd app
[vagrant@centos1 ~]$ python3.6 app.py

```

The app is deployed on three different virtual machines on http://0.0.0.0:5000.
The applications ports are forwarded to local ports as below:

| VM           | Guest Port    | Host Port   |
| ------------ |:-------------:| -----------:|
| centos1      | 5000          | 5000        |
| centos2      | 5000          | 5003        |
| centos3      | 5000          | 5003        |

Run the below comands to have a post request to the REST API endpoint "/results" on these virtual machines:

CentOS1 (http://0.0.0.0:5000):
```
curl -X POST -H "Content-type: application/json" -d '[["R","R","B","-","B","B","B","-"],["B","R","B","B","B","B","-","-"],["B","R","B","B","R","R","-","B"],["R","R","R","-","-","R","R","R"],["B","B","B","R","-","-","-","B"],["-","R","B","B","B","B","-","B"],["R","B","-","B","R","B","-","R"],["B","R","-","R","B","-","-","-"]] http://0.0.0.0:5000/results

```
CentOS2 (http://0.0.0.0:5002):
```
curl -X POST -H "Content-type: application/json" -d '[["R","R","B","-","B","B","B","-"],["B","R","B","B","B","B","-","-"],["B","R","B","B","R","R","-","B"],["R","R","R","-","-","R","R","R"],["B","B","B","R","-","-","-","B"],["-","R","B","B","B","B","-","B"],["R","B","-","B","R","B","-","R"],["B","R","-","R","B","-","-","-"]] http://0.0.0.0:5002/results

```
CentOS3 (http://0.0.0.0:5003):
```
curl -X POST -H "Content-type: application/json" -d '[["R","R","B","-","B","B","B","-"],["B","R","B","B","B","B","-","-"],["B","R","B","B","R","R","-","B"],["R","R","R","-","-","R","R","R"],["B","B","B","R","-","-","-","B"],["-","R","B","B","B","B","-","B"],["R","B","-","B","R","B","-","R"],["B","R","-","R","B","-","-","-"]] http://0.0.0.0:5003/results

```