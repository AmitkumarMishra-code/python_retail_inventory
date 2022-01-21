# Python based Retail Inventory Scanner

A simple python program that connects to a PostgreSQL database every 6 hours. It scans the inventory for potential low stocks and sends an email, with a brief report to the specified receiving address.

## Pre-requisites

- Download and install the latest python version from [here](https://www.python.org/downloads/).
- Install PostgreSQL driver psycopg2 using the command **pip install psycopg2** from the terminal.
- Install sendgrid using the command **pip install sendgrid** from the terminal.
- Install dotenv using the command **pip install python-dotenv** from the terminal.

## Run the program
**There are two commands that can be used to run the program from the terminal.**
- The first command is **python main.py** . With this command the program will run till the time it is interrupted with **Ctrl + C** or the terminal is closed.
- The second command is **pythonw main.py** . With this command, the program will keep running in the background till it is explicitly terminated from the task manager or till system shutdown. (The program will show up as **Python** in the task manager.)

