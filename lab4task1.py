from pyvis.network import Network

from laboratoryMazeData import *
from laboratoryMazeData import makeMaze
from src.maze2026GraphClass import mazeGraph
from laboratoryClasses import *

n = 7

maze = makeMaze(n)
print(maze)

mazeAllActs = defineMazeActions(maze)
# mazeAllActs

mazeAvailActs = defineMazeAvailableActions(maze)
for i in mazeAvailActs:
    print(i, mazeAvailActs[i])

print("#" * 20)

mazeTransformationModel = makeMazeTransformationModel(mazeAvailActs)
for i in mazeTransformationModel:
    print(i, mazeTransformationModel[i])

print("#" * 20 + "\nmazeWorldGraph nodes")

mazeWorldGraph = mazeGraph(mazeTransformationModel, mazeStatesLocations(list(mazeTransformationModel.keys())))
for i in mazeWorldGraph.nodes():
    print(i)

net_maze = Network(heading="Lab4. Laboratory maze",
                   bgcolor="#242020",
                   font_color="white",
                   height="750px",
                   width="100%"
                   )

nodeColorsList = []
for node in mazeWorldGraph.origin.keys():
    if maze[node[0], node[1]] == 1:
        nodeColorsList.append("black")
    elif maze[node[0], node[1]] == 2:
        nodeColorsList.append("blue")
    elif maze[node[0], node[1]] == 3:
        nodeColorsList.append("green")
    elif maze[node[0], node[1]] == 4:
        nodeColorsList.append("red")
    else:
        nodeColorsList.append("white")

nodes = ["-".join(str(item) for item in el) for el in mazeWorldGraph.origin.keys()]

x_coords = []
y_coords = []
for node in mazeWorldGraph.origin.keys():
    x, y = mazeWorldGraph.getLocation(node)
    x_coords.append(x)
    y_coords.append(y)

sizes = [10] * len(nodes)

net_maze.add_nodes(nodes, color=nodeColorsList, x=x_coords, y=y_coords, size=sizes, title=nodes)
for node in net_maze.nodes:
    node['label'] = ''

edge_weights = {(intTupleTostr(k), intTupleTostr(v2)): k2 for k, v in mazeWorldGraph.origin.items() for k2, v2 in
                v.items()}

edges = []

for node_source in mazeWorldGraph.nodes():
    for node_target, action in mazeWorldGraph.get(node_source).items():
        if (intTupleTostr(node_source), intTupleTostr(node_target)) not in edges and (intTupleTostr(node_target),
                                                                                      intTupleTostr(node_source)):
            net_maze.add_edge(intTupleTostr(node_source), intTupleTostr(node_target),
                              label=edge_weights[(intTupleTostr(node_source), intTupleTostr(node_target))])
            edges.append((intTupleTostr(node_source), intTupleTostr(node_target)))

net_maze.toggle_physics(False)
net_maze.show("graph1.html", notebook=False)

print("#" * 20 + "\nLab environment status")

labMazeEnv = LaboratoryEnvironment(mazeWorldGraph)
print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in labMazeEnv.status.graph_dict.items()) + "}")
