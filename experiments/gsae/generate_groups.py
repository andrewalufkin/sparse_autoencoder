import json
from pathlib import Path


def generate_group_mapping(latent_dim: int, group_size: int) -> dict[str, int]:
    """Generate non-overlapping groups of specified size."""
    mapping = {}
    for i in range(latent_dim):
        mapping[str(i)] = i // group_size
    return mapping


def main(latent_dim: int = 16384, group_size: int = 8) -> None:
    group_spec = {
        "latent_dim": latent_dim,
        "group_size": group_size,
        "mapping": generate_group_mapping(latent_dim, group_size),
    }
    out_path = Path(__file__).parent / "group_spec.json"
    with open(out_path, "w") as f:
        json.dump(group_spec, f, indent=2)


if __name__ == "__main__":
    main()
