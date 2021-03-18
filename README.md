# Description of the Exercise

        1. Using Python and MySQL, create a database for a fishing company with the below schema: 
                    a) Boat Table
                        bout_id Has to be Unique
                        bout_Name
                        boat_size in tones
                        boat_length
                        station_id
                        boat_capacity in number of people it can carry
                        fishing (Yes/No)

                    b) Fisher Table
                        fisherman_id Has to be Unique
                        fisher_names
                        boat_id Has to be Unique
                        phone_number
                        email_address
                        Age

                    c) Owner Table
                        owner_id Has to be Unique
                        owner_name
                        boat_id Has to be Unique
                        phone_number
                        email_address

                    d) Station
                        station_id
                        station_name
                        Address

        2. Creare a csv file for all the data sets and upload them into the different tables.


# Exercise Resolution
        The program is intended to allow user to be able to create a MySQL database using Python and be able to write and run queries so as to fetch data from the different tables. 

        The success of this code run is dependent on a user having the following readily installed in their local machine:
              - Python (https://www.python.org/downloads/)
              - Python interpreter e.g.
                      - PyCharm (https://www.jetbrains.com/pycharm/download/)
              - MySQL (https://www.mysql.com/downloads/)
              
        Description of the file functions:
              Create the database
                - create_db()
                
              Create boat table
                - create_boat_table()
              
              Create fishermen Table
                - create_fishermen_table()
                
              Create owners table
                - create_owners_table()
                
              Create station table
                - create_station_id()
                
              Insert data into boat table
                - insert_into_boat()
                
              Insert data into fishermen table
                - insert_into_fishermen()
                
              Insert into owners table
                - insert_into_owners()
                
              Insert into station table
                - insert_into_station()
                
              Commit all the changes  
                - conn.commit()
                
              
