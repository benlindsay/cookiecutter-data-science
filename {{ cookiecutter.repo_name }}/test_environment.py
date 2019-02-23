import sys
import os


def main():
    if not sys.version.startswith("{{ cookiecutter.python_version }}"):
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                sys.version
            )
        )

    if os.environ["CONDA_DEFAULT_ENV"] != "{{ cookiecutter.env_name }}":
        raise TypeError(
            "ERROR: The {{ cookiecutter.env_name }} environment is not activated.\n"
            + "Activate with `conda activate {{ cookiecutter.env_name }}`.\n"
            + "Create or update the environment with `make environment`."
        )

    print(">>> Development environment passes all tests!")


if __name__ == "__main__":
    main()
