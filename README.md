# Gilded Rose Refactoring Kata

## Approach

This repo's commit history shows the process step by step:

1. **Initial commit** – the original, unmodified starting code (buggy/unstructured,
   as given).
2. **Characterization tests** – before touching any logic, I wrote unit tests
   against the *original* code to lock in its existing (intended) behavior for
   every item type: normal items, Aged Brie, Sulfuras, and Backstage Passes.
   These passed against the original code, confirming the tests describe the
   correct behavior and give a safety net for refactoring.
3. **Refactor** – rewrote `update_quality()` using small, named helper methods
   instead of deeply nested `if` statements, centralized the "quality is
   clamped between 0 and 50" rule into two helper methods, and replaced
   negated string comparisons (`!=`) with direct, positive checks. All 16
   existing tests still passed unchanged after this step, confirming no
   behavior was altered — this was a pure refactor.
4. **New feature: Conjured items** – added support for items whose name
   starts with `"Conjured"`, which degrade in quality twice as fast as
   normal items (and therefore four times as fast once the sell-by date has
   passed, consistent with the existing "twice as fast after expiry" rule).
   Added 3 new tests covering this.

`Item` was never modified, as required.

## Design decision

I kept the design intentionally simple (helper methods + a per-item
dispatch) rather than introducing a full Strategy Pattern with one class
per item type. With only 5 item types and no indication that many more are
coming, a small set of clear functions is easier to read and review than
several extra classes. If this system were expected to grow with many more
item types over time, I would move to a Strategy Pattern (one updater class
per item type, selected via a factory) to keep `update_quality()` itself
untouched when adding new types — I'm happy to walk through that
alternative as well.

## Running tests

```bash
python3 -m unittest test_gilded_rose -v
```

## Running the text-based fixture

```bash
python3 texttest_fixture.py <days>
```
