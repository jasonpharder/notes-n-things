Feature: Navigating between screens

Scenario: Moving from the 'Home' screen to the 'Courses' screen
Given I launch the app
Then I should be on the Home screen
When I navigate to "Courses"
Then I should see a navigation bar titled "Courses"

Scenario: Moving from the 'Courses' screen to the 'Comp 1010' screen
Then I should see a navigation bar titled "Courses"
Then I wait a bit
When I touch the button marked "Comp 1010"
Then I should see a navigation bar titled "Comp 1010"

Scenario: Moving from the 'Comp 1010' screen to the 'Courses' screen
Then I should see a navigation bar titled "Comp 1010"
Then I wait a bit
Then I navigate back
Then I should see a navigation bar titled "Courses"

Scenario: Moving from the 'Courses' screen to the 'Home' screen
Then I should see a navigation bar titled "Courses"
Then I wait a bit
Then I navigate back
Then I should be on the Home screen

Scenario: Moving from the 'Home' screen to the 'Notes' screen
Then I should be on the Home screen
When I navigate to "Notes"
Then I should see a navigation bar titled "Notes"

Scenario: Moving from the 'Notes' screen to the 'Home' screen
Then I should see a navigation bar titled "Notes"
Then I wait a bit
Then I navigate back
Then I should be on the Home screen

Scenario: Moving from the 'Home' screen to the 'Login' screen
Then I should be on the Home screen
When I navigate to Login
Then I should see a navigation bar titled "Login"

Scenario: Moving from the 'Login' screen to the 'Home' screen
Then I should see a navigation bar titled "Login"
Then I wait a bit
Then I navigate back
Then I should be on the Home screen