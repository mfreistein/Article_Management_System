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




## 2. UML diagrams can be found in the [UML folder](Aufgaben/Diagrams/UML): 

-[Model_View_Controller_Architecture_Article Conception_AMS](Aufgaben/Diagrams/UML/Model_View_Controller_Architecture_Article_Conception_AMS.jpg)

-[State_Diagram_Review_Management_Workflow_AMS](Aufgaben/Diagrams/UML/State_Diagram_Review_Management_Workflow_AMS.jpg)

-[Class_Diagram_SQL_Databases_Article_Conception_AMS](Aufgaben/Diagrams/UML/Class_Diagram_SQL_Databases_Article_Conception_AMS.jpg)




## 3. DDD diagrams can be found in the [DDD folder](Aufgaben/Diagrams/DDD): 

-[Bounded Contexts Diagram](Aufgaben/Diagrams/DDD/Bounded_Contexts_Diagram_AMS.jpg)




## 4. Metrics

-[SonarQube](Sonarqube)

-Pylint

-Flake8




## 5. Clean Code Development: 

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
