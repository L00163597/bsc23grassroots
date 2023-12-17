# bsc23grassroots

![Code Coverage](https://github.com/ruthlennonatu/bsc23grassroots/actions/workflows/coverage-report.yml/badge.svg)
![Django Build](https://github.com/ruthlennonatu/bsc23grassroots/actions/workflows/django.yml/badge.svg)
![Selenium Tests](https://github.com/ruthlennonatu/bsc23grassroots/actions/workflows/selenium-tests.yml/badge.svg?event=push)
![Unit Tests](https://github.com/ruthlennonatu/bsc23grassroots/actions/workflows/unit-tests.yml/badge.svg?event=push)
![OWASP Zap](https://github.com/ruthlennonatu/bsc23grassroots/actions/workflows/dast-scan.yml/badge.svg?event=push)
![Synk Security](https://github.com/ruthlennonatu/bsc23grassroots/actions/workflows/snyk-security.yml/badge.svg?event=push)
![Synk Security](https://github.com/ruthlennonatu/bsc23grassroots/actions/workflows/locust-test.yml/badge.svg?event=push)
---

BScDevOps Assign - Team 2

# Table of Contents
- [Preamble](#preamble)
- [Scrum Master](#scrum-master)
- [Product Owner](#product-owner)
- [Product Development Team](#product-development-team)
- [Project Deadline](#project-deadline)
- [Project Specification](#project-specification)
- [Tools and Services used](#tools-and-services-used)
- [Frameworks](#frameworks)
- [Useful Links](#useful-links)
- [Section Description](#sectiondescription)
- [Risk Register](#risk-register)
- [Tenants of Design](#tenants-of-design)
- [Security](#security)
- [Testing](#testing)
- [Environments](#environments)
- [GitHub Version Control](#github-version-control)
- [Agile project management methods/principles (jira)](#agile-project-management-methodsprinciples-jira)
- [Social Contract](#social-contract)
- [Meetings](#meetings)
- [Communication](#communication)
- [Aglie way of working](#agile-way-of-working)
- [Estimating Story Points](#estimating-story-points)
- [Definition of Ready](#definition-of-ready)

# Preamble
This is the online repository for the DevOps Assignment.

Our product will be delivered using an Agile methodology that embraces the DevOps culture. Please note that our culture embraces change and these documents are treated as living, breathing artefacts that will be continuously updated.

# Scrum Master
- Week 4 Lewis Barett L00145352
- Week 5 Mark Connolly L00166007
- Week 6 Matthew McDaid L00160463 
- Week 7 Pratik L00171104
- Week 8 Faran Khan L00179451
- Week 9 Yeoh Jing Ming L00155848
- Week 10 Mahjabin Chowdhury L00170397
- Week 11 Michael Creamer L00163597
- Week 12 Juliane Costa L00161565
  
# Product Owner
Lewis Barett L00145352 (Permanent)

# Product Development Team
- Testing & QA & Performance: Lewis Barett L00145352 
- Scalability & Admin Access Control: Mark Connolly L00166007
- Compliance & Data Regulations: Matthew McDaid L00160463 
- Data Validation & Inadequate Documentation: Pratik L00171104
- Security Faran Khan: L00179451
- User Support & Training: Yeoh Jing Ming L00155848
- Data Backup and Recovery: Mahjabin Chowdhury L00170397
- Cross Browser Compatibility:  Michael Creamer L00163597
- User Experience: Juliane Costa L00161565

# Project Deadline
Refer to BB for deadlines

# Project Specification
- Clean and simple design
- User access levels (client, administrator)
- Includes at least one self developed api and one webservice 
- To be run over Django

# Tools and services used

1. **PyCharm** - is an integrated development environment (IDE) specifically designed for Python programming, offering features such as code analysis, debugging, and project management.
2.	**Django** - Django is a Python web framework that facilitates the development of robust and scalable web applications by providing a high-level, clean, and pragmatic design.
3.	**Selenium** - is a suite of tools and libraries for automating web browsers, commonly used for testing web applications. Its core component, WebDriver, allows developers to script interactions with browsers in various programming languages.
4.	**Docker** – is a tool that lets you package and run applications with all their parts in a neat, portable box called a container, making it easy to deploy and run consistently across different places. Doing it because during automated workflow
5.	**Snyk** - is a security platform that helps developers find and fix vulnerabilities in their open-source dependencies. It integrates into the development workflow, providing real-time feedback and automated remediation to improve the overall security of software applications.
6.	**OWASP ZAP** - is an open-source DAST tool that integrates into the development workflow, scans a target URL for vulnerabilities and maintains an issue in GitHub repository for the identified alerts.
7.	**Unit testing** - is the practice of testing individual parts of a software program to ensure they work correctly in isolation. It helps catch and fix errors early in the development process.
8.	**Locust Performance testing** - assesses how well a system functions under different conditions, helping ensure it meets speed, responsiveness, and scalability requirements.

# Frameworks
We will be using Django and SQLite

IDE will be Pycharm 2023 Community Edition

# Useful Links
 - Project Slack: https://app.slack.com/client/T0419S2HV9B/C060GSYPG69
 - GitHub: https://github.com/ruthlennonatu/
 - Repository Link: https://github.com/ruthlennonatu/bsc23grassroots.git


# Section	Description
- Process	- Describes the companies process
- Project Log	- Log of project activities
- Costings - Overview of the project cost
- Architecture - Outlines the architecture
- Environments - Overview of the environment set-up
- DR Plan	- Disaster Recovery Plan and procedures
- Requirements - Overview of the requirements for the project
- SLAs - Service level agreements
- Risk Management	- How we manage risk
- Security - Overview of security
- Project Log	- Team log for the project

# Risk Register
These are the current Risks on the project, re-aligned on a weekly basis


# Tenants of Design
The code framework to be used will be Python, we will be programming using the app PyCharm

# Security:
- Synk: Uses static analysis to find security flaws in the code. 
- OWASP Zap: Black box dynamic testing of the application to search for live vulnerabilities 

# Testing:
    Unit testing
    integration testing
    UA
    API Testing
# Environments:
    staging and production
    tight configuration management for consistency and reproducibility
    automated creation and deployments
    integrated and automated pipeline (commit -> test -> deploy)
# Github version control:
    branches used
    version/release management

# Agile project management methods/principles (jira)

# Social Contract
    Mobile phones be left on silent during sprint sessions and class time.
    Be on time for team meetings and class, if you are running late let the group know by sending a message into the Slack channel.
    Everyone has an equal voice and valuable contribution.
    When you are assigned a job, take ownership of it and keep it up to date, do not be afraid to ask others for help, always be honest about your work.
    Do not speak over someone when they are expressing a point, everyone has an equal voice.
    No blame culture.
    Do not be afraid to ask for help, we are all learning.
    No invisble work.
    Ask questions to make sure you understand the task given to you.
    Try have some fun, team work makes the dream work.
    Use Agile methodoligies in the project at all times.

# Meetings
Stand-ups will occur on Every Wednesday/11:30-1:30 during class and Friday on Slack/12:30-1:30
The order that people give their updates will be based starting with the scrum master and going clockwise around the group of those present at the meeting.
Updates will be in the form: What I've done, Impediments, What I plan to do.
Sprint planning will occur at the start of class every week at the end of our sprint.
Please add and update items within <<issue management tool>> a prior to the sprint planning session.
Sprint retro will at the end of our sprint on <<Date/Time>> (timebox retro for 15 minutes, to be organised by the scrum master).
The order that people present their sprint retro updates will be based on The Team 2 list in the Assign_BSc_DevOps_2023.pdf file on blackboard of those present at the meeting.
Points raised in the sprint retro will be noted and posted on the slack channel by the Scrum Master. The Scrum Master is rotated per team member every week.
Backlog refinement will happen on <<date/time>> during our sprint.
Task estimation will be done using poker planner. 
Come prepared to meetings.
Be on time for Stand Ups and meetings.
Mobile phones on silent.
Everyone has equal voice and valuable contribution.
Keep your language and tone professional at all times.
Be honest.

# Communication
Slack is the preferred method of communication.
we will also be using discord for the generasl quick comunication 
Communication in this order: Slack, Discord, Microsoft Teams, Outlook 
If a demonstration is required use Zoom, record the session and upload to the Slack channel.
No Slack communications between 9PM and 9AM.
Raise a problem as soon as you see it.
Respect each other and understand differences in knowledge.
All team documents are to be created using Markdown language and shared on GitHub.
There are no silly questions, if you don’t understand, ask.
Share success stories.
Focus on the positives.
Don’t make assumptions.
Don’t interrupt and cut another person off while they are talking.
Listen when someone is talking, don’t interject.
Zero tolerance for bullying.

# Agile way of working.
If are assigned a job, take ownership of it and keep it up to date.
Stick to your agreed working patterns. Let the team know when you are late or going early.
Keep JIRA board updated at all times.
Update the Scrum Board as you progress the story i.e. don’t update at standup.
Don't be afraid to ask for help.
Don't be afraid to give constructive criticism, as long as it is constructive.
Solve roadblocks within the team. If the impediment can’t be solved within the team then give it to the Scrum Master.
Other
Sprints will start after the stand up that happens at the start of class each week.
The Scrum Master role rotates each week, the schedule is available on the on the process section
Poker Planner will be used for task management and planning.
Each member of the team will work approximitely 3 hours per week, unless they are on vacation.
Our branching stategy will start with gh then the issue number followed by wip

# Estimating Story Points
The teams team's velocity is calculated by the number of story points we achieve on average in the previous sprints.
we will be usign the mthodology 1 story point per hour of work 

The teams current story point velocity is "16".

# Definition of Ready
Story is pointed
Enough information to start
Acceptance criteria is defined
Definition of Done
Code
Min of 1 reviewer
Merged into main
Deployed successfully
Deployment Tested
Documentation
Reviewed, followed and executed by Reviewer
Working solution over documentation
