Feature: Personal Blog Navigation

  Scenario: Visit the main page
   Given I am at main blog site
    Then I should see the title Rodney's Corner
     And I should see the links Blog, Archive, About
     And I should see the headers Blog, Recent Posts 

  Scenario Outline: Navigate to <link>
   Given I am at main blog site
    Then I should see the title Rodney's Corner
    When I click on <link>
    Then I should see the links <links>
    When I click back
    Then I should see the title Rodney's Corner

Examples:
  |  link   |  links  |
  |  Blog   | Blog, Archive, About, Jekyll, Bootstrap |
  | Archive | Blog, Archive, About, Jekyll, Bootstrap |
  |  About  | Blog, Archive, About, Jekyll, Bootstrap, email, AIM, YIM, Gtalk |
