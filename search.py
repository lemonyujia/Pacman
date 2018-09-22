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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    # python pacman.py -l tinyMaze -p SearchAgent
    # python pacman.py -l mediumMaze -p SearchAgent
    # python pacman.py -l bigMaze -z .5 -p SearchAgent

    # Initialization
    print('[SearchAgent] test')
    startState = problem.getStartState()
    fringe = util.Stack()
    fringe.push((startState, []))  # (state, action)
    # A dictionary to store successors from current state and visited states
    visited = []
    path = []

    while not fringe.isEmpty():
        state, actions = fringe.pop()
        if state not in visited:
            visited.append(state)
            if problem.isGoalState(state):
                #print('[SearchAgent] test',  actions, "dfs")
                return actions
            successors = problem.getSuccessors(state)
            for next in successors: # (successor, action, stepCost)
                # If the successor has not been visited, push it to stack
                if next[0] not in visited:
                    fringe.push((next[0], actions+[next[1]]))
    return path

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
    # python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
    '''
    # Initialization
    state = problem.getStartState()
    fringe = util.Queue()
    fringe.push(state)
    #visited = set(state) # Store list of visited states
    visited = []
    visited.append(state)
    parent = {} # Store parent path in dictionary <KEY, VALUE> -> <parent_state, action_from_parent_to_current>

    while not fringe.isEmpty():
        state = fringe.pop()
        if problem.isGoalState(state):
            break;
        # Get successor positions
        successors = problem.getSuccessors(state)
        for nextState, action, _ in successors:
            # If the successor has not been visited, push it to queue
            if nextState not in visited:
                #visited.add(nextState)
                visited.append(nextState)
                fringe.push(nextState)
                parent[nextState] = (state, action) # Track the parent path and action
    path = []
    while not state == problem.getStartState():
        p = parent[state]
        path.append(p[1]) # Create a list of actions
        state = p[0] # All the way back to startState
    return path[::-1] # Path reverse
    '''
    # Initialization
    startState = problem.getStartState()
    fringe = util.Queue()
    fringe.push((startState, []))  # (state, action)
    # A dictionary to store successors from current state and visited states
    visited = []
    path = []

    while not fringe.isEmpty():
        state, actions = fringe.pop()
        if state not in visited:
            visited.append(state)
            if problem.isGoalState(state):
                #print('[SearchAgent] test',  actions, "bfs")
                return actions
            successors = problem.getSuccessors(state)
            for next in successors:
                # If the successor has not been visited, push it to queue
                if next[0] not in visited:
                    fringe.push((next[0], actions+[next[1]]))
    return path

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
    # python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
    # python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

    # Initialization
    startState = problem.getStartState()
    fringe = util.PriorityQueue()
    fringe.push((startState, []), 0)  # (state, action, stepCost)
    # A dictionary to store successors from current state and visited states
    visited = []
    path = []

    while not fringe.isEmpty():
        state, actions = fringe.pop()
        if state not in visited:
            visited.append(state)
            if problem.isGoalState(state):
                return actions
            successors = problem.getSuccessors(state)
            for next in successors: # (successor, action, stepCost)
                # If the successor has not been visited, push it to PriorityQueue
                if next[0] not in visited:
                    # Sorted order of items in pq by cost of actions
                    fringe.update((next[0], actions+[next[1]]), problem.getCostOfActions(actions+[next[1]]))
    return path

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
    # Initialization
    startState = problem.getStartState()
    fringe = util.PriorityQueue()
    h = heuristic(startState, problem) # (state, problem)
    fringe.push((startState, []), h)  # (state, action, heuristic function)
    # A dictionary to store successors from current state and visited states
    visited = []
    path = []

    while not fringe.isEmpty():
        state, actions = fringe.pop()
        if state not in visited:
            visited.append(state)
            if problem.isGoalState(state):
                return actions
            successors = problem.getSuccessors(state)
            for next in successors:  # (successor, action, stepCost)
                # If the successor has not been visited, push it to PriorityQueue
                if next[0] not in visited:
                    # Sorted order of items in pq by heuristic function
                    fringe.update((next[0], actions+[next[1]]), problem.getCostOfActions(actions+[next[1]])+heuristic(next[0], problem))
    return path

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
