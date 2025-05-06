# This is a automation script I worked on for a case challenge from Circula. 
* automated several test cases(10) which I created for a specific user-acceptance criteria.
* cross-browser automation implemented
* used pytest/playwright for fixtures implementation
* Faker for fake credential generation.
* conftest contains all fixtures
* test_main.py contains all tests I created. 


# To run locally run the following commands
> You can also use `pip` or `poetry`, if you wish to not use `uv`.
```
brew install uv

git clone https://github.com/bhavana-murugan/circula-challenge.git

cd circula-challenge

uv sync

.venv/bin/pytest test_main.py -v
```


## Test Results Screenshot
![alt text](<Screenshot 2025-03-23 at 10.30.38 PM.png>)
