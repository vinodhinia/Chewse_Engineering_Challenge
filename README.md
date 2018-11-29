# Chewse_Engineering_Challenge
In our product, we’ve exposed a way for users to plan a meal by specifying the total number of portions ( people ) and a certain ratio of meal items they would like the meal to be composed of.

For example, for a meal of 100 people we would like ⅗ meat burgers, ⅕ veggie burgers, ⅕ gluten free chicken.

This feature then determines how many portions should be allocated for each item. In the example above, this would be 60 meat burgers, 20 veggie burgers, 20 gluten free chicken.

Ratio Problem


Write a function that takes in 2 arguments:

A dictionary/map where the keys are numeric identifiers for a certain food item, and the values are the ratio of that item desired

An integer indicating how many portions the meal should serve

For Example:

{1: 1, 2: 1, 3: 1}, 120 -- means that item IDs 1, 2, 3 they each will have equal portions distributed ( ⅓ each ), and we are serving 120 portions (people)

Assigns all portions

Only assigns integers for portion counts

Chooses the largest remainder for allocating non-integer portion counts, If there is no largest remainder, the item with the smallest numeric ID should be chosen (distributing portions from lowest ID to largest)

Example:

{1: 2, 2: 3}, 3 -- {1: 1, 2: 2} Item ID 2 gets the extra portio ​because it has the largest remainder


{1: 1, 2: 1, 3: 1}, 11 — {1: 4, 2: 4, 3: 3} Item ID 1 and 2 gets the extra portions​because they have lower ID than item 3
Please write tests to go with your solution

Test Cases and Results

{}, 1 — {}

{1: 1}, 2 — {1: 2}

{1: 1}, 0 — {1: 0}

{1: 1, 2: 1, 3: 1}, 11 — {1: 4, 2: 4, 3: 3}

{1: 10, 2: 0}, 2 -- {1: 2, 2: 0}

{1: 2, 2: 4, 3: 4, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2}, 12 ---

{1: 1, 2: 3, 3: 3, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1 }

{1: 1, 2: 2, 3: 2, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}, 12 —

{1: 1, 2: 3, 3: 3, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}
