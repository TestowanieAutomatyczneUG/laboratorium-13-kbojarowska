Feature: PasswordValidator

    Scenario: Password validator, empty string
        When password is empty string
        Then password is invalid

    Scenario: Password validator, 12Slowo_
        When password contains too little numbers
        Then password is invalid

    Scenario: Password validator, 123slowo_
        When password contains too little big letters
        Then password is invalid

    Scenario: Password validator, 123Slowo
        When password dont contain special character
        Then password is invalid

    Scenario: Password validator, 421S+
        When password has minimum number of characters
        Then password is valid

    Scenario: Password validator, ++++++++13171461UUCFSKBJS
        When password has many needed characters
        Then password is valid

    Scenario: Password validator, +_1S2l3O4W5o_+
        When password has many mixed needed characters
        Then password is valid

    Scenario: Password validator, 123Slowo_
        When password is good password
        Then password is valid
