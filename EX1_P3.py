def func(x, y, z):
    """ This function defines the function equation y''-y=x into first order ODE's x being the independent variable,
    y being the dependent variable, and z being the derivative of y with respect to x or z = dy/dx"""
    return x * y - z


def improved_euler_method(x0, y0, z0, h, target_x):
    """ Function to utilize the Euler Method to get the approximate solution of an Ordinary Differential Equation or ODE
     variables:
     x0 = 0 the reference point, y0 being the y value at x0 = 0 and z0 being the y' value at x = 0
     target_x = x value we want to find the solution of
     y_temp = temporary y value in the iterative process
     z_temp =temporary z value in the iterative process
     h = step size or interval, smaller = more accurate"""
    x, y, z = x0, y0, z0   # stating initial values
    while x < target_x:    # Using the given equations for improved euler, found in book
        f = func(x, y, z)
        y_temp = y + h * z
        z_temp = z + h * f
        y = y + h * (z + z_temp) / 2
        z = z + h * (f + func(x + h, y_temp, z_temp)) / 2
        x += h
    return y, z


def runge_kutta_method(x0, y0, z0, h, target_x):
    """Function to utilize the Runge-Kutta Method to get the approximate solution of an ODE
    New variables:
    k =  points within a step contributing to the weighted average in the calculations for y and z or y' """
    x, y, z = x0, y0, z0  # stating initial values
    while x < target_x:   # Using equations for this numerical method, found in book
        k1_y = h * z
        k1_z = h * func(x, y, z)

        k2_y = h * (z + k1_z / 2)
        k2_z = h * func(x + h / 2, y + k1_y / 2, z + k1_z / 2)

        k3_y = h * (z + k2_z / 2)
        k3_z = h * func(x + h / 2, y + k2_y / 2, z + k2_z / 2)

        k4_y = h * (z + k3_z)
        k4_z = h * func(x + h, y + k3_y, z + k3_z)

        y = y + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        z = z + (k1_z + 2 * k2_z + 2 * k3_z + k4_z) / 6

        x += h
    return y, z


def main():
    """Main Function to solve the problem, requests the y and y' aka z value at x = 0, then the step size.
    Input a target x value to solve for y and y' values at that x value using both methods."""
    print("For the initial value problem y’’- y = x")
    y0 = float(input("Enter the value of y at x=0: "))
    z0 = float(input("Enter the value of y’ at x=0: "))
    h = float(input("Enter the step size for the numerical solution: "))

    while True:
        target_x = float(input("At what value of x do you want to know y and y’? "))

        # Improved Euler Method
        y_ie, z_ie = improved_euler_method(0, y0, z0, h, target_x)  # y_ie is y(improved euler)
        print(f"At x={target_x:.3f}")
        print(f"For the Improved Euler method: y={y_ie:.3f}, and y’={z_ie:.3f}")

        # Runge-Kutta Method
        y_rk, z_rk = runge_kutta_method(0, y0, z0, h, target_x)   # y_rk is y(runge kutta)
        print(f"For the Runge-Kutta method: y={y_rk:.3f}, and y’={z_rk:.3f}")

        choice = input("Do you want to compute at a different x? (Y/N): ")
        if choice.upper() != 'Y':    # to find the y and y' values at another x without having to redo all inputs
            break


if __name__ == "__main__":
    main()
