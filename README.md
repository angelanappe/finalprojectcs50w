# CS50W's Job Portal Web Application

## Distinctiveness and Complexity: 
### The Job Portal web application stands out from other projects in this course by addressing the field of job search and hiring. Although it incorporates elements of a social network, it deviates significantly from other course projects by focusing on the creation of professional networks, allowing candidate/employer communication through a messaging section (“Inbox”), in addition to the possibility of attaching .pdf files, thought about the applicants' resumes. This guarantees a different user experience oriented to the CS50 community. 
### The Job Portal Web Application is more than just a job-finding/hiring tool—it's a robust platform designed with intricate features. The effort I put into both the back-end and front-end development ensures a comprehensive user experience. 
### At the core of its complexity is Django, seamlessly integrated into the back-end. Utilizing Django's model system, I've meticulously structured the database. This isn't just for job listings; it manages user profiles and tracks applications. This robust foundation not only enhances user experience but also sets the stage for scalable and maintainable development. 
### The dynamic front-end, powered by JavaScript, adds a layer of sophistication to our project. Through seamless interactivity and real-time updates, users can navigate a fluid and engaging interface. This project’s complexity extends to the responsive design of the application, ensuring optimal usability across different devices.
### The Job Portal Web Application it's a creation made by the integration of Django and JavaScript. This mixture of elements results in a powerful and user friendly job portal platform.

## Overview
### The Job Portal Web Application is a platform designed to connect job seekers with employment opportunities, between people at CS50. This project provides a user-friendly interface for both job seekers and employers, facilitating the process of job search, application or the process of hiring, and management.

## File Structure
### job_offers/
  *	settings.py: Django settings and configurations.
  *	urls.py: URL patterns for routing.
  *	db.sqlite3: to manage the database used in this Project.
  * manage.py: Django management script.
  *	README.md file: description, 
###	joboffers/
  *	models.py: Defines Django models for jobs, user profiles, and applications.
  *	views.py: Contains views for rendering templates and handling user requests.
  *	templates/: HTML templates for different pages.
  *	static/: Holds static files, including CSS and image assets.
  *	urls.py: App-specific URL patterns.
  * forms.py: Defines forms that handle aspects of user registration, profile creation, and job application. 

## Project Features
### 1. User Authentication
 *	User Registration: New users can create accounts by providing basic details.
 *	User Login: Registered users can log in securely to access personalized features like creating a profile, upload resume, posting a job, etc.
 * Templates related: /login, /register, /index.
### 2. Job Search and Listings
 *	View Jobs at CS50: Authenticated users can explore available job opportunities at CS50.
 *	Job Details: Users can view detailed information about each job, including the job title, company, location,   and description of the job.
 * Templates related: /search_jobs, /job_detail
### 3. Save Jobs for Later
 *	Bookmark Jobs: Users can save interesting jobs for future reference.
 *	Quick Access: Access saved jobs from the user dashboard.
 * Templates related: /saved_jobs.
### 4. Job Application
 *	Apply for Jobs: Users can submit job applications directly through the platform with the information that tey provided on “My Information” section, which includes abilities, experience, .pdf resume, etc.
 *	Application Registration: Job seekers can track their applications and remove them if they wanted.
 * Templates related: /step1, /step2, /confirm_application.
### 5. Job Posting
 *	Post Jobs: Employers can post new job opportunities, providing details about the job location, the company name, the requirements needed to stay in the job. 
 *	Job Management: Employers have the ability to manage and update their posted jobs. The owner of a posted job, also has an “Applicants” feature, where they can see who has applied to his/her job and start a conversation with the candidates. This messaging between user/employer will be available at the “Inbox” section.
 * Templates related: /post_job, /candidates, /send_message.
### 6. User Profile
 *	My Information: Authenticated users can view and edit their profile information, where they also can upload their resume (.pdf file), which can be modified any time they want. The information on this section is with what the candidate applies to a job.
 *	Inbox: Users can check if they received messages from a representative of a requested job. Communication can only start from the employer's side. Once the conversation starts, the candidate can reply and send messages as well.
 * Templates related: /my_profile, /edit_profile, /inbox.
### 7. Responsive Design
 *	Mobile Compatibility: The web application is designed to be responsive, ensuring a seamless experience across different devices.
 * Templates related: /layout.
### 8. Carousel
 *	Dynamic Carousel: The homepage features a dynamic carousel showcasing attractive visuals related to job search, catering to both logged-in and non-logged-in users.
 *	Personalized Content: For logged-in users, the carousel content can be personalized based on their status (e.g., displaying different content for new users vs. returning users).
 * Templates related: /layout.
### 9. Pagination
 *	Efficient Navigation: Job listings are paginated for easy navigation, allowing users to explore multiple pages of available jobs.
 * Templates related: /layout.


### Getting Started
## Prerequisites
* Python 3.x
* Django 3.x

## Installation
### Clone the repository:
### git clone https://github.com/angelanappe/job_offer.git
### cd job-portal

### Install dependencies:
### pip install -r requirements.txt

### Run migrations:
### python manage.py migrate

### Start the development server:
### python manage.py runserver

### Access the Job Offer in your web browser: http://localhost:8000/

## Technical Details

###  Brief breakdown of each view function on this project (views.py):

### index(request): Displays the main page and redirects to other pages based on user choice.
### search_jobs(request): Displays available jobs and allow users to search for and apply to jobs.
### post_job(request): Allows users to post a new job.
### job_detail(request, job_id): Displays details of a specific job.
### register(request): Allows users to register for a new account.
### login_view(request): Allows users to log in.
### logout_view(request): Logs out the current user.
### profile(request): Displays user profile information and details about user applications or job posted by him/her.
### edit_profile(request): Allows users to edit their profile.
### step1(request, job_id): Displays the first step of the job application process, handling job selection for form submission.
### step2(request, job_id): Displays the second step of the job application process, with user information.
### confirm_application(request, job_id): Confirms the job application, processes and saves the job application.
### remove_application(request, application_id): User can remove her/his job application.
### send_message(request, receiver_id): Allows users to send a message to another user.
### delete_message(request, message_id): Deletes a message.
### inbox(request): Displays user's inbox.
### saved_jobs(request): Displays jobs saved by the user.
### save_job(request): Handles the saving or unsaving a job.
### delete_job(request, job_id): Deletes a job if the logged-in user is the owner.
### candidates(request, job_id): Displays candidates for a specific job, if the logged-in user is the owner.

###  Brief breakdown of each Model created for this project (models.py):

### User (Custom User Model): Extends Django's built-in AbstractUser to include additional fields.
### Offer_job: Represents a job offer in the system. Stores information related to: title of the job, company name, company information, description of the job, location of the job, etc. 
### User_profile: Represents a user's profile information, like her/his profession, experience, abilities, years of experience, file field for uploading resumes. 
### Application: Represents a user's application for a job. It's fields are the FK from User who applied, FK to the Offer_job, FK to the User_profile and date of application.
### SMS: Represents a message sent between users, storing sender, receiver, content, timestamp. 


# Acknowledgments
### The project was developed as part of a learning experience.
### Inspiration for the project came from the idea for an efficient and user-friendly job portal while you are specializing in a particular study.
### Thank you for reaching the end of the Job Offer Web Application Project README file!