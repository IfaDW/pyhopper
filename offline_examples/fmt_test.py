import numpy as np

# sys.path.insert(0, ".")
import pyhopper


def of(param):
    print(param)
    return np.random.default_rng().uniform(-5, 5)


search = pyhopper.Search(
    {
        "lr": pyhopper.float(1e-5, 1e-2, fmt="0.1g"),
        "dr": pyhopper.float(0, 0.5, fmt="0.2f"),
    }
)
search.run(of, "max", steps=30, seeding_steps=30)
