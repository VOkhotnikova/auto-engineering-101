Feature: GoogleSearch

	Scenario: Entering a search displays a result page
		Given I am on google search
		When I search 'puppies'
		Then I see the 'puppies' result page