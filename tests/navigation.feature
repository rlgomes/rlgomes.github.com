Feature: Personal Blog

  Scenario: Visit the main page
   Given I am at main blog site
    Then I should see the title Rodney's Corner
     And I should see the links Blog, Archive, About
     And I should see the headers Blog, Recent Posts, Coding

  Scenario Outline: Navigate from the main page
   Given I am at main blog site
    Then I should see the title Rodney's Corner
   When I click on <link>
    Then I should see the links <links_to_validate>
   When I click back
    Then I should see the title Rodney's Corner

Examples:
  | link    |  links_to_validate   |
  |  Blog   | Blog, Archive, About |
  | Archive | Blog, Archive, About |
  |  About  | Blog, Archive, About |
