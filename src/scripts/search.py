from random import choice


def search(Client) -> None:
    Client.send_message("pls search")

    latest_message = Client.retreive_message("pls search")

    if "Where do you want to search" not in latest_message["content"]:
        latest_message = Client.fallback_retreive_message("pls crime")

    custom_id = None

    for option in latest_message["components"][0]["components"]:
        if option["label"] == "street":
            # Gives `Golden Phalic Object` / `Rare Pepe`.
            custom_id = option["custom_id"]
            break
        elif option["label"] == "dresser":
            # Gives `Bank note` / `Normie Box` / `Apple`.
            custom_id = option["custom_id"]
            break
        elif option["label"] == "mailbox":
            # Gives `Normie Box` / `Bank note`.
            custom_id = option["custom_id"]
            break
        elif option["label"] == "bushes":
            # Gives ``Normie Box`.
            custom_id = option["custom_id"]
            break
        elif option["label"] == "bank":
            # Gives `Bank note`.
            custom_id = option["custom_id"]
            break
        elif option["label"] == "laundromat":
            # Gives `Tidepod`.
            custom_id = option["custom_id"]
            break
        elif option["label"] == "hospital":
            # Gives `Life Saver` / `Apple`.
            custom_id = option["custom_id"]
            break
        elif option["label"] == "laundromat":
            # Gives `Tidepod`.
            custom_id = option["custom_id"]
            break

    Client.interact_button(
        "pls search",
        choice(latest_message["components"][0]["components"])["custom_id"]
        if custom_id is None
        else custom_id,
        latest_message,
    )

    latest_message = Client.retreive_message(
        "pls search", old_latest_message=latest_message
    )

    latest_message["embeds"][0]["description"] = (
        latest_message["embeds"][0]["description"]
        .replace("! <:horseshoe:813911522975678476>", "")
        .replace(" <:horseshoe:813911522975678476>", "")
    )

    try:
        coins = int(
            "".join(
                filter(
                    str.isdigit,
                    latest_message["embeds"][0]["description"]
                    .split("\n")[0]
                    .split("https://")[0],
                )
            )
        )
    except Exception:
        coins = 0

    try:
        item = (
            latest_message["embeds"][0]["description"].split("**")[-2]
            if latest_message["embeds"][0]["description"].count("**") == 2
            else "no items"
        )
    except Exception:
        item = "no items"

    Client.log(
        "DEBUG",
        f"Received ⏣ {coins} coin{'' if coins == 1 else 's'} &{' an' if item[0] in ['a', 'e', 'i', 'o', 'u'] else '' if item == 'no items' else ' a'} {item} from the `pls search` command.",
    )
    Client._update_coins("pls search", coins)
    Client._update_items("pls search", item)