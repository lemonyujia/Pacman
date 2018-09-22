#1 OVERALL
	Project 1: Search in Pacman
	(The project is based on Berkeley pacman projects and adapted by Prof. Vibhav Gogate in his class.)

	Files included: 
	| search.py
	| searchAgents.py
	| README.md

	Author: Yujia Zhai
	Date: 09/22/2018

#2 PARTIAL RUNNING RESULTS
    Question 1 (3 points): Finding a Fixed Food Dot using Depth First Search

        python pacman.py -l tinyMaze -p SearchAgent

		[SearchAgent] using function depthFirstSearch
		[SearchAgent] using problem type PositionSearchProblem
		[SearchAgent] test
		Path found with total cost of 10 in 0.0 seconds
		Search nodes expanded: 15
		Pacman emerges victorious! Score: 500
        ********************
        python pacman.py -l mediumMaze -p SearchAgent

        Path found with total cost of 130 in 0.0 seconds
		Search nodes expanded: 146
		Pacman emerges victorious! Score: 380
		********************
		python pacman.py -l bigMaze -z .5 -p SearchAgent

		Path found with total cost of 210 in 0.0 seconds
		Search nodes expanded: 390
		Pacman emerges victorious! Score: 300

	Question 2 (3 points): Breadth First Search
		python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

		Path found with total cost of 68 in 0.0 seconds
		Search nodes expanded: 269
		Pacman emerges victorious! Score: 442
		********************
		python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

		Path found with total cost of 210 in 0.1 seconds
		Search nodes expanded: 620
		Pacman emerges victorious! Score: 300

	Question 3 (3 points): Varying the Cost Function
		python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

		Path found with total cost of 68 in 0.0 seconds
		Search nodes expanded: 269
		Pacman emerges victorious! Score: 442
		********************
		python pacman.py -l mediumDottedMaze -p StayEastSearchAgent

		Path found with total cost of 1 in 0.0 seconds
		Search nodes expanded: 186
		Pacman emerges victorious! Score: 646
		********************
		python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

		Path found with total cost of 68719479864 in 0.0 seconds
		Search nodes expanded: 108
		Pacman emerges victorious! Score: 418

	Question 4 (3 points): A* search
		python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

		Path found with total cost of 210 in 0.1 seconds
		Search nodes expanded: 549
		Pacman emerges victorious! Score: 300

	Question 5 (3 points): Finding All the Corners
		python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

		Path found with total cost of 28 in 0.0 seconds
		Search nodes expanded: 252
		Pacman emerges victorious! Score: 512
		********************
		python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

		Path found with total cost of 106 in 0.3 seconds
		Search nodes expanded: 1966
		Pacman emerges victorious! Score: 434

	Question 6 (3 points): Corners Problem: Heuristic
		python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

		Path found with total cost of 106 in 5.0 seconds
		Search nodes expanded: 801
		Pacman emerges victorious! Score: 434

	Question 7 (4 points): Eating All The Dots
		python pacman.py -l tinySearch -p AStarFoodSearchAgent

		Path found with total cost of 27 in 4.0 seconds
		Search nodes expanded: 2372
		Pacman emerges victorious! Score: 573
		********************
		python pacman.py -l trickySearch -p AStarFoodSearchAgent

		Path found with total cost of 60 in 19.2 seconds
		Search nodes expanded: 4137
		Pacman emerges victorious! Score: 570

	Question 8 (3 points): Suboptimal Search
		python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5

		Path found with cost 350.
		Pacman emerges victorious! Score: 2360

#3 AUTOGRADER RESULT
    ==================
    Question q1: 3/3
    Question q2: 3/3
	Question q3: 3/3
	Question q4: 3/3
	Question q5: 3/3
	Question q6: 3/3
	Question q7: 5/4
	Question q8: 3/3
	------------------
	Total: 26/25









