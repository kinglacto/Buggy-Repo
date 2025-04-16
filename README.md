### Fixing the Buggy Code

- This code has 30 issues out of which 1 is no code in style.css . 
- The total marks for the entire codebase is 40, some issues have more marks than the other one. Style.css is of 5 marks. It will get scaled down to 20. All team members will get equal marks.
- You are suppose to work in teams of 4 or 5
- Each team member has to identify atleast 4 issues and fix atleast 4 issue. If someone doesn't do this, their marks get deducted.
- You are suppose to work on a git repository as collaborators

### What kind of bugs are there

- Bugs which will break your code
- Bugs might be a single word
- Bugs might be section of removed code
- Bugs might be section of unnecessary code
- Bugs might be useless files
- Bugs might be in the UI/UX of the pages
- Bugs might be in the api calls
- Bugs might be in the dependencies

### submission format

- Make submissions on moodle
- Do not remove .git folder 
- Only 1 submission per team
- Submit it as Corrected_Code.zip

### Add the names of the members and roll numbers of your team below

- Name : Roll Number
- Yashas: 2024101028
- Sushil Raaja U: 2024101002
- Aryama Vinay Murthy: 2024101043
- Sahid Islam: 2024101054
- Adithya J: 2024101012

Github link: https://github.com/kinglacto/Buggy-Repo

### Table to keep track
| ID  | Issue Description                                                         | Identified By | Fixed By     |
|-----|---------------------------------------------------------------------------|---------------|--------------|
| 1   | Style.css is not filled                                                   | Narain        | Aryama   |
| 2   | items.py: router initialised as router= {}                                | Adithya       | Adithya      |
| 3   | items.py: Duplicate create_item definitions with same path                | Adithya       | Adithya      |
| 4   | items.py: delete endpoint with unnecessary two parameters                 | Adithya       | Adithya      |
| 5   | db.py: collection name mismatch                                           | Adithya       | Adithya      |
| 6   | backend/model.py: fixed data type of name to str                          | Yashas        | Yashas       |
| 7   | backend/model.py: add baseclass inheritance to Item                       | Yashas        | Yashas       |
| 8   | frontend/items.html: added div container                                  | Yashas        | Yashas       |
| 9   | items.js: changed post to delete method                                   | Yashas        | Yashas       |
| 10  | items.js: changed application/html to application/json                    | Yashas        | Yashas       |
| 11  | analytics.js: changed localhost port to 8000                              | Yashas        | Yashas       |
| 12  | index.html: changed charset to UTF-8                                      | Yashas        | Yashas       |
| 13  | Script path in profile.html is incorrect (styles/ vs scripts/)            | Sushil        | Sushil       |
| 14  | Element ID mismatch: HTML id="userCounts" vs JS userCount                 | Sushil        | Sushil       |
| 15  | In profile.js, inconsistent use of baseURL in fetch calls                 | Sushil        | Sushil       |
| 16  | Delete button handler uses PATCH method instead of DELETE                 | Sushil        | Sushil       |
| 17  | HTTP Method Mismatch: Submits answer via POST, backend expects GET        | Sushil        | Sushil       |
| 18  | No event listeners for search input/source dropdown in news.html          | Sushil        | Sushil       |
| 19  | Initial loadNews() call doesn't use the reset parameter                   | Sushil        | Sushil       |
| 20  | style.css: Empty CSS File (only comments)                                 | Aryama        | Aryama       |
| 21  | main.py: User routes not imported/included                                | Aryama        | Aryama       |
| 22  | main.py: Analytics router included without prefix                         | Aryama        | Aryama       |
| 23  | main.py: Missing CORS configuration                                       | Aryama        | Aryama       |
| 24  | Added quiz links to all the pages                                         | Aryama        | Aryama       |
| 25  | Wrong HTTP method for get_users (was POST, needed GET)                    | Sahid         | Sahid        |
| 26  | Incorrect delete operation (used delete_all() instead of delete_one())    | Sahid         | Sahid        |
| 27  | Quiz question selection was fixed (not random)                            | Sahid         | Sahid        |
| 28  | Wrong HTTP method for submit_answer (was GET, needed POST)                | Sahid         | Sahid        |
| 29  | Used hardcoded user array instead of fetching from DB                     | Sahid         | Sahid        |
| 30  | Field name errors in analytics calculations (e.g., "names" vs "name")     | Sahid         | Sahid        |
| 31  | Missing plot image in JSON response for analytics                         | Sahid         | Sahid        |
| 32  | Missing navigation menu in analytics.html                                 | Sahid         | Sahid        |
| 33  | Pydantic deprecated .dict() method replaced with model_dump()             | Yashas        | Yashas       |
