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

This is my first own Git project. I installed Git, generated a project token and was able to set up a remote Github repository. I added a .gitignore file and was able to set up Github Actions. I got acquainted with commits as well as push and pull requests. I created new branches and occasionaly ran into trouble with unstaged changes which I fixed with rebase and stash commands. I was able to reset to previous stages of my project. 


## 2. UML 

I created 4 UML diagrams to help in the design and ordering process of the project. The UML diagrams can be found in the [UML folder](Aufgaben/Diagrams).
 
 -The class diagram of the system's architecture was a helpful tool in implementing the Model/View/Controller Principle including databases that I chose to use: [Model_View_Controller_Architecture_Article Conception_AMS](Aufgaben/Diagrams/UML/Model_View_Controller_Architecture_Article_Conception_AMS.jpg)

-The state diagram allows for a more detailed understanding of the editorial workflow process and how it can be reproduced digitally. This is something that would have been produced in close consultation with the editors who will actually be using the project: [State_Diagram_Review_Management_Workflow_AMS](Aufgaben/Diagrams/UML/State_Diagram_Review_Management_Workflow_AMS.jpg)

-I also included a class diagram of the basic components of my SQL Database which includes the basic structure of article suggestions and the users who suggest/manipulate them: [Class_Diagram_SQL_Databases_Article_Conception_AMS](Aufgaben/Diagrams/UML/Class_Diagram_SQL_Databases_Article_Conception_AMS.jpg)

-Finally, I created a Bounded Contexts Diagram which helped me structure the project as a whole: [Bounded Contexts Diagram](Aufgaben/Diagrams/DDD/Bounded_Contexts_Diagram_AMS.jpg)




## 3. DDD 

The DDD diagram can be found in the [DDD folder](Aufgaben/Diagrams/DDD): 

-There are several bounded contexts involved in this project, which I was able to seperate during the design of the [Bounded Contexts Diagram](Aufgaben/Diagrams/DDD/Bounded_Contexts_Diagram_AMS.jpg). General Editors, Managing Editors, Authors, Reviewers and Layout Editors each work seperately from each other and have different responsibilites. These responsibilities are reflected in structure of the code. Necessary interaction between these bounded contexts occurs via a published language in the case of the Authors and Reviwers interacting with the Managing Editors during the review process. This is especially important considering that the review process is blind and reviewers and authors need to be kept anonymous. A downstream Supplier/Customer relationship is necessary during the process of the article moving from its conception phase to the review phase as well as from the review phase to the layout editing phase. Certain changes will have to take place during this process, but the basic information of the article is set during the conception and only added to during the review phase. Same principle applies to the layout editing phase.



## 4. Metrics

I applied three different metrics including [SonarQube](Sonarqube), [Pylint](Aufgaben/pylint_output) and [Flake8](PyBuilder/target/reports/flake8). Sonarqube was particularly helpful in identifying code vulnerabilities. Pylint and Flake8 were helpful style guides, especially considering my aim to apply clean code principles. However, I did have to configure [Pylint](src/.pylintrc) and [Flake8](src/.flake8) as many of their suggestions weren't necessary and interrupted the build process (f. ex. lines of code too long or whitespace conventions)



## 5. Clean Code Development: 

I tried to apply as many clean code principles as I could. I paid particular attention to the following five as they seemed easy to apply, particularly helpful to others trying to read and make sense of the code or supported for greater code stability.

-Model/View/Controller Principle was applied in order to seperate concepts vertically 

-Single responsbility principle was applied to avoid coupling 

-Explanatory variables were used extensively to improve readability

-DocStrings were used to improve readability

-[Custom Exception Handling Statements](src/Conception/Model.py?plain=1#L99) were created to ease error handling



[Clean Code Cheat Sheet](Aufgaben/Clean_Code_Cheat_Sheet.txt)




## 6. Build Management: 

[PyBuilder](PyBuilder) runs: 

-[Sphinx Automatic Documentation](PyBuilder/Sphinx/_build/index.html)

-[Unit Tests](PyBuilder/target/reports/unittest)

-[Flake8](PyBuilder/target/reports/flake8)




## 7. Unit Tests:

-[Test Model Conception](src/Conception/Model_tests.py)

-[Test View Conception](src/Conception/View_tests.py)




## 8. Continuous Delivery: 

[GitHub Actions](.github/workflows/main.yml) runs:

-[Pylint](.github/workflows/main.yml?plain=1#L49)

-[Flake8](.github/workflows/main.yml?plain=1#L64)

-[Unit Tests](.github/workflows/main.yml?plain=1#L77)




## 9. IDE: Pycharm 
 
Favourite Pycharm key shortcuts for Mac

-cmd-c/cmd-v (copy/paste)

-alt-spacebar (preview function)

-alt+shift+click (edit several lines at once )

-hightlight section + alt+shift+g (add carets to ends of selected lines)

-click+cmd+b (shows me where everywhere I've used the class/function/variable in my code) 

-shift shift (allows me to quickly navigate code)




## 10. DSL:

-[MySQL](src/Databases/Article_Info_Conception.py?plain=1#L17)

-[Factory Method Pattern](src/Conception/Datamodel_Article_Conception.py) used [here](src/Conception/View.py?plain=1#L161)




## 11.
