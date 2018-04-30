Logs Analysis:
 
Project Description:
this is a tool that prints out reports  based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

what is in the output:
-What are the most popular three articles of all time.
-Who are the most popular article authors of all time. 
-On which days did more than 1% of requests lead to errors

Setup:
This project is run in a virutal machine created using Vagrant so there are a few steps to get set up:

Installing the dependencies and setting up the files:
Install Vagrant
Install VirtualBox
Download the vagrant setup files from Udacity's Github These files configure the virtual machine and install all the tools needed to run this project.
Download the database setup: data
Unzip the data to get the newsdata.sql file.
Put the newsdata.sql file into the vagrant directory
Download this project: log analysis
Upzip as needed and copy all files into the vagrant directory into a folder called log_analysis
Start the Virtual Machine:
Open Terminal and navigate to the project folders we setup above.
cd into the vagrant directory
Run vagrant up to build the VM for the first time.
Once it is built, run vagrant ssh to connect.
cd into the correct project directory: cd /vagrant/log_analysis

Load the data into the database:
Load the data using the following command: psql -d news -f newsdata.sql
Note: Checkout Udacity's FAQ page if you are running into any errors here.

Run The Project Already!
You should already have vagrant up and be connected to it.
If you aren't already, cd into the correct project directory: cd /vagrant/log_analysis
Run python log.py
Generating this information will take several seconds.

congratulations you did it.

