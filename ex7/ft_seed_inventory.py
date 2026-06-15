def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if seed_type == "tomato":
        print("Tomato seeds:", quantity, unit, "available")
    elif seed_type == "carrot":
        print("Carrot seeds:", quantity, unit, "total")
    elif seed_type == "lettuce":
        print("Lettuce seeds:", "covers", quantity, "square meters")
    else:
        print("Unknown unit")
