# pylenium-selenium-sample

### Step 1 : Fork the repository 
#### https://github.com/LambdaTest/pylenium-selenium-sample

### Step 2 : Clone the repository
            git clone https://github.com/mukesh-lt/pylenium-selenium-sample.git
            cd pylenium-selenium-sample

### Step 3 : Added your LambdaTest credential in the pylenium.json
        Replace `username` and `accesskey` in remote url or pass `--remote_url https://${LT_USERNAME}:${LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub` while running the test
### Step 4 : Run below commands
           command 1 :  pip install pyleniumio
           command 2 :  pylenium init 

### Step 5 : got to the directory of tests
### Step 6 : Execute the tests
        Single test command :  python -m pytest Serial/LT_ToDo_App/tests/test_todo_app.py
        Parallel test command : python -m pytest Parallel/LT_ToDo_App/tests/test_todo_app.py