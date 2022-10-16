# PropertyManagement
### Project Description
This project contains a web-based data analysis and visualization reporting tool for property management. 

On the website, the user is able to upload a pre-defined CSV format file, and the webpage will output the data table as well as bar charts, and pie charts for the data. The website will also execute some calculations based on the given data and output the expenses and income for property Owners on a monthly basis. 

### Technologies Used
Django, Pyhton3, HTML, ChartJS, Sqlite, Tailwind, VSCode, Pandas

### Install Technologies (Mac, Through Terminal)
If you do not have Python3 installed on your laptop, make sure you do that first : )
Then start installing the following:

1. Install Virtual Environment: 
  * `pip3 install virtualenv`


### How to Run the Project(Mac, Terminal)
1. git clone `https://github.com/summerhanyuezheng/PropertyManagement.git` to the location of your choice

2. Activate Virtual Environment: 
  - (Make sure you are in the `PropertyManagement` directory)
    * `virtualenv env`
    * `cd env`
    * `source bin/activate`
(by now, if you see `(env)` displaying at the beginning of command line, you are on the right track :))
  
3. Install Django :
   `pip install Django==3.2`
  
4. Install Pandas:
    * `pip install pandas`
    
5. run the server:
   - (right now, if you are in `env` directory, make sure to change to `mysite` directory first, then do the following)
     * ` python manage.py runserver`
     * then you should see a message saying: `Starting development server at http://127.0.0.1:8000/`
     * copy the url with method `report` as `http://127.0.0.1:8000/report` and paste into a browser of your choice
     
     
(by now, you should see the web page displaying successfully)

6. upload the file:
 * find the file named `propertySheet` in the cloned folder and drag the file into the `choose File` box on the web page, click submit, all the table and charts should display with given data 
 - (if google chrome does not work when you click on `choosefile` button, try to use Safari)
   

