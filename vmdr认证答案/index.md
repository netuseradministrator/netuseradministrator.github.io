# VMDR认证答案

## Your objective is to display information about critical assets for the past year. Why are dashboard widgets NOT an appropriate choice?Choose an answer:

**They only display data for the past 90 days.**

Widgets can store real-time data but cannot store trend data.

They only display data for the past 7 days.

They only display data for the past 30 days.







## Which resource allows you to see the maintenance windows，upgrades，and outages of each platform？

**https://platform.qualys.com**
**https://support.qualys.com**
**https://status.qualys.com**





## You have been asked to quickly produce a report which includes a high-level view of your scan results. What is the best way to achieve this?

Choose an answer:

**Run a Scorecard report.**

Run a new vulnerability scan.

Run a Remediation report.



## "Impact if vulnerability is exploited" What is being described in this statement?

Choose an answer:

**Threat Level**

Risk Level

Severity Level

Potential vulnerabilities are found by a Passive Sensor and not by a scanner appliance.





## What is the first stage of the VMDR lifecycle?

Choose an answer:

Vulnerability Management

**Asset Management**

Response

TruRisk Level



## A critical level Qualys Detection Score (QDS) includes which attributes? (Select two.)

Choose all that apply:

**Evidence of exploitation by threat actors**

An Asset Tag with an ACS level of 5.

**Weaponized exploit available**

VMDR 2.0 Prioritzation Report





## Why might you choose Host-based findings for your report instead of Scan-based findings?

Choose an answer:

To enable users with different roles to view vulnerability history.

**To enable you to view vulnerability history from an individual scan.**

To enable you to view vulnerability history of a selection of vulnerabilities.

To enable you to view the vulnerability history of any host asset.





## Why does Qualys recommend performing scans in authenticated mode?

Choose an answer:

**Because it provides the most accurate results with fewer false positives.**

Because it is more likely to discover high-severity vulnerabilities.

Because it includes all QIDs in every scan

Because it includes "risk" in addition to "severity".





## Why might you use Qualys TruRisk?

Choose an answer:

It helps you remediate and fix the vulnerabilities that really count to your organization.

It enables you to manage remediation with ServiceNow integration.

It enables you to identify unauthorized and end-of-life software.

**It prioritizes detected vulnerabilities based on CVSS score and detection age.**





## Which of the following components contribute to a Qualys TruRisk score? (Select two.)

Choose all that apply:

**Qualys Detection Score**

**Asset Criticality Score**

Agentless Tracking





## Which of the following are usually used as the starting point of an Asset Tag hierarchy?

Choose an answer:

Asset Criticality Score

Dynamic Tags

**Static Tags**

TruRisk Score
Severity Level







## Which Qualys sensor runs as a local process on the host they protect?

Choose an answer:

Offline Scanner

**Cloud Agent**

Passive Sensor



## How can a search list be used? (Select three.)

Choose all that apply:

Remediation Tickets

**Report Templates**

**Asset Criticality Score**

**Option Profiles**
Virtual Scanner Appliance



## You need to scan private IP address ranges in a local area network. Which Qualys sensors should you consider? (Select two.)

Choose all that apply:

Passive Sensor

**Physical appliance**

Out of band Sensor

**Virtual appliance**



## You have been asked to organize the assets in your Qualys subscription, including their criticality. Which feature should you use?

Choose an answer:

Severity Level

**Asset Criticality Score**

Asset Groups













## Your organization has recently decommissioned a number of assets. You are concerned that your reports might become inaccurate. What action should you choose to correct this issue?

Choose an answer:

Delete the decommissioned assets from your subscription.

**Purge the decommissioned assets from your subscription.**

They only display data for the past 7 days.

Disable Cloud Agent application modules.









## Why might you create a Search List that includes Real Time Indicators?

Choose an answer:

To help prioritize active security threats.

To help prioritize high severity level vulnerabilities.

**To help prioritize critical assets.**

To help prioritize internet-facing assets.
Asset Tags









## You have been asked to create a scan job which will detect load balancers. How would you configure this?

Choose an answer:

By including this option in a Cloud Agent Configuration Profile.

By enabling this option as part of the Prioritization Report wizard and in an Option Profile.

**By including this option in an Option Profile and adding this Option Profile to the scan job.**

By including this option in an Authentication Record.









## How can you establish a context when creating a Prioritization Report?

Choose an answer:

Asset Groups

Business Units

User Roles

**Asset Tags**











