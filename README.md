# Unplug Take Home Challenge

> Community Edition of the Hestia Calculations

Provides a self-hosted installation of everything you need to run calculations on your server or computer.

## Getting started

### Prerequisites

You will need to install the following softwares:
1. Docker
2. Python 3

### Install

Go to the root of the project and run these commands

- docker compose build
- docker compose up

### Notes

This api has created with following in mind:

- Added restaurant and menus to db.
- Deleting menu item means soft deletion.
- Updating menu item means changes in description, calorie etc. I've just made ranking attribute unique and didn't implement logic of changing all
the affected rows manipulation.
- API docs with swagger UI in: http://localhost:5000/docs/