---
layout: default
title: Microsoft Teams
parent: Integrations
grand_parent: Configuration
has_children: false
nav_order: 1
---

## Creating an MS Teams App Package

Once the user navigates to the Integrations page within the Admin form builder portal, they must click on the button area labelled "Download Microsoft Teams App". 

{% include image.html file="teamspanel.png" class="docimage" url="https://admin-dev.aapli.app/admin/configurations/integrations" alt="Microsoft Teams Panel" caption="Microsoft Teams Panel" %}

This will open up an overlay wherein the user can enter the necessary details to create their custom app.

{% include image.html file="teamssettings.png" class="docimage" url="https://admin-dev.aapli.app/admin/configurations/integrations" alt="Microsoft Teams Settings" caption="Microsoft Teams Settings" %}

1. **App Name (Short):** The short name of the custom app, for display efficiency 

2. **App Name (Full)**: The full name of the custom app 

3. **App Description (Short)**: The short description of the custom app’s function, for efficient reference 

4. **App Description (Full)**: The full description of the custom app, where the user can define how the application works completely 

5. **Accent Color**: The desired color of the app’s icon space 

6. **App Icon** *(must be PNG, at least 128x128px)*: The app icon desired to display next to the app's full name when opening the app 

7. **Outline Icon** *(must be PNG, at least 128x128px)*: The app icon desired to display on the Teams toolbar 

8. **Website URL**: The URL to where the custom app should direct the user 

Once all details are entered, the user can then click Download App Package to receive the created package on their local system. If the user changes their mind about integrating MS Teams, they can click Cancel.

## Uploading the Custom App to Microsoft Teams

Follow the instructions on https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/deploy-and-publish/apps-upload to successfully install the application on Teams, and access the Ideabridge service configured in the custom app.