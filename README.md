# README_

#### Business Model:

The Article Management System aims to drive research by helping experts in a field propose, commision, write, review and edit scientific research papers for an online journal at low cost to themselves.

It allows a select group of experts (General Editors) to propose articles and to supervise and guide the commissioning process by voting and commenting on their suggestions.

The System supports another group of experts (Managing Editors) in managing the journal's scientific double blind peer review process. It guides them through the process in a user friendly way and reduces workload by sending important automatic emails at various stages. The Managing Editors can make use of and facilitate the growth of an extensive network of voluntary experts as authors and reviewers by accessing and updating the systems database of project contributors.

Authors and Reviewers will be contacted automatically and can upload their work directly to the system, making life easier for them and enabling the system to ensure the integrity of the anonymous peer review process, greatly reducing human error where possible.

Lastly, the system assists a group of professional layout editors in preparing reviewed articles for publication.


#### The [Article Management System for General Editors/Article Conception](src) has been implemented.

-[Model](src/Conception/Model.py)

-[View](src/Conception/View.py)

-[Controller](src/Conception/Controller.py)


## 1. Git

I installed Git, generated a project token and was able to set up a remote Github repository. I added a [.gitignore](.gitignore) file and was able to set up Github Actions. I got acquainted with commits as well as push and pull requests. I created new branches and occasionaly ran into trouble with unstaged changes which I fixed with rebase and stash commands. I was able to reset to previous stages of my project. 


## 2. UML 

I created 4 UML diagrams to help in the design and ordering process of the project. The UML diagrams can be found in the [Diagrams folder](Aufgaben/Diagrams).
 
 -The class diagram of the system's architecture was a helpful tool in implementing the Model/View/Controller Principle including databases: [Model_View_Controller_Architecture_Article Conception_AMS](Aufgaben/Diagrams/UML/Model_View_Controller_Architecture_Article_Conception_AMS.jpg)

-The state diagram allows for a more detailed understanding of the editorial workflow process and how it can be reproduced digitally. This is something that would have been produced in close consultation with the editors who would actually be working with the system: [State_Diagram_Review_Management_Workflow_AMS](Aufgaben/Diagrams/UML/State_Diagram_Review_Management_Workflow_AMS.jpg)

-I also included a class diagram of the basic components of my SQL Database which includes the basic structure of article suggestions and shows how the users can suggest/manipulate them: [Class_Diagram_SQL_Databases_Article_Conception_AMS](Aufgaben/Diagrams/UML/Class_Diagram_SQL_Databases_Article_Conception_AMS.jpg)

-Finally, I created a Bounded Contexts Diagram which helped me structure the project as a whole: [Bounded Contexts Diagram](Aufgaben/Diagrams/DDD/Bounded_Contexts_Diagram_AMS.jpg)




## 3. DDD 

The DDD diagram can be found in the [DDD folder](Aufgaben/Diagrams/DDD): 

There are several bounded contexts involved in this project, which I was able to seperate during the design of the [Bounded Contexts Diagram](Aufgaben/Diagrams/DDD/Bounded_Contexts_Diagram_AMS.jpg). General Editors, Managing Editors, Authors, Reviewers and Layout Editors each work seperately from each other and have different responsibilites. These responsibilities are reflected in structure of the code. Necessary interaction between these bounded contexts occurs via a published language in the case of the Authors and Reviwers interacting with the Managing Editors during the review process. This is especially important considering that the review process is blind and reviewers and authors need to be kept anonymous. A downstream Supplier/Customer relationship is necessary during the process of the article moving from its conception phase to the review phase as well as from the review phase to the layout editing phase. Certain changes will have to take place during this process, but the basic information of the article is set during the conception and only added to during the review phase. Same principle applies to the layout editing phase.



## 4. Metrics

I applied three different metrics including [SonarQube](Sonarqube), [Pylint](Aufgaben/pylint_output) and [Flake8](PyBuilder/target/reports/flake8). Sonarqube was particularly helpful in identifying code vulnerabilities. Pylint and Flake8 were helpful style guides, especially considering my aim to apply clean code principles. However, I did have to configure [Pylint](src/.pylintrc) and [Flake8](src/.flake8) as many of their suggestions seemed to be a matter or preference as opposed to necessity and interrupted the build process (f. ex. whitespace conventions)



## 5. Clean Code Development: 

I tried to apply as many clean code principles as I could. I paid particular attention to the following five as they seemed easy to apply, particularly helpful to others trying to read and maintain the code or supported greater code stability.

-Model/View/Controller principle was applied in order to seperate concepts vertically and focus responsibilities on specific issues.

