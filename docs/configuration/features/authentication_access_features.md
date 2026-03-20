---
layout: default
title: Authentication & Access
parent: Features
grand_parent: Configuration
has_children: false
nav_order: 2
---

## Authentication & Access

## Overview

This section of the Features panel controls features concerning authentication and overall access onto the platform. This is where most features concerning overall security are controlled.

{% include image.html file="authaccess.png" class="docimage" url="https://admin-dev.aapli.app/admin/configurations/application-features" alt="Authentication & Access" caption="Authentication & Access configuration interface" %}

1. **Self-Registration:** This feature will allow users to create their own profile, as opposed to having profiles created for them, giving them access to the platform and greater control over their log-in details.

2. **Authentication Type:** Enabling this feature will give admins the option to choose the kind of authentication they want to implement on the platform for users to comply by when signing in.

    <figure>
    <a class="no_icon" target="_blank" rel="noopener" href="https://admin-dev.aapli.app/admin/configurations/application-features"><img class="docimage" src="/assets/images/authtype.png" alt="Authentication Type" /></a>
    <figcaption>Authentication Type</figcaption>
    </figure>

3. **Two-Factor Authentication:** This feature gives admins the option to enforce 2FA over the sign-in of every user, ensuring greater security and preventing potential simple hacking.

4. **Inactivity Timeout:** Enabling this feature will warn users that they've not registered any form of activity in some time on the platform while they're logged in, and enforce logging out if the inactivity exceeds a defined duration.

    <figure>
    <a class="no_icon" target="_blank" rel="noopener" href="https://admin-dev.aapli.app/admin/configurations/application-features"><img class="docimage" src="/assets/images/inactivity.png" alt="Inactivity Timeout" /></a>
    <figcaption>Inactivity Timeout configuration</figcaption>
    </figure>

5. **Reports:** Activation of this feature will enable visibility of metrics through certain media, for example regular reports & dashboards, for admins to monitor user activity & performance.

6. **Single Session:** Enabling this feature will ensure that a user won't be able to log into the website on any other device if they're already logged in. This will ensure a greater level of security over sensitive data.

    <figure>
    <a class="no_icon" target="_blank" rel="noopener" href="https://admin-dev.aapli.app/admin/configurations/application-features"><img class="docimage" src="/assets/images/singlesession.png" alt="Single Session" /></a>
    <figcaption>Single Session</figcaption>
    </figure>