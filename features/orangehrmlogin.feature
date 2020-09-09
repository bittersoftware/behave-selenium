Feature: OrangeHRM Login

    Test Login
    Scenario: Login to OrangeHRM with valid parameters
      Given I launch Chrome Browser
      When I open OrangeHRM Home Page
      And Enter user name "admin" and password "admin123"
      And Click Login button
      Then User must successfully login to the Dashboard page

    
    Scenario Outline: Login to OrangeHRM with multiple parameters
      Given I launch Chrome Browser
      When I open OrangeHRM Home Page
      And Enter user name "<username>" and password "<password>"
      And Click Login button
      Then User must successfully login to the Dashboard page if credentials are "<valid>" 

      Examples:
          | username | password | valid |
          | admin    | admin123 | True  |
          | admin123 | admin    | False |
          | adminxyz | admin123 | False |
          | admin    | adminxyz | False |