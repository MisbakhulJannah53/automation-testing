Feature: Authentication
    As u user 
    I want to login jubelio dashboard

    Scenario: Successful login with correct email and password
        Given I am on the login page
        When I enter my correct email and password ("qa.rakamin.jubelio@gmail.com" and "Jubelio123!")
        And I click on the login button
        Then I should be redirected to the dashboard