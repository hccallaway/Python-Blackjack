# Python-Console-Poker

Created by Hadley Callaway as part of her 2020 Kleiner Perkins Engineering Fellow application.

## To play:

`python3 blackjack.py`

## The codebase:

### blackjack.py

This file creates a `Game` object and then calls that object's `play` method.

### card.py

This file represents a `Card` object. It contains two methods, `to_string` and `get_rank`.

### deck.py

This file represents a `Deck` object. It contains two methods, `get_cards` (used to populate the `Deck`) and `deal`.

### game.py

This file represents a `Game` object. It contains the methods `get_hand_str` (used to print out the player's hand), `deal_new_hands`, `dealer_play`, `determine_winner`, `end_game`, and `play`. `play` calls the other helper methods. It is in `play` that the blackjack game takes place.

### player.py

This file represents a `Player` object. It contains the methods `add_card`, `new_hand`, `get_hand`, and `get_total`.
