
def count_batteries_by_health(present_capacities):
  
  battries_count = {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }                #Dictionary to store the count of the batteries according to their health
  
  for capacity in present_capacities:
    rated_capacity = 120 # given common rated capacity for all batteries
    soh = 100 * (capacity/rated_capacity)

    if soh > 80:
      battries_count["healthy"] += 1
    elif 63 <= soh <=80:
      battries_count["exchange"] += 1
    else:
      battries_count["failed"] += 1

  return battries_count 

def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")

  # Test Case 1 : Given Test Case 
  present_capacities = [115, 118, 80, 95, 91, 72]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting case 1 :)")

  #Test Case 2 : All batteries are in failed state
  present_capacities = [75, 69, 64, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 4)
  print("Done counting case 2 :)")

  #Test Case 3 : Testing boundary conditions 
  present_capacities = [96,76,97,75]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 1)
  assert(counts["exchange"] == 2)
  assert(counts["failed"] == 1)
  print("Done counting case 3 :)")

if __name__ == '__main__':
  test_bucketing_by_health()
