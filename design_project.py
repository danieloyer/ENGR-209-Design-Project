# take user inputs for variables

basis = 1
X_list = [20, 30, 40, 50, 60, 70, 80, 85, 90, 95]
R_list = [6.0, 5.9, 5.8, 5.6, 5.2, 4.4, 3.6, 2.4, 1.2, 0.0]
P_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

ethylene_cost = 1.36  # 0.55
EO_price = 1.38      # 0.98
mm_ethylene = 0.02805
mm_EO = 0.04405

f = open("209_profit_values.txt", "r+")
for P in P_list:
    f.write("Profit values for " + str(P) + "% ethylene:" + "\n")
    for i in range(len(X_list)):

        X = X_list[i]
        R = R_list[i]
        B21 = (R*(0.01*X))/(R+1)
        E8 = (1/(0.01*P))-1-(0.5*B21+3*((X*0.01)/(R+1)))+(2*((X*0.01)/(R+1)))
        E9 = 2*(X*0.01)/(R+1)
        F9 = (79/21)*(0.5*B21+3*((X*0.01)/(R+1)))
        B9 = 0.4*(E9+F9) / E8

        E_need_to_buy = basis - (1-(0.01*X)-B9)

        cost = E_need_to_buy * mm_ethylene * ethylene_cost
        price = (R * (0.01 * X) / (R + 1)) * mm_EO * EO_price
        profit = price - cost
        f.write("$" + str(profit) + "\n")
    f.write("\n\n")

f.close()