## What is one of the differences between Global Asset View (GAV) and CyberSecurity Asset Management (CSAM)?

Choose an answer:

GAV does not allow you to add business-context through dynamic tagging.

**CSAM enables you to build rules to identify unauthorized software and quickly identify non-compliant assets.**

GAV enables you to enable 2-way integration to sync with ServiceNow CMDB

CSAM does not enable you to define asset criticality using asset tags.





## You want to use QQL to help you decide which patches to install on Windows assets. Which QQL search token would help you to filter the list of patches in the Patch Selector?

Choose an answer:

software:(category1: `Security`)

isSuperseded: false

criticalityScore<1000

**vulnerabilities.detectionAge: default**





## Why should you run a supplemental scan on Cloud Agent hosts, including remote only vulnerabilities?

Choose an answer:

"Remote Only" QIDs are only detected by using a relevant Authentication Record.

"Remote Only" QIDs can only be detected by Cloud Agents on Unix platforms.

An External scanner is always required to detect "Remote Only" QIDs.

**A scanner's remote perspective is required to detect "Remote Only" QIDs**







## Why might you choose to use a Qualys Gateway Server (QGS) as part of your patch deployment process?

Choose an answer:

The QGS is required for assets without the patch management license.

The QGS is beneficial for agents which have not checked in within the last 30 days.

The QGS is required to enable access to the vendor Content Delivery Networks.

**The QGS is used to enable local caching of downloaded patches for all agents.**









## Which of the following statements best describes severity level 3 and 4 vulnerabilities?

Choose an answer:

Severity level 3 and 4 vulnerabilities could potentially allow an attacker to gain root or admin privileges to the vulnerable host.

Severity level 3 and 4 vulnerabilities involve the disclosure of sensitive data that could potentially be very useful to an attacker.

Severity level 3 and 4 vulnerabilities involve the disclosure of open port information.

**Severity levels 3 and 4 vunerabilities involve some type of potential compromise of the host system or one of its applications or services.**







## Why would you choose to select "Enable Agent Scan Merge" in the agent Configuration Profile?

Choose an answer:

This is to enable the Agent to be included in a TruRisk-based Prioritization Report.

This is required to change the Data Collection Interval setting.

**This is to allow scanner appliances to read the Agent Correlation Identifier.**







## What is the difference between a Confirmed vulnerability and a Potential vulnerability?

Choose an answer:

Potential vulnerabilities are found by a Passive Sensor and not by a scanner appliance.

**Confirmed vulnerabilities have more than one active tests, but Potential vulnerabilities have one test.**

Confirmed vulnerabilities have no patch available and Potential vulnerabilities have a patch available.

Confirmed vulnerabilities are found only on internet-facing assets.







## Which of the following is a best practice for using Asset Tags?

Choose an answer:

Use multiple types of rule engines in a single hierarchy

Never mix static tags and dynamic tags in the same hierarchy

Never attempt to next asset tags in a parent-child hierarchy.

**Attempt to group tag hierarchies around some type of common criteria.**









## You work for a large organization and you need to delegate the task of adding assets. Which user roles could you assign to your co-workers? (Select two.)

Choose all that apply:

Reader

**Unit Manager**

Agentless Tracking

**Manager**





## What are two advantages of using a ""Numerical"" widget? (Select two.)

Choose all that apply:

It can track status changes for up to 12 months

**It can be designed to change color, when specific threshold conditions are met.**

It displays the Data Collection Interval setting.

**It can include trend data.**





## What is a consideration of using Asset Groups to organize assets in your subscription?

Choose an answer:

The Asset Tag which gets created based on this Asset Group will have an Asset Criticality Score of 4.

Host assignment is determined by Asset Tag Rule Engine

**Groups are typically nested, creating various parent/child relationships**







## How does Qualys TruRisk help you manage vulnerabilities?

Choose an answer:

It removes disabled vulnerabilities from a Prioritization Report.

It prioritizes detected vulnerabilities based on CVSS score and detection age.

It calculates risk based on the asset's environment.

**It places detected vulnerabilities within the context of your critical and non-critical assets.**





## What is included in a Zero-touch Patch Job? (Select two.)

Choose all that apply:

**A recurring job schedule**

A Remediation Ticket

A Qualys TruRisk score

**Patches that are selected using QQL**





本文是将youtube大佬答案摘抄至此，照着视频抄不爽。原视频链接

https://youtu.be/34F-J2Mfr5Y?si=X67auJKmbecdR1Cr
