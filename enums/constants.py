from enum import Enum

class Url(Enum):
    HOME = "https://automationexercise.com/"
    LOGIN = "https://automationexercise.com/login"
    SIGNUP = "https://automationexercise.com/signup"
    ACCOUNT_CREATED = "https://automationexercise.com/account_created"
    DELETE_ACCOUNT = "https://automationexercise.com/delete_account"

class Text(Enum):
    BUTTON_SIGNUP = " Signup / Login"

class Title(Enum):
    HOME = "Automation Exercise"
    LOGIN = "Automation Exercise - Signup / Login"
    SIGNUP = "Automation Exercise - Signup"
    ACCOUNT_CREATED = "Automation Exercise - Account Created"
    DELETE_ACCOUNT = "Automation Exercise - Account Created"
    