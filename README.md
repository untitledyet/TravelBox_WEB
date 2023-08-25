# AutoFinder-Web

Technical Documentation for Changing Standards in the Autofinder.bags.ge Project

Introduction The Autofinder.bags.ge project is a website that allows users to search for vehicles on www.myauto.ge, a popular vehicle listing website. The project includes a feature that allows users to filter data on myauto.ge, copy the link from the browser, and upload it to the Autofinder.bags.ge website. The program then automatically checks the added link and records the statements on this link in a separate database. Additionally, users can specify a mobile number and a time duration for which they want to observe the link. The program sends SMS notifications to users when new ads are added to the observed link. Furthermore, a daily script is run to check the expiration time of observations and update the active status in the database accordingly.

Database Structure The Autofinder.bags.ge project has two main databases:

2.1. Database 1: Observation Database This database stores the information related to the observations made by users. It includes the following fields:

Search Link: The link copied from myauto.ge that is being observed. Mobile Number: The mobile number provided by the user. Start Time: The time when the observation was started. Duration: The duration for which the observation is active. Status: The status of the observation (active or not). 2.2. Database 2: Statement Database This database stores the statements found on the observed link. It includes the following fields:

Link: The link that was observed. Statements: The statements extracted from the observed link. Workflow The workflow of the Autofinder.bags.ge project is as follows: 3.1. Adding a New Observation

User enters the website www.myauto.ge. User filters the data to their preference. User copies the link from the browser. User uploads the link to the Autofinder.bags.ge website. User provides a mobile number and specifies the duration for which they want to observe the link. The observation is added to the Observation Database with the relevant information, including the status set to active. 3.2. Checking and Recording Statements

The program automatically checks the added link and extracts statements from the observed link. The extracted statements are recorded in the Statement Database, associated with the observed link. 3.3. Sending SMS Notifications

If a new ad is added to the observed link, the program sends an SMS notification to the user's provided mobile number. The SMS notification includes a link to the newly added ad. 3.4. Daily Script for Expiration Time

A daily script is run at 00:00 to check if the expiration time of observations is less than the current time. If the expiration time is less, the active status in the Observation Database is updated to false. Conclusion The Autofinder.bags.ge project provides a convenient way for users to observe and receive notifications about new ads on myauto.ge. The program automatically checks and records statements from the observed link, and sends SMS notifications to users when new ads are added. Additionally, a daily script is run to update the active status of observations based on their expiration time.
