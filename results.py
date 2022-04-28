import numpy as np
import matplotlib.pyplot as plt

prefixes = ["25ennuw", "eniuw", "ennuw", "entuw", "enuuw"]
for prefix in prefixes:
  binary_results = np.loadtxt(f'results/{prefix}-binary.dat', dtype=int, delimiter=",")
  accuracy_results = np.loadtxt(f'results/{prefix}-accuracy.dat', dtype=float, delimiter=",")
  concentration_results = np.loadtxt(f'results/{prefix}-concentration.dat', dtype=float, delimiter=",")
  K = binary_results.shape[0]

  binary_results_mean = np.mean(binary_results, axis=1)
  binary_results_variance = np.var(binary_results, axis=1)
  accuracy_results_mean = np.mean(accuracy_results, axis=1)
  accuracy_results_variance = np.var(accuracy_results, axis=1)
  concentration_results_mean = np.mean(concentration_results, axis=1)

  f1 = plt.figure()
  plt.plot(np.arange(1,K+1), binary_results_mean, label="Mean")
  plt.plot(np.arange(1,K+1), binary_results_variance, label="Variance")
  plt.ylim(0,1)
  plt.title(f'{prefix.upper()} Outcome Results')
  plt.xlabel("K")
  plt.ylabel("Win Probability of Correct Alternative")
  plt.legend()
  plt.savefig(f'plots/{prefix.lower()}-binary.png')

  f2 = plt.figure()
  plt.plot(np.arange(1,K+1), accuracy_results_mean, label="Mean")
  plt.plot(np.arange(1,K+1), accuracy_results_variance, label="Variance")
  plt.ylim(0,1)
  plt.title(f'{prefix.upper()} Accuracy Results')
  plt.xlabel("K")
  plt.ylabel("Vote Share of Correct Alternative")
  plt.legend()
  plt.savefig(f'plots/{prefix.lower()}-accuracy.png')

  f3 = plt.figure()
  plt.plot(np.arange(1,K+1), concentration_results_mean)
  plt.ylim(0,1)
  plt.title(f'{prefix.upper()} Concentration Results')
  plt.xlabel("K")
  plt.ylabel("Highest Post-Delegation Voting Weight Share")
  plt.savefig(f'plots/{prefix.lower()}-concentration.png')

  f4, ax = plt.subplots(2, 2)
  plt.suptitle('Correct Votes / Votes Cast')
  ax[0,0].hist(accuracy_results[0])
  ax[0,0].set_title('k = 1')
  ax[0,1].hist(accuracy_results[1])
  ax[0,1].set_title('k = 2')
  ax[1,0].hist(accuracy_results[2])
  ax[1,0].set_title('k = 3')
  ax[1,1].hist(accuracy_results[3])
  ax[1,1].set_title('k = 4')
  plt.subplots_adjust(wspace=0.4, hspace=0.4)
  plt.savefig(f'plots/{prefix.lower()}-histogram.png')