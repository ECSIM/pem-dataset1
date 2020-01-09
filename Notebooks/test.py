import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from art import tprint

NOTEBOOKS_LIST = [
    "Activation Test MEA Constant Current 0.25A",
    "Activation Test MEA Constant Voltage 0.6V",
    "Activation Test MEA Constant Voltage 0.6V-2",
    "Activation Test MEA Constant Voltage "
    "0.6V-3",
    "Activation Test MEA Constant "
    "Voltage 0.6V-4",
    "Activation Test MEA Cycling Potential",
    "Activation Test MEA Standard Protocol (Repeat)",
    "Activation Test MEA Standard Protocol",
    "Standard Test of Nafion Membrane 112"]

EXTENSION = ".ipynb"


if __name__ == "__main__":
    tprint("PEM DATASET1","bulbhead")
    tprint("NOTEBOOKS","bulbhead")
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    print("Processing ...")
    for index, notebook in enumerate(NOTEBOOKS_LIST):
        path = os.path.join("Notebooks", notebook)
        with open(path + EXTENSION) as f:
            nb = nbformat.read(f, as_version=4)
            ep.preprocess(nb, {'metadata': {'path': 'Notebooks/'}})
        with open(path + EXTENSION, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("{0}.{1} [OK]".format(str(index + 1), notebook))
