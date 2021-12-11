Feature: reading the translated books
  Scenario: Translate the book to Russian
    Given There is an English book named "Harry Potter and the Philosopher's Stone"
    When The book is translated
    Then The next result is expected: "Перевод: The book named <<Harry Potter and the Philosopher's Stone>> - теперь доступно на русском языке!"
  Scenario: Russian reader tries to read the book translated
    Given There is an English book named "Harry Potter and the Philosopher's Stone"
    Given There is a Russian reader
    When The book is translated
    When The reader tries to read the book
    Then The next result is expected: "Книга под названием <<Перевод: The book named <<Harry Potter and the Philosopher's Stone>> - теперь доступно на русском языке!>> мне очень понравилась!"
  Scenario: English reader tries to read the book translated to Russian
    Given There is an English book named "Harry Potter and the Philosopher's Stone"
    Given There is an English reader
    When The book is translated
    When The reader tries to read the book
    Then The next result is expected: "I don't understand <<Книга под названием <<Перевод: The book named <<Harry Potter and the Philosopher's Stone>> - теперь доступно на русском языке!>>>> and I hate it."