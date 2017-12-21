
from app import db

from app.models import User, Paper

# user = User(name="admin", email="admin@admin.com", password="admin")
# db.session.add(user)
# db.session.commit()
#
# user1 = User(name="user", email="user@user.com", password="user")
# db.session.add(user1)
# db.session.commit()

paper = Paper(title="Organizing Your Social Sciences Research Paper: 3. The Abstract",
              abstract="Sometimes your professor will ask you to include an abstract, "
                       "or general summary of your work, with your research paper. The abstract "
                       "allows you to elaborate upon each major aspect of the paper and helps readers "
                       "decide whether they want to read the rest of the paper. Therefore, enough key "
                       "information [e.g., summary results, observations, trends, etc.] must be included "
                       "to make the abstract useful to someone who may want to examine your work.How do you "
                       "know when you have enough information in your abstract? A simple rule-of-thumb is to "
                       "imagine that you are another researcher doing a similar study. Then ask yourself: if "
                       "your abstract was the only part of the paper you could access, would you be happy with "
                       "the amount of information presented there? Does it tell the whole story about your study? "
                       "If the answer is no then the abstract likely needs to be revised.",
              status="Under Review", author_id=1)
db.session.add(paper)
db.session.commit()

paper1 = Paper(title="A Research on Cloud Computing Security",
               abstract="This paper gives an overview on cloud computing security. To clarify cloud security, "
                        "a definition and scope of cloud computing security is presented. An ecosystem of cloud "
                        "security is shown to illustrate what each role in industry can do in turn. Then security "
                        "impacts of cloud security for both customers and operators are analyzed. To overcome "
                        "challenges from cloud security, many state-of-the-art technical solutions, e.g., continuation "
                        "protection mechanism, IDM, data security, and virtualization security are discussed. Finally, "
                        "best practices on perspective of operator are summarized and a conclusion is conducted.",
               status="Under Review", author_id=1)
db.session.add(paper1)
db.session.commit()

paper2 = Paper(title="CyberCSP: Integrating cybersecurity into the computer science principles course",
               abstract="The demand for cybersecurity professionals is projected to grow substantially, with the US "
                        "Bureau of Labor Statistics reporting that employment in cybersecurity within the US will grow "
                        "by 18% from 2014 to 2024, much faster than the average for all occupations. As creating a "
                        "cyberspace workforce has become a matter of national security for every country, "
                        "cybersecurity needs to be taught at all levels, to all students, in the educational system. "
                        "The good news is that cybersecurity is also a topic that students from a wide variety of "
                        "backgrounds find interesting, and as a result, it motivates them to study computing too. Over "
                        "the past two decades, there has been an increased effort worldwide to incorporate computer "
                        "science and computational thinking into the middle and high school curriculum. The CS10K "
                        "initiative in the US has led to projects to introduce computer science at the K-12 "
                        "educational level. One of these initiatives, the new Advanced Placement (AP) course in "
                        "Computer Science Principles (CSP), was designed to introduce computer science in an engaging "
                        "way, show students how computing is relevant in their lives, and to attract a diverse group "
                        "of students to computing. The CSP Curriculum Framework allows for multiple implementations of "
                        "the CSP course, permitting course designers to develop courses to engage and attract specific "
                        "groups of students and that focus on specific themes in computing. This paper describes an "
                        "approach to develop a new CSP course, CyberCSP, which integrates cybersecurity first "
                        "principles throughout the course. The approach builds on an CSP course that was created from "
                        "a previous collaboration between the Computer Science Department at Rochester Institute of "
                        "Technology, Rochester, New York, and the Webster Central School District in Webster, "
                        "New York. The paper discusses the background, details of the earlier CSP course, how relevant "
                        "cybersecurity content was identified, and then integrated into the CSP course to create the "
                        "CyberCSP varia- t of the Computer Science Principles course.",
               status="Under Review", author_id=1)
db.session.add(paper2)
db.session.commit()

paper3 = Paper(title="« Prev Back to Results | Next A study of students' progress through introductory computer "
                     "science programming courses",
               abstract="Given the growing demand for skilled workers from the Computer Science field, the high "
                        "attrition rate of entering Computer Science students is a serious problem at most "
                        "universities. Much research exists on evaluating the reasons of failure with the introductory "
                        "Computer Science curriculum referred to as the CS1, CS2 and CS3 courses. Current research has "
                        "proposed methods to predict patterns and characteristics to offer early detection of students "
                        "likely to fail. The problem is difficult to understand due to the existence of many possible "
                        "reasons students drop-out from the computer science curriculum. Factors such as student "
                        "transfers, course diversity, and students repeating failed courses are seldom considered. The "
                        "goal of this paper is to extend the understanding of the attrition rates for entering "
                        "Computer Science students by analyzing the progress of student success through 10 years of "
                        "course data. The impact of transfer students is considered as well as the frequency students "
                        "repeat the CS1, CS2, and CS3 courses, and their success. Analysis is done by following the "
                        "students up until graduation. An analysis is also made to determine how courses tend to "
                        "predict the graduation success rate.",
               status="Under Review", author_id=1)
db.session.add(paper3)
db.session.commit()

paper4 = Paper(title="Analysis of the teaching-learning methodology adopted in the introduction to computer science "
                     "classes",
               abstract="To meet socio-cultural demands imposed by the new millennium and its implications for "
                        "education, it was necessary for teachers and students to participate actively in the "
                        "teaching-learning process. In this context, the classes' evaluation by students has been a "
                        "tool widely used in various universities in different countries. For institutions and "
                        "teachers, these assessments allow knowing and measuring the results, further analysis of the "
                        "institutional status, reviewing projects, adjusting goals, diagnosing weaknesses and "
                        "correcting possible deviations. For the monitoring and improvement of this process, "
                        "it was necessary to create instruments that aimed to evaluate the performance of the proposed "
                        "changes. The teaching-learning methodology adopted in the Introduction to Computer Science "
                        "classes may be a process that makes it difficult to understand the principles of language "
                        "programming for undergraduate students in Computer Science and related areas, generating high "
                        "failure and course drop out rates. This paper presents an analysis of the results obtained in "
                        "the Introduction to Computer Science classes taught in five Engineering courses, "
                        "of the Faculty of Gama (FGA) at University of Brasília (UnB). It was analyzed the evaluation "
                        "questionnaire answered by the undergraduate students in 2017, perform validation of the "
                        "questionnaire, check the level of students satisfaction in relation to the evaluated subject "
                        "and the association among the level of satisfaction, the percentage of practical activities "
                        "of the discipline, student performance and the level of absenteeism. 519 responses were "
                        "studied, 63% of students reported satisfaction with the classes taken, however a significant "
                        "number of students 37% reported dissatisfaction with assessment practices and the dynamics of "
                        "the classes.",
               status="Under Review", author_id=1)
db.session.add(paper4)
db.session.commit()
