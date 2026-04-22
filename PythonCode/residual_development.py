import pandas as pd
import matplotlib.pyplot as plt

# Loading the different datasets
df1 = pd.read_csv("Data/residual_data/coefficient.csv", sep=r"\s+", skiprows = 12)
df2 = pd.read_csv("Data/residual_data/coefficient_200.csv", sep=r"\s+", skiprows = 12)
df3 = pd.read_csv("Data/residual_data/coefficient_250.csv", sep=r"\s+", skiprows = 12)
df4 = pd.read_csv("Data/residual_data/coefficient_275.csv", sep=r"\s+")

# Slå sammen (append) df1 til df2
ny_df3 = pd.concat([df3, df4], ignore_index=True)
# Lagre resultatet til en ny eller eksisterende fil
ny_df3.to_csv('df3.csv', index=False)



# Coarse mesh
time1 = df1["Time"]
Cd1 = df1["Cd"]

#Cd_last1 = Cd1.iloc[-1]
#t_last1 = time1.iloc[-1]

# Medium mesh
time2 = df2["Time"]
Cd2 = df2["Cd"]

#Cd_last2 = Cd2.iloc[-1]
#t_last2 = time2.iloc[-1]

# Fine mesh
time3 = ny_df3["Time"]
Cd3 = ny_df3["Cd"]

#Cd_last3 = Cd3.iloc[-1]
#t_last3 = time3.iloc[-1]


start = 30

# Creating the figure
fig, ax = plt.subplots(1, 3, figsize=(20, 6), constrained_layout=False)
fig.suptitle("Residual convergence check", fontsize=16)

# Plotting the coarse data
ax[0].plot(time1[15:], Cd1[15:], label=rf"$\bar{{C}}$_d")
#ax[0].scatter(t_last1, Cd_last1, color='r', marker='x', label=f"Final: {Cd_last1:.3f}")
ax[0].set_title("p tolerance 1e-6 u tolerance 1e-5")
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Cd")
ax[0].grid(True)
#ax[0].legend()

# Plotting the medium data
ax[1].plot(time2, Cd2, label=rf"$\bar{{C}}$_d")
#ax[1].scatter(t_last2, Cd_last2, color='r', marker='x', label=f"Final: {Cd_last2:.3f}")
ax[1].set_title("p tolerance 1e-7 u tolerance 1e-5")
ax[1].set_xlabel("Time")
ax[1].set_ylabel("Cd")
ax[1].grid(True)
#ax[1].legend()

# Plotting the fine data
ax[2].plot(time3, Cd3, label=rf"$\bar{{C}}$_d")
#ax[2].scatter(t_last3, Cd_last3, color='r', marker='x', label=f"Final: {Cd_last3:.3f}")
ax[2].set_title("p tolerance 1e-7 u tolerance 1e-7")
ax[2].set_xlabel("Time")
ax[2].set_ylabel("Cd")
ax[2].grid(True)

#ax[2].legend()

plt.show()