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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    "*** YOUR CODE HERE ***"

    from util import Stack

    frontier = Stack()

    explored = []

    node = problem.getStartState()

    path = []

    cost = 0

    if problem.isGoalState(node):

        return []

    frontier.push((node, path, cost))

    while not frontier.isEmpty():

        node, path, cost = frontier.pop()

        explored.append(node)

        if problem.isGoalState(node):

            return path


        for child_node in problem.getSuccessors(node):

            child = child_node[0]

            child_direction = path + [child_node[1]]

            child_expenditure = problem.getCostOfActions(child_direction)

            if child not in explored:

                frontier.push((child, child_direction, child_expenditure))

    return []


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"

    from util import Queue

    frontier = Queue()

    node = problem.getStartState()

    explored = []

    path = []

    cost = 0

    if problem.isGoalState(node):

        return []

    frontier.push((node, path, cost))

    while not frontier.isEmpty():

        node, path, cost = frontier.pop()

        explored.append(node)

        if problem.isGoalState(node):

            return path

        for child_node in problem.getSuccessors(node):

            child = child_node[0]

            child_direction = path + [child_node[1]]

            child_expenditure = problem.getCostOfActions(child_direction)

            if child not in explored and child not in (state[0] for state in frontier.list):

                frontier.push((child, child_direction, child_expenditure))

    return []


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""

    "*** YOUR CODE HERE ***"

    from util import PriorityQueue

    frontier = PriorityQueue()

    node = problem.getStartState()

    explored = []

    path = []

    cost = 0

    if problem.isGoalState(node):

        return []

    frontier.push((node, path), 0)

    while not frontier.isEmpty():

        node, path = frontier.pop()

        explored.append(node)

        if problem.isGoalState(node):

            return path

        for child_node in problem.getSuccessors(node):

            child = child_node[0]

            child_direction = path + [child_node[1]]

            child_expenditure = problem.getCostOfActions(child_direction)

            if child not in explored and (child not in (state[2][0] for state in frontier.heap)):

                frontier.push((child, child_direction), child_expenditure)

            elif child not in explored and (child in (state[2][0] for state in frontier.heap)):

                for state in frontier.heap:

                    if state[2][0] == child:

                        prev_expenditure = problem.getCostOfActions(state[2][1])

                if prev_expenditure > child_expenditure:

                    frontier.update((child, child_direction), child_expenditure)

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    "*** YOUR CODE HERE ***"

    from util import PriorityQueueWithFunction



    frontier = PriorityQueueWithFunction(lambda x: problem.getCostOfActions(x[1]) + heuristic(x[0], problem))

    explored = []

    node = problem.getStartState()

    path = []

    if problem.isGoalState(node):

        return []

    frontier.push((node, path, heuristic))

    while not frontier.isEmpty():

        node, path, cost = frontier.pop()

        if node in explored:

            continue

        explored.append(node)

        if problem.isGoalState(node):

            return path

        for child_node in problem.getSuccessors(node):

            child = child_node[0]

            child_direction = path + [child_node[1]]

            if child not in explored:

                frontier.push((child, child_direction, heuristic))

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
