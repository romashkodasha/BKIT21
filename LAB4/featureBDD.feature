Feature:
    Biquadratic equations

Scenario: first test
    Given coef 1.2, -1, -0.2
    When Something
    Then Result -1, 1

Scenario: second test
    Given coef 1, 5, -6
    When Something
    Then Result -1, 1

Scenario: third test
    Given coef 2, 0, 1
    When Something
    Then Result None