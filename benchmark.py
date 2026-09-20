import ast
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
INSTANCES_DIR = PROJECT_ROOT / "Instances"


def load_instances() -> list[dict]:
	"""Load every generated TSP instance from the Instances directory."""
	instances = []

	for instance_path in sorted(INSTANCES_DIR.glob("instances*.txt")):
		instance_data = {"file_name": instance_path.name}

		for line in instance_path.read_text(encoding="utf-8").splitlines():
			if not line.strip():
				continue
			name, value = line.split(" = ", maxsplit=1)
			instance_data[name] = ast.literal_eval(value)

		instances.append(instance_data)

	return instances


