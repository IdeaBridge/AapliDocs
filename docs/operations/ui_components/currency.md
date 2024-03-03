---
layout: default
title: Currency
parent: UI Components
grand_parent: Operations
has_children: false
nav_order: 9
---

The Currency component enables users to input and display monetary values with a specified currency format.

{% include image.html file="img1.jpg" url="https://admin-dev.aapli.app/admin/operations/application-management" alt="Currency" caption="Currency" %}

**Properties of Currency**

**General**

1. Field Label: Use a clear and descriptive label to guide users on what to choose from the currency options. For example, "Select your preferred currency" or "Currency of payment".
2. Placeholder Text: Use a placeholder text to indicate the expected format or value of the currency input. For example, "USD" or "0.00".
3. Help Text: Provide additional assistance or concise information to clarify aspects of the currency input. For example, "The currency you select will be used for all transactions in this form" or "You can change the currency at any time by clicking on the dropdown menu".
4. Tooltip: Enhance user interaction by providing quick tips or additional context with tooltips when they hover over the currency. For example, "This currency is based on the current exchange rate from Google Finance" or "This currency is not supported by some payment methods".
5. Enable Duplicate: Choose whether to allow or disallow the entry of identical values in the currency for a more streamlined data collection. For example, "Enable duplicate if you want to enter multiple amounts in the same currency" or "Disable duplicate if you want to prevent users from entering the same amount more than once".

{% include image.html file="img2.jpg" url="https://admin-dev.aapli.app/admin/operations/application-management" alt="Currency" caption="Currency" %}

6. Index Number: This automatically appears when enabling duplicate entries, aiding in sorting and referencing. For example, "The index number shows the order of the entries in the currency field" or "You can use the index number to filter or sort the entries by currency".
7. Allow Attachment: Enable users to attach files within the currency for added versatility. For example, "Allow attachment if you want users to upload receipts or invoices in the currency field" or "Disable attachment if you want to limit the input to numeric values only".
8. Show conversion: There is a radio button to show the currency conversion rates. For example, "Show conversion if you want users to see how much their amount is worth in other currencies" or "Hide conversion if you want users to focus on their selected currency only".
9. Filterable: Improve sorting and the user experience through indexing and filtering. For example, "Filterable allows users to search for entries by currency name or symbol" or "Filterable helps users to compare and analyze the data by currency".


**Condition:**

Use in Workflow Checkbox: Integrate the Currency input into workflow processes by selecting this checkbox.

{% include image.html file="img3.jpg" url="https://admin-dev.aapli.app/admin/operations/application-management" alt="Currency" caption="Currency" %}

**Appearance:**

Customize the visual appearance of the Currency input by choosing from "Small," "Medium," or "Large" sizes to align with your design preferences.

{% include image.html file="img4.jpg" url="https://admin-dev.aapli.app/admin/operations/application-management" alt="Currency" caption="Currency" %}

**Validation**

{% include image.html file="img5.jpg" url="https://admin-dev.aapli.app/admin/operations/application-management" alt="Currency" caption="Currency" %}

Required Checkbox: To make sure that the currency is always filled in, select the "Required" checkbox. This will prevent users from submitting the form without entering a currency.

**Permission**

{% include image.html file="img6.jpg" url="https://admin-dev.aapli.app/admin/operations/application-management" alt="Currency" caption="Currency" %}

Field Can Be Hidden from Responder Checkbox: If you want to hide the currency field from the form users or ideators, tick the "Field Can Be Hidden from Responder" option.

Visible to:  To choose who can see the currency field, use the "Visible to" dropdown menu and pick the desired users.


