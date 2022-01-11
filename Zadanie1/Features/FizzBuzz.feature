Feature: FizzBuzz

  Scenario: FizzBuzz, number 5
    Given I play FizzBuzz
    When I get the number 5
    Then Its Buzz

  Scenario: FizzBuzz, number 3
    Given I play FizzBuzz
    When I get the number 3
    Then Its Fizz

  Scenario: FizzBuzz, number 15
    Given I play FizzBuzz
    When I get the number 15
    Then Its FizzBuzz

  Scenario: FizzBuzz, number 41
    Given I play FizzBuzz
    When I get the number 41
    Then Its 41

  Scenario: FizzBuzz, number 225
    Given I play FizzBuzz
    When I get the number 225
    Then Its FizzBuzz
