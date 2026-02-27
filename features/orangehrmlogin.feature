Feature:OrangeHRM Login
 Scenario: Login to orangehrm with valid parameters
    Given launch chrome browser
    When open orange hrm homepage
    And Enter usernaem "admin" and password "admin123"
    And click on login button
    Then user must successfully login to the Dasboard Page
    And close browser