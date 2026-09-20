def get_problem_description():
    return """
Scenario Overview:
A service provider must visit a set of distinct locations exactly once and return to the starting point. Each pair of locations has an associated travel cost (distance, time, or monetary expense).
Objective:
Determine the optimal sequence in which to visit all locations such that the total accumulated travel cost is minimized.
Key Constraints:
Every location must be visited exactly once
The route must form a closed loop (returning to the origin)
No location can be visited multiple times
The complete tour must encompass all designated locations
Problem Characteristics:
The cost structure is typically asymmetric (cost from A→B may differ from B→A)
Costs follow the triangle inequality property in most practical instances
Solution space grows factorially with the number of locations (highly combinatorial)
Both symmetric and asymmetric variants exist depending on application context
Input Provided:
The distance is provided in the format of dictionary  named distances in the format of (city_a, city_b): distance
in the following format:
EXPECTED OUTPUT FORMAT:
The code must return the solution as a list of cities in the order they are visited, starting and ending at the same city.
Example: ['city 1', 'city 3', 'city 2', 'city 4', 'city 1']
"""