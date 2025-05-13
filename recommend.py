from restaurant_data import restaurants

def recommend_restaurant(location, cuisine, budget):
    try:
        budget = int(budget)
    except ValueError:
        return {"error": "Invalid budget format."}

    matches = [
        r for r in restaurants
        if r["location"].lower() == location.lower()
        and r["cuisine"].lower() == cuisine.lower()
        and r["budget"] <= budget
    ]

    if matches:
        return {
            "count": len(matches),
            "results": matches
        }
    else:
        return {
            "count": 0,
            "message": "No restaurants found matching your criteria."
        }
