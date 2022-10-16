# PropertyManagement
### Project Description
This project contains a web-based data analysis and visualization reporting tool for property management. 

On the website, the user is able to upload a pre-defined CSV format file, and the webpage will output the data table as well as bar charts, and pie charts for the data. The website will also execute some calculations based on the given data and output the expenses and income for property Owens on a monthly basis. 

### Technologies Used
Django, Pyhton3, HTML, ChartJS, Squlite, Tailwind, VSCode, Pandas

### Install Technologies (Mac, Through Terminal)
If you do not have Python3 installed on your laptop, make sure you do that first : )
Then start installing the following:

1. Install Virtual Environment: 
  * `pip3 install virtualenv`
2. Insatll Django3.2:
  * `pip install django==3.2`


### How to Run the Project(Mac, Terminal)
1. git clone `git@github.com:summerhanyuezheng/PropertyManagement.git` to the location of your choice

2. Activate Virtual Environment: 
  - (Make sure you are in the `PropertyManagement` directory)
    * `virtualenv env`
    * `cd env`
    * `source bin/activate`
(by now, if you see `(env)` displaying at the beginning of command line, you are on the right track :))
  
3. Insatll Django :
  * `pip install Django==3.2
  
4. Install Pandas:
    * `pip install pandas`
    
5. run the server:
   - (right now, if you are in `env` directoty, make sure to change to `mysite` directory first, then do the following)
    * ` python manage.py runserver`
    * then you should see a message saying: `Starting development server at http://127.0.0.1:8000/`
    * copy the url with method `report` as `http://127.0.0.1:8000/report` and paste into a browser of your choice
(by now, you should see the web page displaying successfully)

6. upload the file named `propertySheet` in the cloned folder , click submit, all the table and charts should display with given data
   

