# How to run
```sh
# Make virtualenv with Python 3.10.14
pip install -r requirements.txt
# cd to repo
PYTHONPATH=. pytest
```


# Results

```
========================================= test session starts =========================================
platform darwin -- Python 3.10.14, pytest-8.3.2, pluggy-1.5.0
rootdir: /Users/300073166/playground/pytestbug
plugins: anyio-4.4.0
collected 2 items                                                                                     

tests/smoke_tests/test_student_ben.py .                                                         [ 50%]
tests/unittests/test_student_john.py .                                                          [100%]

========================================== 2 passed in 0.03s ==========================================
```
