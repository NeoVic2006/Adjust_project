# Adjust_project

**Installation:** 
Used: **python "^3.9", Django "^3.2.5", pgadmin4 "^5.5"**.                      
Copy this repository: https://github.com/NeoVic2006/Adjust_project.git 

Install dependencies with poetry.lock file usinsg this command: **poetry install**                       

**APIs functionality:**     
**1)** Show the number of impressions and clicks that occurred before the 1st of June 2017, 
broken down by channel and country, sorted by clicks in descending order:

http://127.0.0.1:8000/api/stock?date_to=2017-05-19&groupby=channel&groupby=country&ordering=-clicks   
**Result sample:**   
![image](https://user-images.githubusercontent.com/48185629/126563352-a1b46acb-be0d-4292-b5a2-0df38349630d.png)


**2)** Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order:

http://127.0.0.1:8000/api/stock?date_from=2017-05-01&date_to=2017-05-31&os=ios&groupby=date&ordering=date   
**Result sample:**   
![image](https://user-images.githubusercontent.com/48185629/126563431-bca6f17a-2bee-4079-ae1d-d301be338db2.png)

**3)** Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order:

http://127.0.0.1:8000/api/stock?date=2017-06-01&country=US&groupby=os&ordering=-revenue     
**Result sample:**    
![image](https://user-images.githubusercontent.com/48185629/126563494-f7ba8b40-91a0-4c75-94b1-3ba2443affb9.png)  

**4)** Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. 
Please think carefully which is an appropriate aggregate function for CPI.

http://127.0.0.1:8000/api/stock?country=CA&groupby=channel&ordering=-CPI  
**Result sample:**  
![image](https://user-images.githubusercontent.com/48185629/126563519-b3fc770e-a8bc-47fd-a744-10d1da70099b.png)  

**BD Scheme:**   
 ![image](https://user-images.githubusercontent.com/48185629/126563931-372e2cc9-553d-42d4-9d3c-2c5e298f0cfe.png)




