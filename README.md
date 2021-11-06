# SSD Assignment 3A : Python based Restuarant Bill Calculator (CLI)

> ### Overview
- This project is basic python implemented Bill calculator that reads the **Menu.csv** and displays the formatted output and ask for the following inputs from the user:
    - **Orders**: one by one of the items with respect to the _Item No._, _Plate type(full or half)_ and _quantity_.
    - **Tip**: Either 10% or 20%, if user agrees.
    - The number of people planning to split, if yes.
    - Whether user would like to play game **_Test your luck_**, that offers discounts as well as the chance for bill amount increment.
- At the end, the complete Bill summary is displayed.

> ### Execution
- Execute the following command in terminal in the directory where code is placed
    ``` 
    python bill.py 
    ```

> ### Assumption
- The user input has to be valid.
- In case, user avails discount, the discounted price will be displyed with **negative sign**, else **positive sign** in case of incremented value.