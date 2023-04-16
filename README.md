# Project 4: Konbinet, the best social media

![Hotpot (1)](https://user-images.githubusercontent.com/89135778/230832513-d6722d51-e9ed-41e6-be9a-35451d10d151.png)

## Criteria A: Planning

### Problem definition
My client is the co-owner of a little convenience store at a local school. After meeting with her (see Appendix A) I learned that every Thursday she opens her "Konbini", where she sells products to students and some teachers. However, she feels like it is sometimes hard to know which products the customers want the most, and to let them know what they are selling every week and when. She would like to improve the Konbini's marketing and to promote customer-business interaction, but as students are very busy, she thinks they would not have time for in-person events. She would like the Konbini to have a SNS website where customer can write reviews, upvote the products they want and receive updates and news. My client needs a cost effective, efficient, and more interactive way to promote the Konbini's products and gather feedback from customers.

### Rationale for proposed solution
OOP is the programming paradigm.The application will have a sign up and login system with encrypted password, to increase security. The application will be minimalistic and simple for it to be user-friendly. Once the user has passed the login system, a main menu will appear. There, user will be able to select and emotion and write how she is feeling. She can also access past notes organised in folders by emotion. The tools I am using for this are Python, Kivy, and SQL.
I chose Python because  its codes can be easily written and executed much faster than other programming languages[^1]. Python is an open source and has a lot of libraries to complement the code[^2], so there are multiple options of personalisation for fulfilling the client's necessities. Python is also good for the client, as it is free and my client will not need to buy a license[^3].
I chose Kivy because it is also free and convenient for the client, as it can run in many platforms. Kivy is fresh, fast, flexible, and focused. If the client needed to sell her application in the future, doing that would be completely free and she would not have to pay anything to Kivy. [^4]
I chose SQLite because it is an easy and simple way to look and get all data. SQLite is lightweight, efficient, and easy to integrate in Python applications.  It does not require a separate server process or system, and data can be stored in a single file, making it easy to manage. The use of Client/Server RDBMS would had been necessary for a high volume website, client/server app, very large databases, and high concurrency of simultaneous readers. [^5] As my app does not have data separated from app by the networks, concurrent writers, or very big data, SQLite is a good option that will meet the client’s requirements.
Overall, the combination of Python, Kivy, and SQLite provides a cost-effective, efficient, and user-friendly solution to the client's needs for a mood tracker application.

[^1]: “Advantages of Python over Other Programming Languages.” Vilmate, 2019, https://vilmate.com/blog/python-vs-other-programming-languages/. 
[^2]: “About Python.” Python.org, https://www.python.org/about/. 
[^3]: Citation needed
[^4]: “Philosophy”, https://kivy.org/doc/stable/philosophy.html
[^5]: “Appropriate Uses For SQLite”, https://www.sqlite.org/whentouse.html

### Success criteria:
After meeting with the client ans sending her an email (See Appendix B), we agreed the following success criteria:
1. There is a secure registration and login system with requirements for password and email.
2. The website will 
3. The website will
4. The website will
5. The website will allow the client to write and delete their own posts.
6. The website will give statistical information: number of producsts available, number of .

# Criteria B: Design
## Design statement
I will design and make an website for writing a mood diary for a client who is a student at UWC ISAK Japan. The program will consist on an application for being able to keep track of her mood every day, plus being able to write some notes and having them organized by feeling. It is constructed using the softwares Python, Kivy, and SQLite. It will take 3 weeks to make and will be evaluated according to the criteria A, B, C, and D.

## Creativity
The app is called Konbinet. It is a game of words between "Konbini" (convenience store) and "Net" (network, SNS).

The colour palette for this project is tones ____, with some variations, as these are the favourite colours of the client, and ones that produce _____.

## Test Plan
| TEST                                              | DESCRIPTION                                                                  | PROCEDURE                                                                                                  | EXPECTED OUTPUT                                                                                                                    |
|---------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Unit testing of sign up page (functional)         | This test evaluates the sign up page.                                        | User tries to sign up, not following the password and email requirements. For example, password="password" | An error will be shown in red just below, explaining why it is incorrect. For example, password does not have digits and uppercase |
| Unit testing of new note (functional)             | This test is evaluating how the user add a new note into the notes database. | Click "How are ypu feeling" button, select an emotion, write about it.                                     | The note with the emotion will be saved on the database.                                                                           |
| Unit testing for buttons of feelings (functional) | Functionality of buttons related to emotions                                 | Click on each button and verify.                                                                           | The program will remember which button has just been pressed with a global variable.                                               |
| Unit testing buttons of folders (functional)      | Functionality of buttons related to folders of emotions.                     | Click on each button and verify.                                                                           | The program will lead the user to read the notes that have been written by her and have the tag of the emotion selected.           |
| Unit testing for deleting a note(functional)      | Check if the notes can be deleted from database                              | Select a note in Folders, Mark the checkbox, Click delete                                                  | Note will be deleted from database.                                                                                                |
| Unit testing for statistics (functional)          | Statistics appear in a text message in the user's screen.                    | Click the Statistics button                                                                                | Statistics will appear and they will change when users enter new data in the notes section.                                        |
| Quality of code review (non-functional)           | Use of comments, tabs, and developer-friendly files and variable names       | Check if the program is developer-friendly                                                                 | Program will have comments on every step of the code, and variable names are easy to understand.                                   |
| File organisation review (non-functional)         | Are all files organised? Folders, files, etc                                 | Check Pycharm folder and delete files that have not been used for the project.                             | On the project folder all files should have user-friendly names. All files are organised inside the folder.                        |
| Unit Test: Integration: whole login program       | Check whole code                                                             | Run the program and enter all inputs that a user would put.                                                | The program will not crash and will make its functions.                                                                            |

**Table 1:** Test plan- showing the test plan for my application. The description, expected output, and procedure for each test is also shown.


## System Diagram
**Figure 1**

Fig.1 is the System Diagram. It shows the brand and type of the computer, with its specifications and the Operative System is has. The program runs in Python 3.8 and uses different codes (project_unit3.py, project_untit3.kv). Then, these codes connect with a database of sql files (p3_database.db).

# Wireframe
**Figure 2:**

Fig.2 is the Wirefram Diagram for the program.

## ER Diagrams
**Figure 3:**

Fig. 3 is the ER diagram for the database that my program uses.

## UML Diagrams
**Figure 4:**

Fig. 4 is the UML diagram for the classes of my program.

## Flow Diagrams


## Record of Tasks
xxxxxxxx

**Table 2:** Record of Task- showing the planning and working process of the project. All the steps are related to Planning, Solution Overview analysis and Development, and Functionality (criterias A, B C, and D). The target completion date and the time estimate for each task is also shown.

# Criterion C
### Code
* More details on the comments of the code
### Choose Login or Singup
```.py
# Code
```
explanation

## Sources
- StackOverFlow.com
- YouTube.com
- Chat GPT

## Tools used in Unit 4
- Functions
- For/while loops
- Input Validation
- If statements
- Encryption
- OOP paradigm
- Relational databases
- SQLite, ORM
- Others

# Criteria D: Functionality

### Video
google drive link

### Ideas for further development


# APPENDIX
## A: Notes from First meeting - 10th February 2023
My client and me reunited in a 10-minute meeting.
She wants xxx 

## B: Success Criteria confirmation:
screenshot of email
