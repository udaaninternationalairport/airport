import json

def check_in_passenger(passenger_id, flight_id):
    print(f"Checking in passenger {passenger_id} for flight {flight_id}")
    # Simulate check-in process
    return {"status": "success", "boarding_pass": f"{passenger_id}-{flight_id}"}

if __name__ == "__main__":
    passenger_id = "P12345"
    flight_id = "AI2024"
    result = check_in_passenger(passenger_id, flight_id)
    print(json.dumps(result, indent=4))