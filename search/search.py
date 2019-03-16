# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


class Node:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def solution(self):
        path = []
        current = self
        while current.action != ():
            #print current.state
            path.append(current.action)
            current = current.parent
        path.reverse()
        return path


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    # """
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    "*** YOUR CODE HERE ***"

    """2.6

    for i in problem.getSuccessors(problem.getStartState()):
      state,action,cost=i
      print state
      print action
      print cost
      print i, problem.getSuccessors(i[0])
      
    """

    """2.9

    s=util.Stack()
    s.push("W")

    print s.pop()
    
    """





    frontier = util.Stack()
    initialNode=Node(problem.getStartState(), (), (), 0)

   # if problem.isGoalState(initialNode.state):
    #    return []


    frontier.push(initialNode)
    explored = set()
    result=[]

    while not frontier.isEmpty():
        removeNode = frontier.pop()
        if problem.isGoalState(removeNode.state):
            return removeNode.solution()
        explored.add(removeNode.state)
        for successor in problem.getSuccessors(removeNode.state):
            node = Node(successor[0],removeNode,successor[1],successor[2])
            if node.state not in explored and node not in frontier.list:
                frontier.push(node)
                #print problem.getSuccessors(node.state)


    return []



        


    util.raiseNotDefined()






def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    frontier = util.Queue()
    initialNode = Node(problem.getStartState(), (), (), 0)
    #if problem.isGoalState(initialNode.state):
     #   return []

    frontier.push(initialNode)

    explored = []
    while not frontier.isEmpty():
        removeNode = frontier.pop()
        if problem.isGoalState(removeNode.state):
            return removeNode.solution()
        explored.append(removeNode.state)
        for successor in problem.getSuccessors(removeNode.state):
            node = Node(successor[0],removeNode,successor[1],successor[2])
            if node not in frontier.list and node.state not in explored:
                explored.append(node.state)
                frontier.push(node)

    return []



    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    frontier = util.PriorityQueue()

    initialNode = Node(problem.getStartState(), (), [], 0)
    # if problem.isGoalState(initialNode.state):
    #   return []

    frontier.push(initialNode, 0)
    removed = frontier.pop()

    explored = []
    explored.append((removed.state, removed.cost))
    while not problem.isGoalState(removed.state):
        for successor in problem.getSuccessors(removed.state):
            visited = 0
            for (state, cost) in explored:
                if successor[0] == state and (removed.cost + successor[2]) >= cost:
                    visited = 1
            if not visited:
                child = Node(successor[0], removed, removed.action + [successor[1]], removed.cost+successor[2])
                frontier.push(child, child.cost)
                explored.append((successor[0], child.cost))
        removed = frontier.pop()
    return removed.action
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    frontier = util.PriorityQueue()

    initialNode = Node(problem.getStartState(), (), [], 0)
    # if problem.isGoalState(initialNode.state):
    #   return []

    frontier.push(initialNode, 0)
    removed = frontier.pop()

    explored = set()
    explored.add((removed.state, removed.cost))
    while not problem.isGoalState(removed.state):
        for successor in problem.getSuccessors(removed.state):
            visited = 0
            totalCost = removed.cost + successor[2]
            evaluateFunction = removed.cost + successor[2] + heuristic(successor[0], problem)
            for (state, cost) in explored:
                if successor[0] == state and evaluateFunction >= (cost + heuristic(successor[0], problem)):
                    visited = 1
            if not visited:
                child = Node(successor[0], removed, removed.action + [successor[1]], totalCost)
                frontier.push(child, child.cost+heuristic(successor[0], problem))
                explored.add((successor[0], child.cost))
        removed = frontier.pop()
    return removed.action
    util.raiseNotDefined()




	
	
	
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
