# Gilded Rose Refactoring Kata

This repository contains my solution to the Gilded Rose Refactoring Challenge.

## Approach

I completed the challenge in the following steps:

1. Preserved the original code in the initial commit.
2. Added unit tests for normal items, Aged Brie, Sulfuras, and Backstage passes.
3. Refactored `update_quality()` into smaller helper methods while keeping the existing behavior unchanged.
4. Added support and tests for Conjured items.

The refactoring removes deeply nested conditions, replaces repeated strings with constants, and centralizes the quality limits between 0 and 50. The `Item` class was not modified, as required.

## Conjured Items

Conjured items degrade twice as fast as normal items:

* Before expiration: quality decreases by 2.
* After expiration: quality decreases by 4.

## Design Decision

I used small helper methods instead of a full Strategy Pattern because the current number of item types is limited. This keeps the solution simple and readable. A Strategy Pattern could be introduced later if more item categories are added.

## Running the Tests

```powershell
python -m unittest test_gilded_rose -v
```

The project contains 19 unit tests covering all item types, expiration behavior, and quality boundaries.

Expected result:

```text
Ran 19 tests
OK
```

## Running the Text Fixture

```powershell
python texttest_fixture.py 5
```

The text fixture provides a readable inventory simulation across multiple days.
