# code-wars-v4
Hi everyone! This is where we'll be storing all our code on this project. Some basic guidelines:
- Always pull into your local machine before you start to work, so that you are working on the latest version of the code.
- Make sure your commit messages are descriptive, such as ADDED: `xyz` function in `my_script,py`
- Most importantly, ALWAYS create a new branch when you're adding something new, because if it is buggy it could break everything.
- Ensure you test thoroughly before pushing onto GitHub. Never push buggy code.

## Pirate Signal Composition: *Add more as required*
- x1: (2 digits) - current location x coordinate
- y1: (2 digits) - current location y coordinate
- is_last_primary: (1 digit, "T" or "F") - stores whether the previous move was along the primary direction or the lateral direction. Required for explore_quadrants.py

- **PS:** Ratan here, currently using:<br>
    0th index : pirate Id<br>
    1st index : pirate X<br>
    2nd index : pirate Y<br>
    3rd index : target X<br>
    4th index : target Y<br>


## Team Signal Composition: *Add more as required*

- Ratan here, currently using:<br>
    First 6 indices for x,y of islands<br>
    Next 3 for storing time frames reqd to reach assembly point for gradual defense<br>
    Next goes total no of pirates alive<br>
    Storing 10 closest pirate ids( wrt to assembly point of island)...So 30 in all<br>

    For now total 40 space has been used<br>

