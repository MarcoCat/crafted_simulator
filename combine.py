import csv

conversion_factor = 1.32

weapon_lb_rates = [50.00, 51.00, 52.00, 53.00, 54.00, 55.00]
weapon_lb_probabilities = [12.50, 12.50, 25.00, 25.00, 12.50, 12.50]

weapon_lq_rates = [5.00, 6.00, 8.00, 9.00, 11.00, 12.00]
weapon_lq_probabilities = [12.50, 12.50, 25.00, 25.00, 12.50, 12.50]

weapon_lb_rates = [x / 100 for x in weapon_lb_rates]
weapon_lb_probabilities = [p / 100 for p in weapon_lb_probabilities]

weapon_lq_rates = [x / 100 for x in weapon_lq_rates]
weapon_lq_probabilities = [p / 100 for p in weapon_lq_probabilities]

weapon_lb_rates = [x * conversion_factor for x in weapon_lb_rates]

combined_probabilities = []

for lb_rate, lb_prob in zip(weapon_lb_rates, weapon_lb_probabilities):
    for lq_rate, lq_prob in zip(weapon_lq_rates, weapon_lq_probabilities):
        le_rate = lb_rate + lq_rate
        combined_prob = lb_prob * lq_prob
        combined_probabilities.append((round(le_rate, 4), round(combined_prob, 6)))

combined_probabilities.sort(key=lambda x: x[0])


with open("combined_probabilities.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["LE Rate", "Combined Probability"])
    for le_rate, combined_prob in combined_probabilities:
        csvwriter.writerow([le_rate, combined_prob])

print("Combined probabilities have been saved to 'combined_probabilities.csv'")
