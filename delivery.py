def delivery_cost(weight_kg: float, same_city: bool) -> float:

    if weight_kg <= 0:
        raise ValueError("Weight must be > 0")
    
    base_cost = 40.0
    extra_kg = int(weight_kg - 1)

    if extra_kg > 0:
        total_cost = base_cost + (extra_kg * 15)
    else:
        total_cost = base_cost

    if same_city:
        total_cost *= 0.8

    return round(total_cost, 2)