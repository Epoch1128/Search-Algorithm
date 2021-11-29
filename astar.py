import numpy as np
import argparse
from model import adj, max_epoch

parser = argparse.ArgumentParser(usage="Way selection A* or bfs.", description="A linux implementation of searching algorithm.")

parser.add_argument("--w", type=str, help="The way of selection", default="bfs")

args = parser.parse_args()

def loss(src, tgt=np.arange(start=0, stop=9)):
    score = 0
    for s, t in zip(src, tgt):
        if s!= t:
            score += 1
    return score

def swap_id(src, a, b):
    tgt = []
    for item in src:
        tgt.append(item)
    temp = tgt[a]
    tgt[a] = tgt[b]
    tgt[b] = temp
    return tgt

def A_star(graph, start_point):
    """
    start_point: {state, cost, depth, parent}
    """
    step = 0
    open_list = []
    closed_list = []
    open_list.append(start_point)
    print("Start Searching...")
    while len(open_list) != 0:
        step += 1
    # for idx in range(10000):
        open_list = sorted(open_list, key=lambda x: x["cost"] + x["depth"])
        tgt = open_list.pop(0)
        closed_list.append(tgt)
        if tgt["cost"] == 0:
            print("Finish Searching! Using steps: {}".format(step))
            break
        # 扩展tgt
        pos = tgt["state"].index(0)
        for i, item in enumerate(graph[pos]):
            if item == 1:
                new_point = {
                        "state": swap_id(tgt["state"], pos, i),
                        "cost": loss(swap_id(tgt["state"], pos, i)),
                        "depth": tgt["depth"] + 1,
                        "parent": len(closed_list) - 1
                    }
                if new_point not in open_list and new_point not in closed_list:
                    open_list.append(new_point)
        if step > max_epoch:
            print("Failed to find the solution.")
            break
    tgt = closed_list[-1]
    path = []
    while tgt["parent"] != "root":
        path.append(tgt['state'])
        tgt = closed_list[tgt["parent"]]
    
    path.reverse()
    print("Path to target:")
    print(start_state, end='')
    for item in path:
        print("->{}".format(item), end='')

def bfs(graph, start_point):
    """
    start_point: {state, cost, depth, parent}
    """
    step = 0
    queue = []
    used = []
    queue.append(start_point)
    print("Start Searching...")
    while len(queue) != 0:
        step += 1
        tgt = queue.pop(0)
        used.append(tgt)
        if tgt["cost"] == 0:
            print("Finish Searching! Using steps: {}".format(step))
            break
        # 扩展tgt
        pos = tgt["state"].index(0)
        for i, item in enumerate(graph[pos]):
            if item == 1:
                new_point = {
                        "state": swap_id(tgt["state"], pos, i),
                        "cost": loss(swap_id(tgt["state"], pos, i)),
                        "depth": tgt["depth"] + 1,
                        "parent": len(used) - 1
                    }
                if new_point not in used:
                    queue.append(new_point)
        if step > max_epoch:
            print("Failed to find the solution.")
            break
    tgt = used[-1]
    path = []
    while tgt["parent"] != "root":
        path.append(tgt['state'])
        tgt = used[tgt["parent"]]
    
    path.reverse()
    print("Path to target:")
    print(start_state, end='')
    for item in path:
        print("->{}".format(item), end='')


if __name__ == "__main__":
    # start_state = random.sample(range(0, 9), k=9)
    start_state = [8, 0, 2, 3, 5, 6, 4, 7, 1]
    start_point = {
        "state": list(start_state),
        "cost": loss(start_state),
        "depth": 1,
        "parent": "root"
    }
    print("Initial point: {}".format(start_point))
    if args.w == "astar":
        A_star(adj, start_point)
    elif args.w == "bfs":
        bfs(adj, start_point)
    else:
        raise NotImplementedError("The way is not legal!")