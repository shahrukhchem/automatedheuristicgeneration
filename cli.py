import argparse
from orchestrator import run_experiment


def main():
    parser = argparse.ArgumentParser(description="LLM-driven heuristic generation and improvement")
    parser.add_argument("--iterations",type=int,default=10,help="Number of heuristic improvement iterations")
    parser.add_argument("--resume",action="store_true",help="Resume an existing experiment")
    args = parser.parse_args()
    run_experiment(iterations=5)
    print('srk')
    


if __name__ == "__main__":
    main()