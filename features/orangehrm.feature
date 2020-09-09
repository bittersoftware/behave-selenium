Feature: OrangeHRM Logo

    Assert logo is displayed
    Scenario: Logo is present in Home Page
      Given launch chrome webrowser
      When open OrangeHRM homepage
      Then verify that logo is present in the page
      And close browser

    

