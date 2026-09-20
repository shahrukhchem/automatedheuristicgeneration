# Automatically Generated Heuristics

This project explores the automatic generation and improvement of heuristics for difficult optimization problems.

## Idea

Many optimization problems have solution spaces that grow too quickly for exact methods to be practical at useful scales. Heuristics provide practical solutions by using problem structure, rules, and search strategies to find good solutions within a reasonable amount of time.

The goal of this project is to use a language model to generate heuristic algorithms, evaluate their behavior, and iteratively improve them based on their previous results.

## How It Works

The system follows an iterative optimization loop:

1. A general problem description is provided to the language model.
2. The language model generates executable heuristic code.
3. The generated heuristic is evaluated on a collection of problem instances.
4. Each solution is checked for feasibility.
5. A performance objective is calculated for feasible solutions.
6. Runtime, feasibility, objective values, and violations are recorded.
7. The previous heuristic and its results are used to generate an improved version.

This process allows heuristics to be developed through repeated evaluation and feedback rather than being written entirely by hand.

## Project Structure

- `llm.py` - Connects to the language model and requests heuristic code.
- `prompts.py` - Builds prompts for initial heuristic generation and improvement.
- `problem_description.py` - Provides the optimization problem specification used by the generator.
- `orchestrator.py` - Coordinates heuristic generation, evaluation, and iteration.
- `evaluator.py` - Loads generated heuristics, checks feasibility, and calculates objectives.
- `benchmark.py` - Loads the available benchmark instances.
- `Heuristics/` - Stores generated heuristic implementations.
- `Instances/` - Stores benchmark instance data.
- `results/` - Stores evaluation results.

## Generated Heuristic Interface

Every generated heuristic must provide a `solve` function:

```python
def solve(instance):
    # Return a candidate solution for the supplied instance.
    return solution
```

The evaluator is responsible for deciding whether the returned solution is feasible and for calculating its objective value. This keeps heuristic generation separate from validation and measurement.

## Running the Project

Install the language model dependency:

```powershell
pip install google-genai
```

Provide the API key through an environment variable:

```powershell
$env:GEMINI_API_KEY = "your-api-key"
```

Run the command-line interface:

```powershell
python cli.py --iterations 5
```

The number of iterations controls how many generations of heuristics are created and evaluated.

## Evaluation

The evaluator records, for each benchmark instance:

- Whether the generated solution is feasible.
- The objective value of the solution when feasible.
- The runtime of the heuristic.
- Any feasibility violation or execution error.

These measurements make it possible to compare generated heuristics and provide concrete feedback for future iterations.

## Security

Do not commit API keys or other secrets. Keep local credentials in environment variables or ignored local configuration files. Generated heuristics, benchmark outputs, and local editor configuration may also be excluded from version control when appropriate.
