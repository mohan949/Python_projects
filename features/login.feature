Feature: User Login
  As a registered user
  I want to log in
  So that I can access the dashboard

  Scenario: Successful login with CSS validation
    Given I open the login page
    When I enter valid credentials
    Then the login label should have correct CSS properties
    And I click the login button
    Then I should see the dashboard page