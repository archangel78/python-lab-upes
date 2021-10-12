def check_baggage(baggage_weight):
    if(40>=baggage_weight>=0):
        return True
    return False
def check_immigration(expiry_year):
    if(2050>=expiry_year>=2030):
        return True
    return False
def check_security(noc_status):
    if(noc_status.upper()=="VALID"):
        return True
    return False
def traveler(traveler_id,traveler_name,baggage_weight,expiry_year,noc_status):
    print("Traveler id: "+str(traveler_id)+"\nTraveler name: "+str(traveler_name))
    if(check_baggage(baggage_weight) and check_immigration(expiry_year) and check_security(noc_status)):
        print("Allow traveler to fly")
    else:
        print("Detain traveler for re-checking")

traveler(1001, "Jim", 35, 2019, "valid")