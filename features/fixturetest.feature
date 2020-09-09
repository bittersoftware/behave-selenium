Feature: Test Fixtures with environment.py

    @setup_scenario
    @teardown_scenario
    Scenario: Login
      When Enter user name "admin" and password "admin123"
      And Click Login button
      Then User must successfully login to the Dashboard page