Feature: Login SwagLabs

	Scenario: User can login with a valid Username and Password
		Given I am on login page
		When I put my login in the login field and password in the password field
		Then I an on the product page


	Scenario: User can not login with an invalid Username and Password
   		Given I am on login page
   		When I put wrong login in the login field or wrong password in the password field
   		Then I see a notification that login or password is wrong


   Scenario: User can logout
   		Given I am on product page
   		When I press logout
   		Then I an on login page

       Examples:
         | username | password | message |
         | 'fake'    | 'secret_sauce' | 'Username and password do not match any user in this service'
         | 'standard_user' | 'fake'   | 'Username and password do not match any user in this service'
         | ''              | 'secret_sauce'       | 'Username is required'
         | 'standard_user' | ''                   | 'Password is required'