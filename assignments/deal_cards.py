import requests

BASE = "https://deckofcardsapi.com/api/deck"


def get_json(url: str) -> dict:
    """Helper: makes a GET request and returns JSON (dict)."""
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


# ---------- DECK ACTIONS ----------

def new_shuffled_deck(deck_count: int = 1) -> dict:
    url = f"{BASE}/new/shuffle/?deck_count={deck_count}"
    return get_json(url)


def reshuffle_deck(deck_id: str, remaining_only: bool = False) -> dict:
    extra = "?remaining=true" if remaining_only else ""
    url = f"{BASE}/{deck_id}/shuffle/{extra}"
    return get_json(url)


def brand_new_deck(jokers_enabled: bool = False) -> dict:
    extra = "?jokers_enabled=true" if jokers_enabled else ""
    url = f"{BASE}/new/{extra}"
    return get_json(url)


def partial_deck(card_codes: list[str]) -> dict:
    # Creates + shuffles a deck with only those cards
    cards = ",".join(card_codes)
    url = f"{BASE}/new/shuffle/?cards={cards}"
    return get_json(url)


def draw_cards(deck_id: str, count: int = 1) -> dict:
    url = f"{BASE}/{deck_id}/draw/?count={count}"
    return get_json(url)


# ---------- PILES ----------

def add_to_pile(deck_id: str, pile_name: str, card_codes: list[str]) -> dict:
    cards = ",".join(card_codes)
    url = f"{BASE}/{deck_id}/pile/{pile_name}/add/?cards={cards}"
    return get_json(url)


def list_pile(deck_id: str, pile_name: str) -> dict:
    url = f"{BASE}/{deck_id}/pile/{pile_name}/list/"
    return get_json(url)


def shuffle_pile(deck_id: str, pile_name: str) -> dict:
    url = f"{BASE}/{deck_id}/pile/{pile_name}/shuffle/"
    return get_json(url)


def draw_from_pile(deck_id: str, pile_name: str, count: int = 1, mode: str = "top") -> dict:
    # mode: "top", "bottom", "random"
    if mode == "top":
        url = f"{BASE}/{deck_id}/pile/{pile_name}/draw/?count={count}"
    elif mode == "bottom":
        url = f"{BASE}/{deck_id}/pile/{pile_name}/draw/bottom/?count={count}"
    elif mode == "random":
        url = f"{BASE}/{deck_id}/pile/{pile_name}/draw/random/?count={count}"
    else:
        raise ValueError("mode must be: top, bottom, random")

    return get_json(url)


def return_from_pile(deck_id: str, pile_name: str, card_codes: list[str] | None = None) -> dict:
    # If card_codes is None -> returns all cards from that pile
    if card_codes:
        cards = ",".join(card_codes)
        url = f"{BASE}/{deck_id}/pile/{pile_name}/return/?cards={cards}"
    else:
        url = f"{BASE}/{deck_id}/pile/{pile_name}/return/"
    return get_json(url)


# ---------- DEMO SCRIPT ----------

def print_cards(title: str, cards: list[dict]):
    print(title)
    for c in cards:
        print(f" - {c['value']} of {c['suit']}  (code={c['code']})")
    print()


def main():
    # 1) Create shuffled deck
    deck = new_shuffled_deck()
    deck_id = deck["deck_id"]
    print("Created deck:", deck_id, "| remaining:", deck["remaining"])

    # 2) Draw 4 cards (we will deal 2 to each player)
    drawn = draw_cards(deck_id, 4)
    cards = drawn["cards"]
    print_cards("Drawn cards:", cards)

    # Split into players
    p1_codes = [cards[0]["code"], cards[1]["code"]]
    p2_codes = [cards[2]["code"], cards[3]["code"]]

    # 3) Add to piles (player1/player2)
    add_to_pile(deck_id, "player1", p1_codes)
    add_to_pile(deck_id, "player2", p2_codes)

    # 4) List piles
    p1 = list_pile(deck_id, "player1")
    p2 = list_pile(deck_id, "player2")
    print("Piles listed. Remaining in deck:", p1["remaining"])

    # Print what’s inside each pile
    print_cards("Player1 pile:", p1["piles"]["player1"]["cards"])
    print_cards("Player2 pile:", p2["piles"]["player2"]["cards"])

    # 5) Shuffle a pile
    shuffle_pile(deck_id, "player1")
    print("Shuffled player1 pile.\n")

    # 6) Draw from a pile (random)
    from_pile = draw_from_pile(deck_id, "player2", count=1, mode="random")
    print_cards("Drew 1 card from player2 pile:", from_pile["cards"])

    # 7) Return cards from pile back to deck (return all)
    ret = return_from_pile(deck_id, "player1")
    print("Returned player1 pile to deck. Deck remaining:", ret["remaining"])

    # 8) Reshuffle deck (remaining only)
    resh = reshuffle_deck(deck_id, remaining_only=True)
    print("Reshuffled remaining cards in deck:", resh["deck_id"], "| remaining:", resh["remaining"])

    # 9) Brand new deck (with jokers)
    fresh = brand_new_deck(jokers_enabled=True)
    print("\nBrand new deck with jokers:", fresh["deck_id"], "| remaining:", fresh["remaining"])

    # 10) Partial deck
    part = partial_deck(["AS", "KH", "8C", "2D"])
    print("Partial deck created:", part["deck_id"], "| remaining:", part["remaining"])

    # Back image
    print("\nBack of card image:")
    print("https://deckofcardsapi.com/static/img/back.png")


if __name__ == "__main__":
    main()