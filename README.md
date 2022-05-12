# Fresh Casts

<p align="center">
  <img src="" alt="Mockup of how the website looks on desktop, laptop and tablet"/>
</p>

[Link to Website](https:///)

[GitHub Repo](https://github.com/RickofManc/fresh-casts)


***

## About

Fresh Casts is a website built for people who enjoy listening to podcasts, and would also like to share and discover new shows and series.
Through clear and intuitive design, Fresh Casts goal is ensure the pleasure of listening, sharing and discussing podcasts is accessible to all possible user groups, no matter of age or background.


***


## Index - Table of Contents

* [User Experience R&D](#user-experience-research-and-design)
    * [Strategy](#Strategy)
    * [Scope](#Scope)
    * [Structure](Structure)
    * [Skeleton](#Skeleton)
    * [Surface](#Surface)
* [Features](#Features)
* [Data Model](#Data-Model)
* [Manual Testing](#Manual-Testing)
* [Deployment](#Deployment)
* [Credits](#Credit)


***


## User Experience Research and Design



### Problem Statement

It's difficult to find a website where you can share and discuss podcasts.
Listeners may feedback or rate a podcast within a listening app, however these apps generally do not allow listeners to post and discuss liked podcasts.
Podcast listenership continues to increase with over 2 million shows to choose from, and by nature humans are social, we like to converse.
There's an opportunity to help people share podcasts, making it easier to discuss and find shows that may have slipped under their radar.



### Objective

By summer 2022, I will develop and deploy a website that promote the sharing and discussion of podcasts they are enjoying. 
All visitors will be able to listen to shared podcasts. Users who create a Fresh Casters profile will be able to comment and like shared shows, as well as posting their own favourites.The site will meet WCAG 2.1 AA standards, and will be thoroughly tested to ensure all user groups can access and enjoy content.



### Design Thinking

Following a Design Thinking process, I've identified four key personas to empathize with and define their requirements.


<details><summary><b>User Personas</b></summary>
  <img src="readme-images/user-personas.png" alt="User Personas; Listener, Commenter, Blogger, Podcaster"/>
</details><br />


This phase led to User Stories being drafted complete with Acceptance Criteria and initial Tasks for the development phase. User Stories have been added to GitHub [here](https://github.com/users/RickofManc/projects/4) and are being tracked through to completion.


#### Primary strategic aims for the website
PPP

The roadmap below highlights the high-level strategic opportunities versus the importance and viability/feasibility of development for the MVP (Minimal Viable Product):

<p align="center">
  <img src="" alt="Strategic Opportunities Roadmap"/>
</p>


### Scope

An agile approach of keeping the in scope features simple and aligned to the strategy for the MVP will be adopted.Below is a list of the leading features for the the Fresh Casts MVP.


#### In Scope Features
* Create an accessible website that follows convention for sites built to inform.
* Conventionally the site will have a fixed Header, Navbar and Footer.
* Main Menu accessible through a hamburger icon.
* By default, the homepage will show the latest posts in ascending order.
* A clickable link will enable Fresh Casters to find out more information on the post.
* Podcasts will be playable directly in the page browser.
* A user account will provide access to Commenting, Liking, Blogging.
* Fresh Casters will be supported with a page dedicated to FAQ's.
* A 'Contact Us' page will enable Fresh Casters to get in touch with Site Admin.
* An Accessibility Statement will inform of how Fresh Casts cares about accessibility.
* The site will be responsive across differing devices, from mobile first design through to 5K screens supported.


#### Potentially In Scope Features (Time Dependant for MVP)
* Recent activity - Pulling commenting, liking, posting data from across the site into Fresh Casters profile page.
* Search and learn - Using keywords, Fresh Casters will be able to search and hone in their choices.
* Update own content - providing Fresh Casters with an option to edit their own posts and comments.
* Podcast downloading - enabling Fresh Casters to listen offline.
* Preferred app - allowing Fresh Casters to listen to a podcast in favourite listening app.



#### Beyond MVP Release Features
* Single Sign On (SSO) - Use social apps such as Google, Facebook and Twitter to sign-in.
* Connecting Fresh Casters - Provide chat service to allow the community to interact directly.




### Structure

This website will be structured with the following design considerations.

* A Hub and Spoke structure, where the main content will be the homepage hub, and spokes are the pages to find out more information on a post. The spokes will also house the useful pages such as Sign-up, FAQ, Contact Us, About Us etc.
* Each post will be displayed in a shortened list view for the homepage with just enough information to entice the user, and also a full description which will open in it's own page.
* All spoke pages will have a text link to allow the user to return back the their original homepage view.
* Users wishing to add a comment or like will be asked to first create a user account as a Fresh Caster. Once a brief form has been completed and submitted, Site Admin will be notified and requested to approve or deny the application. 
* Having a user account will allow users to interact with the site, adding comments, likes and being able to post their own podcast review.
* Users will also be able to contact Site Admin with a range of issues through a contact form available within the Main Menu and Footer. 
* All pages will be available to users consistently through either the Main Menu or Footer - this should ensure users are never two clicks away from where they would like to be.


The final structure for the MVP may differ slightly as development progresses, and from user feedback and testing.



### Skeleton

Key to the UX attributes is the speed and ease for which users can learn about new podcasts, or what fellow users think about a podcast. 

The 'Hub and Spoke' structure should provide users with content from their initial landing, and allowing their intrigue to click on a post and find out more, or refine the content by choosing one of six categories located conveniently on the Navbar (when in the desktop and tablet view).

Aesthetically pages will be clean to promote the information, and allow users to flow between differing categories and expanding posts to learn more and add a Like. Convention from popular information based sites will be adopted so users feel at home and therefore capture their engagement within the first few seconds.



#### Flowchart

A flowchart outlining the customer journey has been created using [Lucidchart](https://www.lucidchart.com/pages/).
The final application may differ slightly as development progresses and from user feedback.


<p align="center">
    <img src="" alt="Fresh Casts Flowchart"/>
</p>


#### Wireframes

As part of this phase wireframes for mobile and desktop devices have been produced using [Balsamiq](https://balsamiq.com/wireframes/) (see image below - the wireframes are located within the project [Repo](wireframes)).

The website is responsive through differing screen widths being designed for mobile first to a max-width of 767px. Tablets are responsive from 768px through to 1023px, and desktops from 1024px upward. 


<p align="center">
    <img src="readme-images/fresh-casts-mobile-wireframes.png" alt="Fresh Casts wireframe for mobile devices" />
</p>


### Surface 

PPP.


#### Colour Palette

This palette has been carefully selected to bring high contrasting colours to improve accessibility to visually impaired users. As the primary aim of the site is to inform, Black text on a White background will be adopted throughout. The Teal based accents will be used to highlight buttons, points of reference or navigation and other key pieces of user information.


<p align="center">
    <img src="readme-images/fresh-casts-colour-palette.png" alt="Fresh Casts Colour Palette"/>
</p>


#### Font Family

**Roboto Flex and Roboto Condensed**

Today, people are constantly switching between devices, resizing browsers, and spreading our viewports across multiple screens. So Google commissioned Font Bureau to re-imagine Roboto to “flex”. This was achieved by amplifying the original design to an extreme range of weights, grades, widths and optical sizes.

I've selected this popular font family for its clean lines and legibility, being widely used on news and information based websites. It also offers a condensed style which can be used for larger text headers to offer some contrast to body text, without having to use a multiple font families.


<p align="center">
    <img src="readme-images/fresh-casts-roboto-flex-font.png" alt="Fresh Casts Font"/>
</p


***


## Features

### Current Features

* PPP
<p align="center">
    <img src="" alt=""/>
</p





### Future Features

PPP


### Meta data

Meta data is included within the HTML head element to increase the traffic to the website. Furthermore, the site page is titled appropriately as another method of informing users of their location.


***


## Data-Model 

PPP

***


## Automatic Testing 
  
  
## Manual Testing 

PPP
  

### Code 

The code on each file has been assessed using the appropriate validation service; W3C Markup for HTML, W3C for CSS, and PEP8 Online for Python & Django.

Below are the summarised results from these tests:

PPP


### Browser

PPP


### Device

PPP


### Accessibility 

PPP


### Performance 

PPP


### User Stories

The leading user stories have been tested to ensure the priority aims of the website have been delivered. 
Below is a summary of the story's validation.
                                                                   


### Bugs

PPP



## Deployment

This project was deployed using the steps below with version releasing active. Please do not make any changes to files within this repository as any changes pushed to the main branch will be automatically reflected on the live website. Instead, please follow the steps below which guide you to forking the website where changes can be made without impact to the live website. Thanks!


### Fork and Deploy with GitHub

<details>
    <summary></summary>

To fork this website to either propose changes or to use as an idea for another website, follow these steps:
1. If you haven't yet, you should first set up Git. Don't forget to set up authentication to GitHub.com from Git as well
1. Navigate to the [Fresh Casts](https://github.com/RickofManc/fresh-casts).
1. Click the 'Fork' button on the upper right part of the page. It's in between 'Watch' and 'Star'
1. You will now have a fork of the VV Pizzas repository added to your GitHub profile. Navigate to your own profile and find the forked repository to add the required files.
1. Above the list of forked files click the 'Code' button
1. A drop-down menu will appear providing a choice of cloning options. Select the one which is applicable to your setup
Further details on completing the last step can be found on GitHub's [Fork a Repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) page

To deploy from GitHub, follow these steps:
1. Log into your GitHub repository, create a GitHub account if necessary
1. Click 'Settings' in the main Repository menu
1. Click 'Pages' from the left-hand side navigation menu
1. Within the Source section, click the "Branch" button and change from 'None' to 'Main'
1. The page should automatically refresh with a url displayed
1. Test the link by clicking on the url

The url for this website can be found here https://freshcasts.herokuapp.com/

</details>

### Create data model and integrate using an API

<details>
    <summary></summary>

Create a Spreadsheet (Data Model)
PPPP


Setup API
1. Navigate to [Google Cloud Platform](https://cloud.google.com/gcp?utm_source=google&utm_medium=cpc&utm_campaign=emea-gb-all-en-bkws-all-all-trial-e-gcp-1011340&utm_content=text-ad-none-any-DEV_c-CRE_500227884420-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20GCP%20~%20General%23v1-KWID_43700060384861702-kwd-26415313501-userloc_9041106&utm_term=KW_google%20cloud%20platform-NET_g-PLAC_&gclid=CjwKCAiAvaGRBhBlEiwAiY-yMH6ZzZToth-9fTjp0B_qAE91ulGwN7jIb0KBGW5TbmN8Z5w9JE1noRoCSmIQAvD_BwE&gclsrc=aw.ds)
1. If you do not already have a profile then follow the basic steps for creating an Account, via clicking on the 'Get Started for Free' button in the upper right corner.
1. Once the previous step is complete, create a new project with a unique title
1. You should now arrive at the project dashboard and be ready to setup the required credentials:
    * Access the navigation menu from clicking on the hamburger button
    * Select APIs and Services, followed by 'Library'
    * Search for and select Google Drive API -> Enable
    * Search for and select Google Sheets API -> Enable
    * Click Enable to navigate to 'API and Services Overview' 
    * Click Create Credentials in the upper left of the screen
    * For Credential Type, select 'Google Drive' from the dropdown
    * For 'What data will you be accessing' select Application Data
    * For 'Are you planning to use this API with Compute Engine...?' choose 'No, I'm not...'
    * Click Next
    * Within the Create Service Account page, enter a Service Account Name
    * Click Create and Continue
    * Next within 'Grant this service account access to project', choose Basic -> Editor from the 'Select a Role' dropdown
    * Click Continue
    * Next within 'Grant users access to this service account', choose 'Done'
    * On the following, click on the 'Service Account Name' you created to navigate to the config page
    * Navigate to the Keys section
    * Select 'Add Key' dropdown -> Create New Key.
    * Select 'JSON' -> Create - the file will download to your machine
    * From your local downloads folder, add file directly to your Gitpod workspace, and rename the file to creds.json
    * Within the file, copy the value for 'client email'. Paste this email address into the 'Share' area of your Google Sheet, assigning the role of Editor

Enable API within IDE
1. From within your GitPod IDE terminal, enter 'pip3 install gspread google-auth'
1. At the top of your Python file add the following lines:

    ```
    import gspread
    from google.oauth2.service_account import Credentials
    ```
    
1. Below this add the following code:

    ```
        SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]

        CREDS = Credentials.from_service_account_file('creds.json')
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
        SHEET = GSPREAD_CLIENT.open('vv_pizzas')
        console = Console()
        install(show_locals=True)
    ```
</details>


### Deploy with Heroku
<details>
    <summary></summary>

* The requirements.txt file in the IDE must be updated to package all dependencies. To do this:
    1. Enter the following into the terminal: 'pip3 freeze > requirements.txt'
    1. Commit the changes and push to GitHub

* Next, follow the steps below:
    1. Login to [Heroku](https://heroku.com/), create an account if necessary
    1. Once at your Dashboard, click 'Create New App'
    1. Enter a name for your application, this must be unique, and select a region
    1. Click 'Create App'
    1. At the Application Configuration page, apply the following to the Settings and Deploy sections:
        * Within 'Settings', scroll down to the Config Vars section to apply the credentials being used by the application. In the Reveal Config Vars enter 'CREDS' for the Key field and paste the all the contents from the creds.json file into the Value field
        * Click 'Add'
        * Add another Config Var with the Key of 'PORT' and the Value of '8000'
        * Within Settings, scroll down to the Buildpacks sections, click to Add a Buildpack
        * Select Python from the pop-up window and Save
        * Add the Node.js Buildpack using the same method
        * Navigate to the Deploy section, select Github as the deployment method, and connect to GitHub when prompted
        * Use your GitHub repository name created for this project
        * Finally, scroll down to and select to deploy 'Automatically' as this will ensure each time you push code in GitHub, the pages through Heroku are updated
    1. Your application can be run from the Application Configuration section, click 'Open App'

</details>

    

***


## Credit

### People

* Mentor Brian Macharia for guiding and advising throughout the projects lifecycle on how to improve UX and my code.

Support with how to develop ideas into code also came from various online resources:

* PPP


### Python Library Dependencies and Packages

* [Google Sheet]PPP
* [Rich Console](https://rich.readthedocs.io/en/stable/console.html) to style terminal text, and as formatted traceback for development.
* [Pandas](https://pandas.pydata.org/) to receive data from the external Google Sheet into a DataFrame.
* [Datetime](https://docs.python.org/3/library/datetime.html) to add the date and time to the order before sending to the kitchen.


### Software & Web Applications

* [Balsamiq](https://balsamiq.com/) - Used to build wireframes in the Skelton phase.
* [LucidChart](https://www.lucidchart.com/pages/) - To map out the flow of data.
* PPP - Heroku, Django, Bootstrap, PPP This website was coded primarily using Python3, HTML5, CCS3 with [GitPod](https://gitpod.io/) used for the IDE and [GitHub](https://github.com/) as a hosting repository.
* [W3schools](https://www.w3schools.com/) - Source of 'How to...' information throughout the build.
* [Stack Overflow](https://stackoverflow.com/) - Source of 'How to...' information on Python code.
* [Python Tutor](https://pythontutor.com/) - For testing sections of code.
* [Wave](https://wave.webaim.org/) - Accessibility Testing to ensure content is readable for all users.
* [HTML Validator](https://validator.w3.org/) - For validating HMTL code.
* [W3 CSS Validator](https://jigsaw.w3.org/css-validator/validator) - For validating CSS code.
* [PEP8 Validator](http://pep8online.com/)  - For validating Python code.
* [Code Beautify](https://codebeautify.org/) - For validating the layout of code.
* [IE NetREnderer](https://netrenderer.com/index.php) - For browser testing on Microsoft IE versions 7-10.
* [LambdaTest](https://www.lambdatest.com/) - For cross browser testing including, macOS Safari and Opera.
