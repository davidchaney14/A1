# Infrastructure as code - Assignment 1 #
This Project Detailed Documentation is designed as a review of the task that is required for **assignment 1**:
>Lecturer - John O Raw

>Student Name - David Chaney *(L00169841)*

>Programmeof Study - PGDip in Cloud computing | Module HCTCP90x

In this document, I hope to be brief and to be honest, I hope this document is correct. What I mean by that is I assume it is to serve as type of review of the assignment. I am writing this up after the project is completed and aim to give an overview on all aspects.

I will start with the first task which was to create an automated script or more so a bat file, the name of this file is ‘projectscript.bat’, the code is fairly straight forward, I did find it a bit tricky around trying to some way randomise the name of the main folder but at the same time keep it somewhat human logical and friendly, I decided here to go on using a format of yeartime / module / task, so when it first ran it created the date 20222202 then took the STATVARNAME  of Ioc-CA.

Moving onto the code, there is a file called *test_main.py*, this was used to work on testing code moves etc, once it worked, I would then move it to the *main.py* file, this was just so that the *main.py* file was kept somewhat tidy. I had tried also to move the checking of the host types out to its own module, and call it back into the program, however no matter what I tried it was just would not work. It would obviously be better split off, as an example, directly under it the exact same lines of code is run. I could have just def a function within the program, it would however look much neater on its own. I might try work on that outside of submission.

Overall, I am happy with the project, one of the big hurdles I found with looking for information on things is that there are about 20 in 1 ways to do things in Python, one of the issues is that if a certain structure is not followed then some of the solutions are not always viable.

A quick code review/overview, the code starts with the usual introduction piece at the top, the variable for the *dhcplog* input is created, then our import of the *source.brackets* is called, used later in program. Main function is then created, *cleanInputLog* is then created to start the process of cleaning input, starts with opening the file into *dhcplogopen*, it also makes sure that each time it is ran the content of the file is cleared so its not constantly writing over and over. It then removes or starts on *char 34*, and does a split on the words in line, *DHCPACK* is defined for later use, and it then checks if starting value is *DHCPACK* or *DHCPREQUEST* before running if these conditions are met, if so it then cleans the *MAC (Media Access Control)* address up, looks at the *IP (Internet Protocol)*, *MAC* and then runs over *MAC* to get a *host name type* final its outputted to the screen and to the file *'dhcpcleaned.log’*. Output is also provided to the screen on not so interesting information, but this is not relayed back to the file. Finally the project mentioned error handling and I could have took this up wrong but the last else statement provides some error handling if the file is not at the correct location, I noticed it will just not run, so this provides the user with some information if that event is realised by the program.
