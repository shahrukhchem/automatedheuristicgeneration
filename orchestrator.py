from pathlib import Path
from llm import generate_heuristic
from prompts import initial_heuristic_prompt, improvement_prompt
from problem_description import get_problem_description
from evaluator import evaluate_heuristic
from benchmark import load_instances
import json
PROJECT_ROOT = Path(__file__).parent

HEURISTICS_DIR = PROJECT_ROOT / "Heuristics"
RESULTS_DIR = PROJECT_ROOT / "results"

def run_experiment(iterations: int, resume: bool = False):
    """
    Run the heuristic generation and improvement experiment.
    Args:
        iterations (int): Number of heuristic improvement iterations.
        resume (bool): Whether to resume an existing experiment.
    """
    # Placeholder for the actual experiment logic
    print(f"Running experiment with {iterations} iterations. Resume: {resume}")
    for iteration in range(1, iterations+1):
        if iteration == 1:
            currprompt=initial_heuristic_prompt(get_problem_description())
        else:
            previous_code = load_previous_heuristic(iteration)
            # Load previous results
            previous_results = load_previous_results(iteration)
            currprompt=improvement_prompt(get_problem_description(),previous_code,previous_results)
        print()
        print("=" * 60)
        print(f"ITERATION {iteration}")
        print("=" * 60)
        print("Generating heuristic...")

        # This will eventually come from llm.py
        heuristic_code = generate_heuristic(currprompt)
        heuristic_path = (HEURISTICS_DIR / f"H{iteration:03d}.py")
        heuristic_path.write_text(heuristic_code,encoding="utf-8")
        print(f"Saved: {heuristic_path}")

        print("Evaluating heuristic...")
        # This will eventually come from evaluator.py
        inst=load_instances()
        results = evaluate_heuristic(heuristic_path,inst)
        # --------------------------------------------------
        # 4. Save results
        # --------------------------------------------------
        result_path = (RESULTS_DIR / f"H{iteration:03d}.json")
        
        totalobj=0
        totalobj = sum(result["objective"]for result in results if result["feasible"] and result["objective"] is not None)

        print(f"Total objective: {totalobj}")

        save_results(result_path,results)
        print(f"Results saved: {result_path}")
        # --------------------------------------------------
        # 5. Results will be fed into the next LLM call
        # --------------------------------------------------
        print("Iteration complete.")
        
        


def load_previous_heuristic(iteration: int) -> str:
    previous_iteration = iteration - 1
    path = (HEURISTICS_DIR/ f"H{previous_iteration:03d}.py")
    return path.read_text(encoding="utf-8")


def load_previous_results(iteration: int) -> dict:
    previous_iteration = iteration - 1
    path = (RESULTS_DIR/ f"H{previous_iteration:03d}.json")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)
# ----------------------------------------------------------
# Temporary placeholder functions
# We'll replace these with llm.py / evaluator.py later.
# ----------------------------------------------------------



def save_results(result_path: Path, results: dict):

    
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(
        json.dumps(results, indent=2),
        encoding="utf-8"
    )

