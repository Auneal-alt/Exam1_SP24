from EX1_P1 import SamplingMean
import math
from math import pi, sqrt
from SmaySimpsonIntegration import Simpson


# this chunk of code was heavily assisted by chatgpt,(dof calcs and its naming of variables)
#  Sample[1] means list of rock sizes, Sample[2] are the sample means, and Sample[3] are the sample variances
def t_test(sampleA, sampleB, alpha=0.05):
    """ Function calculate the degrees of freedom, standard deviation between the two sample's Mean values or
    sqrt(variance) then calculates teh t-statistic value which will be compared to the critical value to test
    the significance of their differences."""
    # Calculating the required degrees of freedom by summing the dof for A and B based on the number of observations
    dof_A = len(sampleA[1]) - 1
    dof_B = len(sampleB[1]) - 1
    dof_total = dof_A + dof_B  # Degrees of Freedom

    # Standard deviation(sigma) between the means for sample A and B
    sigma = sqrt((sampleA[3] / len(sampleA[1])) + (sampleB[3] / len(sampleB[1])))

    # Calculate the t-statistic
    t_statistic = (sampleA[2] - sampleB[2]) / sigma

    # Get the critical value from t-distribution code(Smays code that he helped me with)
    critical_value = FZ((dof_total, 1 - alpha))

    # Compare t-statistic with critical value
    if t_statistic < -critical_value:
        result = "Supplier B has a statistically significant smaller gravel size."
    else:
        result = "There is no statistically significant difference."

    return result


# Below is Primarily Smays code for t-Distribution
def FZ(args):
    """Function FZ computes the area below the t-distribution"""
    m, u = args
    k_m = km(m)

    def tPDF(args):
        x, m = args
        base = 1 + (x ** 2) / m
        epnt = -(m + 1) / 2
        return base ** epnt

    I = Simpson(tPDF, m, u - 100.0 * abs(u), u, 100000)

    return k_m * I


def gamma(alpha):
    """ Gamma Function computes the function for a positive m"""

    if alpha % 1 == 0:
        g = 1
        for i in range(1, int(alpha)):
            g *= i
        return g

    def fn(args):
        t, a = args
        return math.exp(-t) * math.pow(t, a - 1)

    g = Simpson(fn, alpha, 0, 50, 100000)
    return g


def km(m):
    """ Function to find Km constant as a function of gamma and degrees of freedom"""

    k_m = gamma((0.5 * m) + 0.5) / ((sqrt(m * pi)) * gamma(0.5 * m))
    return k_m


def main():
    """Main Function uses a combination of 3 files(EX1_P2, Smayt-distribution, and SmaySimpsonInt)
    to collect and calculate the samples and there means when given different mesh sizes. Then with those means
    calculating the statistical and critical values to find whether the differrence is statistically significant"""
    # SampleA using a upper seive limit of 1
    SampleA = SamplingMean(11, 100, 1, 3 / 8)

    # SampleB using an upper Seive limit of 7/8
    SampleB = SamplingMean(11, 100, 7/8, 3 / 8)
    print("Sample A Mean:", SampleA[2])
    print("Sample B Mean:", SampleB[2])

    # Perform one-sided t-test
    result = t_test(SampleA, SampleB)

    # Print the result of the t-test
    print(result)


if __name__ == "__main__":
    main()
