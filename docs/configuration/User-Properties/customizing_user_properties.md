---
layout: default
title: Customizing User Properties
parent: User Properties
grand_parent: Configuration
has_children: false
nav_order: 5
---

## Customizing User Properties

In User Management system, administrators can add custom details to each user's account, such as "Department," "Job Title," or "Phone Number." These extra details help personalize user profiles and make them more useful for organization. Additionally, Admins can match these custom details with existing organization-wide categories when importing user data. This makes it easy to keep everything organized and ensure the information is accurate for effective user management.

{% include image.html file="column_descriptions.jpg" class="docimage" url="https://admin.aapli.co/admin/configurations/user-setting" alt="User Properties" caption="Customizing User Properties" %}

### Column Descriptions

1. **Property Name:** Property name is a column which provides a field where the admin can define the name of the property. For example, Gender, City, country.  

2. **Property Type:** Under the Property type column, admin can define the type of property.  Once we click on the Drop-Down menu on the Property Type field, a list of available properties would appear.  

Below are the available list of Properties. 

{% include image.html file="listf.jpg" class="docimage" url="https://admin.aapli.co/admin/configurations/user-setting" alt="User Properties" caption="Property Types" %}

If "List" is selected as the property type, an additional checkbox will appear under the next column "Use as a Role" column.

3. **Use as Role:** Under the "Use as Role" column, administrators have the option to designate a user property as a "Role." This functionality is enabled when the admin selects "List" as the property type. When this selection is made, an automatic checkbox appears in the "Use as Role" column. 

{% include image.html file="use_as_a_role.jpg" class="docimage" url="https://admin.aapli.co/admin/configurations/user-setting" alt="Use as Role" caption="Use as Role" %}

By checking this box, the admin can assign the corresponding property name as a role, allowing for more specialized and customized user management based on roles within the organization.

4. **Has Parent:** In the "Has Parent" column, administrators can inform the aapli system whether a chosen User Property has a Parent association. This option becomes available when the admin selects "List" as the property type. When this choice is made, an automatic checkbox appears in the "Has Parent" column. 

{% include image.html file="has_parent.jpg" class="docimage" url="https://admin.aapli.co/admin/configurations/user-setting" alt="Has Parent" caption="Has Parent" %}

By checking this box, the admin communicates to the aapli system that the particular User Property is linked to a parent property, allowing for hierarchical organization.

5. **Parent Property:** In the "Parent Property" column, administrators can choose the Parent property from the list of available options. This option becomes accessible when the admin selects "List" as the property type. After checking the automatic checkbox under the "Has Parent" column, a new dropdown menu appears under the "Parent Property" column. 

{% include image.html file="parent_property.jpg" class="docimage" url="https://admin.aapli.co/admin/configurations/user-setting" alt="Parent Property" caption="Parent Property" %}

Within this dropdown, the admin can select the appropriate Parent property, establishing a hierarchical relationship between user properties.

6. **Show in Profile:** By selecting the checkbox beneath the "Show in Profile" column, the corresponding User Property will be displayed in the User Profile. 

{% include image.html file="show_in_profile.jpg" class="docimage" url="https://admin.aapli.co/admin/configurations/user-setting" alt="Show in Profile" caption="Show in Profile" %}

This option allows administrators to choose which user attributes should be visible and accessible within the user's profile information.

7. **Is Read Only:** In the "Is Read Only" column, selecting the checkbox will restrict the user property to read-only mode. When this option is enabled, users will be unable to edit or modify the specific property, ensuring that the information remains static and unchangeable by users.

{% include image.html file="read_only.jpg" class="docimage" url="https://admin.aapli.co/admin/configurations/user-setting" alt="Is Read Only" caption="Is Read Only" %}

8. **Required:** In the "Required" column, selecting the checkbox will set the user property to mandatory. 

{% include image.html file="required.jpg" class="docimage" url="https://admin.aapli.co/admin/configurations/user-setting" alt="required" caption="Required" %}

When this option is enabled, users will be required to provide a value for the specific property when creating or updating their user profile. This ensures that essential information is captured for each user