-Single responsbility principle was applied to avoid coupling. For example, in the [Model](src/Conception/Model.py) class, there are three seperate functions that each format the particular database information that they receive for console output ([format_articles_in_review_info_for_print](src/Conception/Model.py?plain=1#L187), [format_contributors_info_for_print](src/Conception/Model.py?plain=1#L244), [format_article_suggestions_info_for_print](src/Conception/Model.py?plain=1#L40)). One can get a good overview of this principle in effect in the [Controller Class](src/Conception/Controller.py?plain=1#L133), where each step in the requested is treated as a call to a seperate function.

-Explanatory variables were used extensively to improve readability. For example, it is easy to differentiate [unreviewed_article_suggestions](src/Conception/Controller.py?plain=1#L38) to [reviewed_article_suggestions](src/Conception/Controller.py?plain=1#L76).

-DocStrings were also used to improve readability. In combination with some of the pycharm shortcuts, DocStrings were extremely helpful in quickly understanding code I had written previously. [In this case](src/Conception/View.py?plain=1#L197) for example, the reader is immediately given the format the function is receiving the data in. This is particularly helpful as articles in different stages of the review process will carry differnt data.

-[Custom Exception Handling Statements](src/Conception/Model.py?plain=1#L100) were created to ease error handling.



[Clean Code Cheat Sheet](Aufgaben/Clean_Code_Cheat_Sheet.txt)




## 6. Build Management: 

As this program is written in Python, I decided to use [PyBuilder](PyBuilder). It runs: 

-[Sphinx Automatic Documentation](PyBuilder/Sphinx/_build/index.html). Unfortunately, I kept running into a mysql import error, which I was unable to fix until now. Therefore, not all DocStrings are shown in the Documentation

-[Unit Tests](PyBuilder/target/reports/unittest). I run my unit tests through PyBuilder. However, I had to [configure](PyBuilder/build.py) the coverage threshold warning as the above mentioned mysql import error was also causing problems for the unit test. 

-[Flake8](PyBuilder/target/reports/flake8) was helpful in enforcing coding style principles and maintaining clean code.



## 7. Unit Tests:

Different Unit tests were implemented to make sure that the individual functions were performing as intended. It took me a while to figure out how exactly to test "print to console statements", which enabled me to test the program's interface ([View Conception Tests](src/Conception/View_tests.py)). Testing the MySQL commands was more straightforward ([Model Conception Tests](src/Conception/Model_tests.py)). Again, I tried to label everything as clearly as possible so to avoid confusion while reading/understanding the unit tests. One example would be the [expected output](src/Conception/View_tests.py?plain=1#L10) variable in the interface tests. It clearly shows what the intention of the test is. 




## 8. Continuous Delivery: 

As the project was set up in GitHub, I decided to use [GitHub Actions](.github/workflows/main.yml) as its Continuous Delivery tool. It runs:

-[Pylint](.github/workflows/main.yml?plain=1#L49)

-[Flake8](.github/workflows/main.yml?plain=1#L64)

-[Unit Tests](.github/workflows/main.yml?plain=1#L77)

I would like to have added PyBuilder to the script, however, the import error for mysql kept popping up and interrupting the build. Therefore, I removed it for the time being.




## 9. IDE: Pycharm 
 
I chose Pycharm as my IDE as I had used it before. I've also worked with IntelliJ. I felt very comfortable using both and have profited particularly from the easy reformatting tools. My favourite Pycharm key shortcuts for Mac are:

-alt-spacebar : This preview window allows a reader to quickly read what exactly is happening in the selected function or class without having to navigate to it, saving time and energy. 

-alt+shift+click : Editing several lines at once can be extremely helpful in certain situations. I use this shortcut very often for indenting purposes.

-hightlight section + alt+shift+g : Same principle as above. Adding carets to ends of selected lines eases the editing process.

-click+cmd+b : This shortcut shows me everywhere I've used the selected class/function/variable in my code. It was particularly helpful for reading/understanding the code.

-shift shift : Allows you to quickly navigate to a specific section of the code.




## 10. DSL:

There are two examples of Domain Specific Languages in this code: 

-A [MySQL](src/Databases) database stores all the necessary article and user information for this project. Accessing the database was easiest to achieve by using [SQL commands](src/Databases/Article_Info_Conception.py?plain=1#L17). Any person with an understanding of SQL should be able to reconfigure the code.

-A [Factory Method Pattern](src/Conception/Datamodel_Article_Conception.py) was also introduced. It was used [here](src/Conception/View.py?plain=1#L161) for example. It was especially helpful in this case for flexibly constructing data for specific datamodels and different article types.



## 11. Functional Programming:

I tried to cover several functional programming principles in the python code:

-No global variables. All data was stored in an SQL Database, which was made accessible only through side effect free [database functions](src/Databases/Article_Info_Conception.py?plain=1#L12) adhering to the single repsonsiblity principle. 

-Final Data Structures. There are no final data structures in Python, but double underscores (name mangling) were used. Variables in the implemented  [factory pattern method](src/Conception/Datamodel_Article_Conception.py?plain=1#L2) were for example "finalized" in this way.

-Higher Order Functions. Several examples for the use of a pure higher order function can be found in the model class where the python [filter functions](src/Conception/Model.py?plain=1#L213) makes use of lambda expressions.

-Anonymous Functions. Python's [lambda expressions](src/Conception/Model.py?plain=1#L267) allow for easy implementation of anonymous functions.

-Side Effect Free Functions. Side effect free functions were used throughout the code.


