
##################################################################
# Notes:                                                         #
# You can import packages when you need, such as structures.     #
# Feel free to write helper functions, but please don't use many #
# helper functions.                                              #
##################################################################
from collections import deque

def dfs(testmap):

    #dimension of the map
    width =  len(testmap)
    length = len(testmap[0])

    #record the index of starting location and ending location
    index_2 = []
    index_3 = []
    for ms in testmap:
          if 2 in ms:
                index_2.append(testmap.index(ms))
                index_2.append(ms.index(2))
          if 3 in ms:
                index_3.append(testmap.index(ms))
                index_3.append(ms.index(3))

    #starting location
    stack = [[index_2[0], index_2[1]]]

    while len(stack) > 0:
          flag = False
          current_index = stack[-1]
          testmap[current_index[0]][current_index[1]] = 4

          if ((current_index[0] == index_3[0]) & (current_index[1] == index_3[1])):
                for item in stack:
                      if testmap[item[0]][item[1]] == 4:
                            testmap[item[0]][item[1]] = 5
                break

          #push adjacent elements into stack
          if current_index[0] - 1 >= 0: #up
                if (testmap[current_index[0] - 1][current_index[1]] == 0 or testmap[current_index[0] - 1][current_index[1]] == 3):
                      stack.append([current_index[0] - 1, current_index[1]])
                      flag = True
          if current_index[1] - 1 >= 0: #left
                if (testmap[current_index[0]][current_index[1] - 1] == 0) or (testmap[current_index[0]][current_index[1] - 1] == 3):
                      stack.append([current_index[0], current_index[1] - 1])
                      flag = True
          if current_index[0] + 1 < width: #down
                if (testmap[current_index[0] + 1][current_index[1]] == 0) or (testmap[current_index[0] + 1][current_index[1]] == 3):
                      stack.append([current_index[0] + 1, current_index[1]])
                      flag = True
          if current_index[1] + 1 < length: #right
                if (testmap[current_index[0]][current_index[1] + 1] == 0) or (testmap[current_index[0]][current_index[1] + 1] == 3):
                      stack.append([current_index[0], current_index[1] + 1])    
                      flag = True
          if flag == False:
                stack.pop()

    return testmap

def bfs(testmap):

    #dimension of the map
    width =  len(testmap)
    length = len(testmap[0])

    #record the index of starting location and ending location
    index_2 = []
    index_3 = []
    for ms in testmap:
          if 2 in ms:
                index_2.append(testmap.index(ms))
                index_2.append(ms.index(2))
          if 3 in ms:
                index_3.append(testmap.index(ms))
                index_3.append(ms.index(3))

    #starting location
    queue = deque([[index_2[0], index_2[1]]])
    path = {}

    while len(queue) > 0:

        current_index = queue.popleft()
        testmap[current_index[0]][current_index[1]] = 4

        if ((current_index[0] == index_3[0]) & (current_index[1] == index_3[1])):
            while current_index != index_2:
                if testmap[current_index[0]][current_index[1]] == 4:
                    testmap[current_index[0]][current_index[1]] = 5
                current_index = path[str(current_index[0]) + str(current_index[1])]
            testmap[index_2[0]][index_2[1]] = 5
            break

        #push adjacent elements into queue
        if current_index[1] + 1 < length: #right
            if (testmap[current_index[0]][current_index[1] + 1] == 0) or (testmap[current_index[0]][current_index[1] + 1] == 3):
                  queue.append([current_index[0], current_index[1] + 1])    
                  path[str(current_index[0]) + str(current_index[1] + 1)] = [current_index[0], current_index[1]]

        if current_index[0] + 1 < width: #down
            if (testmap[current_index[0] + 1][current_index[1]] == 0) or (testmap[current_index[0] + 1][current_index[1]] == 3):
                  queue.append([current_index[0] + 1, current_index[1]])
                  path[str(current_index[0] + 1) + str(current_index[1])] = [current_index[0], current_index[1]]

        if current_index[1] - 1 >= 0: #left
            if (testmap[current_index[0]][current_index[1] - 1] == 0) or (testmap[current_index[0]][current_index[1] - 1] == 3):
                  queue.append([current_index[0], current_index[1] - 1])
                  path[str(current_index[0]) + str(current_index[1] - 1)] = [current_index[0], current_index[1]]

        if current_index[0] - 1 >= 0: #up
            if (testmap[current_index[0] - 1][current_index[1]] == 0 or testmap[current_index[0] - 1][current_index[1]] == 3):
                  queue.append([current_index[0] - 1, current_index[1]])
                  path[str(current_index[0] - 1) + str(current_index[1])] = [current_index[0], current_index[1]]
    return testmap


def a_star_search (dis_map, time_map, start,end):

  scores = {}
  open_nodes = {}  #nodes not been expanded
  close_nodes = {}  #nodes been expanded
  all_nodes = {}
  pre_time = 0   #time from the first start node to the current start node
  #time_from_start = {}
  h = dis_map[end]  #distance from each node to the end node
  close_nodes[start] = h[start] #initialize the first start node, add to close_nodes

  while True:

      # f = g + h
      g = {}
      f = {}

      #nodes that are available from the start node
      time = time_map[start]
      for each in time:
          if time[each] != None:
              g[each] = time[each]

      for each in g:
          f[each] = g[each] + h[each] + pre_time
          all_nodes[each] = f[each]
          open_nodes[each] = f[each]

      if start == end:
          break

      scores[start] = f

      for each in close_nodes:
          if each in open_nodes:
              open_nodes.pop(each)

      min_value_item = min(zip(open_nodes.values(),open_nodes.keys()))

      start = min_value_item[1]
      close_nodes[start] = open_nodes[start]
      open_nodes.pop(start)

      pre_time = all_nodes[start] - h[start]

  return scores