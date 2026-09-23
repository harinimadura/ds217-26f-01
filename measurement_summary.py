measurements = [18, 21, 24, 19]
review_threshold_text = "20"

# 1. Convert `review_threshold_text` to an integer named review_threshold;
review_threshold = int(review_threshold_text)

# 2. start total and review_count at zero;
total = 0
review_count = 0
count = 0

# 3. use one direct for loop written as for measurement in measurements: to visit every value;
for measurement in measurements:
    count = count + 1
# 4. add each value to total;
    total = total + measurement
# 5. use if and else so a value at or above review_threshold is labeled review, while a lower value is labeled within range;
    if total >= review_threshold:
        print("Measurement: ", measurement, "review")
# 6. add one to review_count only for a value labeled review;
        review_count = review_count + 1
    else:
        print("Measurement: ", measurement, "within range")
print("Count: ", count)
print("Total: ", total)
# 8. after the loop, calculate the mean using the actual list length; and
measurement_mean = total/count
# 9. print the summary labels shown below using print() with comma-separated values. The supplied data gives a mean of 20.5; no rounding or text formatting is needed.
print("Mean: ", measurement_mean)
print("Review count:", review_count)