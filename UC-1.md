# First Feature

[Use Case 1 - Register an investment](use-cases.md##-Use-Case-1).

## Representation of Users and Investments

This session aims to represent users and their investments in a financial management system. Below you'll find the characteristics of the modeled entities.

### User
The User entity has the following attributes:

- id (unique identifier)
- name (user's name)
- email (user's email address)
- password (user's password)

### Investment Portfolio
The Investment Portfolio entity has the following attributes:

- id (unique identifier)
- name (investment portfolio's name)
- user_id (identifier of the portfolio's owner)

### Investment
The Investment entity represents an investment in a specific type of Investment Portfolio (STOCKS, FIXED INCOME, OTHERS). It has the following attributes:

- id (unique identifier)
- type (investment type - STOCKS, FIXED INCOME, OTHERS)
- applied_value (amount invested)
- quantity (number of units)
- ticker (stock code or fixed income  title)
- user_id (identifier of the investment's owner)
- portfolio_id (identifier of the investment's portfolio, if it is part of one)

### Stock
The Stock entity represents a specific stock. It has the following attributes:

- id (unique identifier)
- name (stock's name)
- ticker (stock code)

### Fixed Income
The Fixed Income entity represents a specific fixed income. It has the following attributes:

- id (unique identifier)
- name (fixed income 's name)
- ticker (fixed income 's code)

With these updates, all investments necessarily belong to a user, through the "user_id" attribute, and may or may not belong to an investment portfolio through the "portfolio_id" attribute. The modeling also allows the addition of other types of investments, besides stocks and fixed income securities, if necessary in the future.
