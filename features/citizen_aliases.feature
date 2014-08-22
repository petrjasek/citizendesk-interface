Feature: citizen aliases

scenario: simple query request
    Given one alias
     When we ask for aliases
     Then we get the alias in the collection

scenario: simple specific request
    Given one alias
     When we ask for that alias
     Then we get the alias

scenario: embedded lists
    Given a list
      And an alias referring to it
     When we ask for the alias with the embedded list
     Then we get tags in the alias
      and we get the alias with the embedded list
