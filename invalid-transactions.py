class Solution:
    def bigFunction(self, transactions):
        name_array, time_array, amount_array, location_array = [], [], [] ,[]
        bad_transactions = {}

        for i in range(len(transactions)):
            name_array.append(transactions[i].split(",")[0])
            time_array.append(transactions[i].split(",")[1])
            amount_array.append(transactions[i].split(",")[2])
            location_array.append(transactions[i].split(",")[3])

        for i in range(len(transactions)):
          if transactions[i] in bad_transactions: continue
          if int(amount_array[i]) > 1000:
              bad_transactions[i] = transactions[i]
          for j in range(i+1, len(transactions)):
              if name_array[i] == name_array[j]:
                # CHECK TIME
                  if abs(int(time_array[i]) - int(time_array[j])) <= 60:
                    # CHECK CITY
                    if  location_array[i] != location_array[j]:
                        bad_transactions[i] = transactions[i]
                        bad_transactions[j] = transactions[j]

        return list(bad_transactions.values())

