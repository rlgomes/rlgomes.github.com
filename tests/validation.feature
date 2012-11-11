Feature: Personal Blog Content Validation

  Scenario Outline: Validate content on <link> page
   Given I am at main blog site
    Then I should see the title Rodney's Corner
    When I click on <link>
    Then I should see the headers <headers>
    When I click back
    Then I should see the title Rodney's Corner
    Then I should see everything spelled correctly

Examples:
  |  link   | headers |
  |  Blog   | Blog, Recent Posts  |
  | Archive | Archive |
  |  About  | About, Rodney Lopes Gomes |

