import random


def SamplingMean(num_samples=11, num_rocks=100, us=1.0, bs=3 / 8):
    """This code finds the sample mean of a random array of rock sizes that went through a sieve. Then finding
    the sampling mean and variance of the sample means.
    variables
    num_samples: the number of samples taken
    num_rocks: numer of rocks used in each sample
    us = upper limit seive or max size of rock used in each sample
    bs = bottom limit seive or max size of rock used in each sample"""

    passing_rocks = []  # Empty list for saving the rocks that are within range to pass the sieve
    sample_means = []  # Empty List to save each sample's mean value to find the mean of each sample

    for _ in range(num_samples):
        # generating rock size data. using a mean of 1.125 because an average pile of gravel is in the range of 0.25
        # to 2 inches in size standard deviation is 7/8. This generates a randomized list to be put through the sieve.
        rocks = [random.normalvariate(1.125, 7 / 8) for _ in range(num_rocks)]

        # count the passing rocks that are within the given range. problem 1 is for 1>r>3/8
        passing_rocks.append(sum([1 for rock in rocks if us > rock > bs]))

        # calculate the sample mean and sample variance, I used chatGPT to create the variance equation from
        # just the rock data that came though the seives
        sample_mean = sum(rock for rock in rocks if us > rock > bs) / sum(1 for rock in rocks if us > rock > bs)
        sample_variance = (sum((rock - sample_mean) ** 2 for rock in rocks if us > rock > bs) /
                           (sum(1 for rock in rocks if us > rock > bs) - 1)) if sum(
            1 for rock in rocks if us > rock > bs) > 1 else 0

        # store the results in a list
        sample_means.append(sample_mean)

        # print the results for each sample
        print(f"Sample {_ + 1}:")
        print(f"  Mean: {sample_mean:.2f}")
        print(f"  Variance: {sample_variance:.2f}")

    # calculate the mean and variance of the sample means data from the 11 samples
    sampling_mean = sum(sample_means) / num_samples
    sampling_variance = sum((sample_mean - sampling_mean) ** 2 for sample_mean in sample_means) / (num_samples - 1)

    # print the results for the sampling mean
    print("\nSampling Mean:")
    print(f"  Mean: {sampling_mean:.2f}")
    print(f"  Variance: {sampling_variance:.5f}")

    # Returned these for ease of use in problem 2
    return passing_rocks, sample_means, sampling_mean, sampling_variance


def main():
    """main function to solve the problem using function SamplingMean"""
    SamplingMean(11, 100, 1, 3 / 8)
    # This uses 11 samples, of 100 rocks each, with an upper seive of 1inch and lower seive of 3/8 inch


if __name__ == "__main__":
    main()
