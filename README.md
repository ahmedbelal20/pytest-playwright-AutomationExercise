# AutomationExercise Test Suite

A Python-based automated test framework using **pytest** and **Playwright** to test the [AutomationExercise](https://automationexercise.com) demo website.  
This project was created for learning and portfolio purposes to demonstrate end-to-end web testing practices.

## Features

- UI test automation with Playwright
- Test execution and reporting via pytest
- End-to-end functional test coverage of AutomationExercise flows:
  - User login and signup
  - Product browsing and search
  - Shopping cart actions
  - Form validation

## Tech Stack

- [Python 3.13.3](https://www.python.org/)
- [pytest](https://docs.pytest.org/)
- [Playwright for Python](https://playwright.dev/python/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. Install dependencies.
   ```bash
   pip install pytest
   pip install pytest-playwright
   install playwright
   ```

## Project Structure
```markdown
├── tests/ # Test cases
│ ├── test_login.py
│ ├── test_cart.py
│ └── ...
├── README.md # Project documentation
└── LICENSE # License (MIT)
```

## Notes

- This project is for **learning and portfolio purposes** only.  
- The target website ([AutomationExercise](https://automationexercise.com)) is a public demo site for practicing test automation.  

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
