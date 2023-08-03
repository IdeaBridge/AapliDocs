---
layout: default
title: User Panel
parent: SSO Settings
grand_parent: Configuration
has_children: false
nav_order: 2
---

## SSO Settings User Panel

When the admin opens the SSO Settings, they will have access to the SSO Settings Panel, which allows them to add and manage SSO configurations.

The SSO Settings Panel provides the following options:

1. **Add:** This option allows the admin to add a new SSO setting by providing the necessary details, such as Domain, Provider, and other relevant information required for SSO configuration.

2. **List of Existing SSO Settings:** The panel displays a tabular list of all existing SSO settings in the system. The table is organized with columns for Domain, Provider, and Actions.

3. **Domain:** In this column, the relevant domain information related to the SSO settings will be displayed (e.g., xxx.aapli.co).

4. **Provider:** This column indicates the available SSO providers that the admin can choose from. Two options are provided: Azure and Onpremise AD. The admin can select one of these Active Directory providers for setting up SSO.

{% include image.html file="sso_userpanel.jpg" class="docimage" url="https://admin.aapli.co/admin/configurations/sso-setting" alt="SSO Settings" caption="SSO Settings; User Panel" %}

5. **Actions Column:** This column provides interactive options for each SSO setting. The available actions may include:

a. **Edit:** This action allows the admin to modify the details of an existing SSO setting, such as updating the domain or provider information.
b. **Delete:** This action permits the admin to remove an SSO setting from the system if required.