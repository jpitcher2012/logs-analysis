# Logs Analysis
This program generates a report from a database on newspaper articles.

&nbsp;
## Prerequisites
- Install [Python](https://www.python.org/)
- Install [VirtualBox](https://www.virtualbox.org/)
- Install [Vagrant](https://www.vagrantup.com/)
- Install [Git](https://git-scm.com/) (optional - only needed if you want to clone the repository)

&nbsp;
## Installation
- **Option 1:** Clone GitHub repository
  - Open a terminal and navigate to where you want to install the program
  - Run the following command to clone the repository:
  
    `git clone https://github.com/jpitcher2012/logs-analysis.git`

&nbsp;
- **Option 2:** Download ZIP
  - Go to the [repository](https://github.com/jpitcher2012/logs-analysis) in GitHub
  - Click on the "Clone or download" button
  - Click "Download ZIP"
  
  &nbsp;
- After installing, [download the data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and put the file `newsdata.sql` in the `vagrant` directory. 
  
&nbsp;
## Program design
- This program makes use of a Linux-based virtual machine. It has a PostgreSQL database and necessary support software.
- The database includes 3 tables: 
  - The authors table includes information about the authors of articles
  - The articles table includes the articles themselves.
  - The log table includes one entry for each time a user has accessed the site.
- There is one python file, which connects to the database, runs 3 queries, and prints the results. 
 
&nbsp;
## Setting up the database
- Using the terminal, navigate to where you installed the code (in the `logs-analysis` directory)
- Open the `vagrant` directory
- Run the following commands to start up the virtual machine and populate the database:
  - `vagrant up`
  - `vagrant ssh`
  - `cd /vagrant`
  - `psql -d news -f newsdata.sql`
 
&nbsp;
## Running the report
- Run `report.py` while connected to the virtual machine, in the `vagrant` directory 