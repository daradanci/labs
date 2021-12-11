Feature: just simple reading
  Scenario: English reader tries to read English book
    Given There is an English book named "Harry Potter and the Philosopher's Stone"
    Given There is an English reader
    When The reader tries to read the book
    Then The next result is expected: "I have read The book named <<Harry Potter and the Philosopher's Stone>> and enjoyed it."
  Scenario: Russian reader tries to read Russian book
    Given There is a Russian book named "Таня Гроттер и волшебный контрабас"
    Given There is a Russian reader
    When The reader tries to read the book
    Then The next result is expected: "Книга под названием <<Таня Гроттер и волшебный контрабас>> мне очень понравилась!"
  Scenario: English reader tries to read Russian book
    Given There is a Russian book named "Таня Гроттер и волшебный контрабас"
    Given There is an English reader
    When The reader tries to read the book
    Then The next result is expected: "I don't understand <<Книга под названием <<Таня Гроттер и волшебный контрабас>>>> and I hate it."
  Scenario: Russian reader tries to read English book
    Given There is an English book named "Harry Potter and the Philosopher's Stone"
    Given There is a Russian reader
    When The reader tries to read the book
    Then The next result is expected: "Я не понимаю <<The book named <<Harry Potter and the Philosopher's Stone>>>>, что за ерунда?"