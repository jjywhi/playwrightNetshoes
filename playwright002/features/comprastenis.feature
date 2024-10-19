Feature: Search and buy a product on Netshoes

  Scenario: Search for a Nike product and buy it
    Given I open the Netshoes homepage
    When I search for "Nike"
    And I click on the product with text "Tênis Nike Downshifter 13 Masculino"
    And I select the size
    And I click the buy button
    Then I click on the home icon
    And I hover over the cart icon