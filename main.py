def value_of_card(card):
    """Determine the scoring value of a card."""
    
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""

    one = value_of_card(card_one)
    two = value_of_card(card_two)

    if one > two:
        return card_one
    elif two > one:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card."""
    if card_one == 'A' or card_two == 'A':
        return 1
    else:
        val = value_of_card(card_one) + value_of_card(card_two)
        if val + 11 > 21:
            return 1
        else:
            return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""

    if (value_of_card(card_one) == 10 or value_of_card(card_two) == 10) and (card_one == 'A' or card_two == 'A'):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""

    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    
    one = value_of_card(card_one)
    two = value_of_card(card_two)

    if one + two == 9 or one + two == 10 or one + two == 11:
        return True
    else:
        return False
