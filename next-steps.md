
# TO-DO

- [ ] Update Dockerfile and Compose to run migration commands.
- [ ] Implement OAuth login.
- [ ] Start documentation with [Swagger](https://swagger.io/blog/api-development/automatically-generating-swagger-specifications-wi/)
- [ ] Write tasks for the first use case.

## Use Case 1 - Register an investment

### Actor
Investor

### Preconditions
Access to the investment platform

### Primary flow
1. The investor accesses the investment platform.
2. The investor selects the option to register an investment.
3. The investor provides investment details (date, asset, quantity, and value).
4. The system validates the investment information.
5. The system registers the investment in the investor's account.

### Alternative flow
- At any stage of the primary flow, if there is a validation error in the information provided by the investor, the system displays an error message and requests that the information be corrected.

### Postconditions
The investment is registered in the investor's account.



## Use Case 2 - View investment details

### Actor
Investor

### Preconditions
Access to the investment platform
At least one investment has been registered in the investor's account.

### Primary flow
1. The investor accesses the investment platform.
2. The investor selects the option to view investment details.
3. The system displays a list of all the investments registered in the investor's account, showing date, asset, quantity, and value for each investment.
4. The investor selects a particular investment from the list.
5. The system displays the details of the selected investment (date, asset, quantity, and value).

### Alternative flow
- At any stage of the primary flow, if there is an error in the system, the system displays an error message and requests that the action be repeated.

### Postconditions
The investor has viewed the selected investment's details.


## Use Case 3 - Make an investment

### Actor
Investor

### Preconditions
Access to the investment platform

### Primary flow
1. The investor accesses the investment platform.
2. The investor selects the option to make a new investment.
3. The system displays a list of investment options available to the investor.
4. The investor selects a particular investment option from the list.
5. The system displays the details of the selected investment option (such as asset type, risk level, expected return, etc.).
6. The investor enters the amount to invest and confirms the investment.
7. The system deducts the investment amount from the investor's account balance.
8. The system records the new investment in the investor's account.

### Alternative flow
- At any stage of the primary flow, if there is an error in the system, the system displays an error message and requests that the action be repeated.

### Postconditions
The investor has successfully made a new investment and the investment details are recorded in the investor's account.

## Use case 4: Register Assets

**Primary Actor:** Platform Administrator

**Stakeholders and Interests:**

- Platform Administrator: Register information on new assets for user asset calculations.
- Platform Users: Have their asset calculations based on up-to-date registered asset information.

**Pre-conditions:**

The platform administrator has access to the system.

**Basic Flow:**

1. The administrator accesses the investment asset management platform.
2. The administrator chooses the option to register a new asset.
3. The system displays a form for the administrator to fill in the new asset information such as name and value.
4. The administrator fills in the required information and confirms the registration of the asset in the system.
5. The system saves the information of the new asset and displays a message confirming the successful registration.

**Post-conditions:**

The new asset is available on the platform to be used in user asset calculations.

**Alternate Flow:**

- If the administrator does not fill in all required fields in the form, the system displays a message requesting the correct filling of the fields. The use case returns to step 3.
