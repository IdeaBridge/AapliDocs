---
layout: default
title: Applications Panel
parent: applications
grand_parent: Operations
has_children: false
nav_order: 1
---

The Application panel is a dedicated section designed for administrators to efficiently manage and create Applications. It provides tools for adding, modifying, enabling/disabling, deleting and duplicating Applications.

{% include image.html file="image018.jpg" class="docimage" url="https://admin.aapli.co/admin/operations/users" alt="Applications Panel" caption="Applications Panel" %}

1. Add: This option is used to create a new application. In the upcoming chapters, we will cover the steps and information required for creating a new application.
2. Application Name: The Application Name section displays a list of all the applications that have been created. Additionally, there is a search bar available where you can enter the name of the application and search for a specific application from the list.
3. Created Date: The Created Date column indicates the date when an application was created. It provides information about when the application was initially set up.
4. Status: The Status column indicates the current status of the application. It can be either active or inactive, depending on its operational state.
5. Actions: When you hover the mouse pointer over the action column corresponding to a specific application, it presents you with four options:
I.	Edit: This option allows you to make changes to the application. You can modify its settings, configurations, or any other relevant information.

II.	Change Status: You can use this option to switch the status of the application. By selecting either "active" or "inactive," you can control whether the application is currently operational or not.
III.	Delete: This option allows you to permanently remove the application from the system. Exercise caution when using this option, as it cannot be undone.
IV.	Duplicate: This option creates a copy of the application. It can be useful if you want to create a similar application without starting from scratch, as it saves time and effort.


**Add**

To create a new application, click on the plus icon next to the "Add" option in aapli application Panel. This will open a new page with various tabs to customize and configure the new application.

{% include image.html file="image019.jpg" class="docimage" url="https://admin.aapli.co/admin/operations/users" alt="Applications Panel" caption="Applications Panel" %}

Creating an application in AAPLI typically involves five steps, which can be organized as tabs within the application. These tabs are Application Settings, Form, Request Workflow, Response Workflow, Roles, and Properties. 
Let's take a closer look at each step/tab:

**General Tabs: Application Settings, Form, and Properties. **

General tabs appear when user selects Response has no work flow in the application settings tab (We will look into details in applications tab) 

{% include image.html file="image020.jpg" class="docimage" url="https://admin.aapli.co/admin/operations/users" alt="Applications Panel" caption="Applications Panel" %}

1. Application Settings: In this tab, you define the general settings and configurations for your application. This includes providing a name and description for the application, and specifying category, type of the application and type of the Workflow. It also involves setting up the preview. 
2. Form: The Form tab allows you to design the user interface and define the data fields that users will interact with user when using the application. You can create forms by adding various types of input fields such as text boxes, dropdown lists, checkboxes, tasks etc. Additionally, you can specify and customize the form's appearance and behavior.
3. Properties: The Properties tab is used to define additional properties or metadata associated with the application or its components. This could include things like custom fields, tags, or labels that provide additional context or information about the application.


**Response Workflow and Task tabs: **

The Workflow tab is used to define the business processes and logic for your application. Here, you can create and configure workflows that automate the sequence of tasks or actions to be performed based on certain conditions.
Once the workflow is defined, the tasks will be assigned accordingly
Request Workflow, Response workflow, and Roles tabs will automatically appear when user selects options “Request has workflow” and “response has Workflow”.

{% include image.html file="image021.jpg" class="docimage" url="https://admin.aapli.co/admin/operations/users" alt="Applications Panel" caption="Applications Panel" %}

1. Request Workflow: The request workflow is designed to gather specific information, answers, or feedback from users. It guides gathered information through a structured process, approvals ensuring that the required data or input is collected and processed in an organized and systematic manner. This workflow is particularly effective for applications where users need to provide specific details or respond to specific queries.
2. Response Workflow: 
The Workflow tab is used to define the business processes and logic for your application. Here, you can create and configure workflows that automate the sequence of tasks or actions to be performed based on certain conditions.
The response workflow is designed for applications that involve both requests and corresponding responses. This type of workflow is adaptable and can be customized based on the application's unique requirements. It manages the flow of interactions where users initiate requests and then provide subsequent feedback or responses.
3. Roles: 
Once you've finished setting up the workflows in the respective Workflow tabs, the next step is to proceed to the Roles tab. In the Roles tab, you can add specific details for different levels of tasks and establish connections by mapping users or roles to these tasks. This ensures an organized approach to Task management within the system.

{% include image.html file="image022.jpg" class="docimage" url="https://admin.aapli.co/admin/operations/users" alt="Applications Panel" caption="Applications Panel" %}

Additionally, we can also see that there is a box positioned above the tabs which allows us to edit the name of the application. 




