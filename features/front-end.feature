@requires-live-http
Feature: The home page should be available and should show a salutation

    Scenario: Home page object returns a valid salutation
        When I visit the home page
        Then it is avaiable
        And it provides a salutation document
