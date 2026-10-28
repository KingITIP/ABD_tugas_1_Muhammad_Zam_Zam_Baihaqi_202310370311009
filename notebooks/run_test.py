import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

for nb in ['01_data_profiling.ipynb','02_data_cleaning.ipynb','03_eda_and_insights.ipynb']:
    if not os.path.exists(nb):
        print('SKIP', nb)
        continue
    print('EXEC', nb)
    try:
        with open(nb) as f:
            nbnode = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=1800, kernel_name='python3')
        ep.preprocess(nbnode, {'metadata': {'path': os.getcwd()}})
        out = nb.replace('.ipynb','_executed.ipynb')
        with open(out, 'w', encoding='utf-8') as f:
            nbformat.write(nbnode, f)
        print('OK', out)
    except Exception as e:
        print('ERR', nb)
        print(e)
        print('---')
