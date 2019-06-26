Feature: Assurity automated Test sample using Python Behave

  Scenario: Name should be Carbon credits
    Given an api url with valid response
    When user sends request to get response
    Then it should display Name with value Carbon credits

  Scenario: CanRelist should be True
    Given an api url with valid response
    When user sends request to get response
    Then it should display CanRelist with boolean value True

  Scenario: Gallery Promotion should have description of 2x larger image
    Given an api url with valid response
    When user sends request to get response
    Then Galery promotion should display description with value 2x larger image
    