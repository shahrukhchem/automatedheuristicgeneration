def initial_heuristic_prompt(problem_description: str) -> str:

    return f"""You are an optimization algorithm researcher.Your task is to design a heuristic for the following optimization problem.
PROBLEM:
{problem_description}
Requirements:
1. Generate a practical heuristic algorithm.
2. The heuristic must produce a solution for a given problem instance.
3. Prioritize solution quality while keeping runtime reasonable.
4. The generated solution will be checked by an external evaluator.
5. Do not assume that your solution is feasible. The evaluator will verify it.
6. Return only executable Python code.
7. The code must contain:

def solve(instance):
    ...

The solve() function must return the solution.

Do not include markdown fences.
Do not include explanations outside the code.
"""

def improvement_prompt(problem_description: str,previous_code: str,previous_results: str) -> str:
    return f"""You are an optimization algorithm researcher.You previously generated a heuristic for this optimization problem.
PROBLEM:
{problem_description}
PREVIOUS HEURISTIC:
{previous_code}
PERFORMANCE OF PREVIOUS HEURISTIC:
{previous_results}
Your task is to generate an improved heuristic.Improved heuristic is defined where the over all cost is improved from previous heuristic.
Analyze the performance results and identify weaknesses in the previous heuristic. If the previous heuristic has an error, or the solution that is not feasible that means the  heurisitc is not acceptable. Modify the algorithm to address those weaknesses.
Requirements:
1. Preserve useful ideas from the previous heuristic.
2. Make genuine algorithmic improvements rather than simply changing
   arbitrary constants.
3. The new heuristic must remain executable Python.
4. The solve() interface must remain:

def solve(instance):
    ...

5. The external evaluator will check feasibility and calculate the objective.
6. Return only executable Python code.
7. Do not include markdown fences.
"""