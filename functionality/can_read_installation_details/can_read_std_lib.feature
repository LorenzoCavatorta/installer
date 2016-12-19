Feature: installer can read a program name from keyboard and install it

  Scenario: can install a program form standard library
	 GIVEN that I run the installer
	 WHEN I enter the name of a program that is in the std library
	 THEN installer installs that program

  Scenario: can store information to install a program form standard library
	 GIVEN that I run the installer
	 WHEN I enter the name of a program that is in the std library
	 THEN installer store information to install that program in the future