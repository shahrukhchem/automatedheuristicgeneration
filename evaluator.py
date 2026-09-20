import importlib.util
import time
from pathlib import Path
def load_heuristic(heuristic_path: Path):
    """Dynamically load a generated heuristic Python file."""
    spec = importlib.util.spec_from_file_location("generated_heuristic",heuristic_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate_heuristic(heuristic_path: Path, instances):
    """
    Evaluate a heuristic on a collection of instances.
    """
    heuristic = load_heuristic(heuristic_path)
    results = []
    for instance in instances:

        #print(f"Evaluating {instance['file_name']}...")

        start_time = time.perf_counter()

        try:
            # Run the heuristic
            solution = heuristic.solve(instance)

            runtime = time.perf_counter() - start_time

            # Check feasibility
            feasible, violation = check_feasibility(
                instance,
                solution
            )

            # Calculate objective only if feasible
            if feasible:
                objective = calculate_objective(
                    instance,
                    solution
                )
            else:
                objective = None

            results.append({
                "instance": instance['file_name'],
                "feasible": feasible,
                "objective": objective,
                "runtime_seconds": runtime,
                "violation": violation
            })

        except Exception as e:

            runtime = time.perf_counter() - start_time

            results.append({
                "instance": instance['file_name'],
                "feasible": False,
                "objective": None,
                "runtime_seconds": runtime,
                "error": str(e)
            })

    return results


def check_feasibility(instance, solution):
    """
    Check whether the solution satisfies all constraints.
    """
    if not isinstance(solution, (list, tuple)):
        return False, "Solution must be a list or tuple of city names."

    number_of_cities = instance["number_of_cities"]
    city_names = set(instance["coordinates"])

    if len(solution) != number_of_cities + 1:
        return False, (
            f"Solution must contain {number_of_cities + 1} cities, "
            f"but contains {len(solution)}."
        )

    if not solution:
        return False, "Solution cannot be empty."

    if solution[0] != solution[-1]:
        return False, "The first and last city must be the same."

    unknown_cities = set(solution) - city_names
    if unknown_cities:
        return False, f"Solution contains unknown cities: {sorted(unknown_cities)}."

    if len(set(solution[1:-1])) != number_of_cities - 1:
        return False, "Each city between the first and last must occur exactly once."

    if set(solution[:-1]) != city_names:
        return False, "Solution must visit every city exactly once before returning."

    return True, None


def calculate_objective(instance, solution):
    """Return the total distance of the solution route."""
    distances = instance["distances"]
    return sum(
        distances[(city_a, city_b)]
        for city_a, city_b in zip(solution, solution[1:])
    )