"Day 11: Reactor"
import copy
import numpy as numpy

def parse_inputs(input_string):
    flows = {}
    split_string = input_string.split("\n")

    for i in split_string:
        line = i.split(":")
        line = [i for i in line if i != ""]
        if len(line) > 0:
            source = line[0]
            targets = [i for i in line[1].split(" ") if i != ""]
            flows[source] = targets

    return flows


# depth first search
def find_dfs_paths(flows, starting_node, ending_node, path=[]):
    path = path + [starting_node]

    if starting_node == ending_node:
        return [path]

    if starting_node not in flows:
        return []

    paths = []
    for node in flows[starting_node]:
        if node not in path:
            newpaths = find_dfs_paths(flows, node, ending_node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def countpaths(flows, end):
    # simpler way without storing paths in memory
    counts = dict()
    new_counts = { node: (1 if node == end else 0) for node in flows }

    while new_counts != counts:
        counts = new_counts
        new_counts = {
            node: (1 if node == end else sum(counts[child] for child in flows[node])) for node in counts
        }

    return new_counts


if __name__ == '__main__':
    
    filename = 'day-11-server-rack-test.txt'

    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    flows = parse_inputs(contents)

    starting_node = "you"
    ending_node = "out"
    path = []

    all_dfs_paths = find_dfs_paths(flows, starting_node, ending_node, path)

    print(len(all_dfs_paths))

    expected = 5
    answer = len(all_dfs_paths)

    assert answer == expected, "wrong number of paths"


    filename = 'day-11-server-rack.txt'

    with open(filename, 'r') as f:
        contents = f.read()
    f.close()

    flows = parse_inputs(contents)
    flows["out"] = []
    starting_node = "you"
    ending_node = "out"
    path = []

    all_dfs_paths = find_dfs_paths(flows, starting_node, ending_node, path)

    print(f"Number of paths from {starting_node} to {ending_node}", len(all_dfs_paths))

    answer_again = countpaths(flows, ending_node)
    print("answer without storing all paths in memory", answer_again[starting_node])


    num_paths = 1
    # now we have to go backwards
    nodes_to_visit = ["dac", "fft"]

    paths_to = {}
    ending_nodes = ["out"] + nodes_to_visit

    for ending_node in ending_nodes:
        paths_to[ending_node] = countpaths(flows, ending_node)

    # meta paths
    # svr -> fft -> dac -> out
    # svr -> dac -> fft -> out
    print("svr -> fft",paths_to["fft"]["svr"])
    print("fft -> dac", paths_to["dac"]["fft"])
    print("dac -> out", paths_to["out"]["dac"])

    print("svr -> dac",paths_to["dac"]["svr"])
    print("dac -> fft", paths_to["fft"]["dac"])
    print("fft -> out", paths_to["out"]["fft"])


    print("ways from svr to out with dac and fft in between", 
        countpaths(flows, 'fft')['svr']
      * countpaths(flows, 'dac')['fft']
      * countpaths(flows, 'out')['dac']

      + 
        countpaths(flows, 'dac')['svr']
      * countpaths(flows, 'fft')['dac']
      * countpaths(flows, 'out')['fft'])






