Feature: bot testing
Scenario: generating buying message
  Given There is a painting named "Jolyne Cujoh"
  When The painting is bought
  Then Send the message: You have bought "Jolyne Cujoh".
Scenario: generating deleting message
  Given There is a painting named "Jolyne Cujoh"
  When The painting is deleted
  Then Send the message: "Jolyne Cujoh" has been deleted.
Scenario: chat testing
  When The message is got: Hello!
  Then Send the message: Hello there! How are you?
  When The message is got: I am fine, thanks!
  Then Send the message: What a nice day to see you here!
  When The message is got: You too!
  Then Send the message: :^)
