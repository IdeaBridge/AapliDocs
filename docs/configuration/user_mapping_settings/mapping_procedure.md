---
layout: default
title: Mapping Procedure
parent: User Import Mapping
grand_parent: Configuration
has_children: false
nav_order: 1
---

## User Import Mapping

Once admin clicks and open the User import mapping, the below page would open. Here the admin is required to select the Active directory from which the user data will be mapped. 

{% include image.html file="userimportsettings1.jpg" class="docimage" url="https://admin-dev.aapli.app/admin/configurations/user-import-mapping" alt="User Import Mapping" caption="User Import Mapping" %}

Under the user properties, list of properties defined in User Properties  will be displayed and Provider properties will have the list of Properties Defined in the company’s AD. 

To map a user property with the Providers property, admin needs to click on the corresponding drop down and select the appropriate Provider property. 

{% include image.html file="userimportsettings2.jpg" class="docimage" url="https://admin-dev.aapli.app/admin/configurations/user-import-mapping" alt="User Import Mapping" caption="User Import Mapping" %}

For example, to map the First name of user property, we have we have selected the Display Name from the dropdown list of the corresponding “Provider Properties”. Please note the First Three Users properties (First Name, Last Name, Email) are predefined and cannot be changed, however the rest of the User Properties can be edited. Clicking on “Save” button will complete the mapping procedure. 


