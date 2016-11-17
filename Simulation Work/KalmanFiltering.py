import matplotlib.pyplot as plt
import random
import math

epsilon = 0.01
total_ks = 100

def simpleControl(K, x0, r):
	x = [x0]
	curr = x0
	actual = [x0]

	for i in range(total_ks):
		curr = x[-1]
		if r != 0:
			random_noise = random.uniform(-r, r)
			random_noise2 = random.uniform(-r, r)
		else:
			random_noise = 0
			random_noise2 = 0
		curr -= K*(curr + random_noise) - random_noise2
		x.append(curr)

		actual.append(actual[-1] - K*(actual[-1] + random_noise))
	return actual

def standard_deviation(base, x):
	total_sum = 0
	for i in range(total_ks + 1):
		total_sum += pow(base[i] - x[i], 2)
	return math.sqrt(total_sum/(total_ks + 1))


def kalmanFilter(K, x0, r):
	x = [x0]
	x_k = x0
	state_variance = math.pow(r,2)/3
	measurement_variance = math.pow(r,2)/3

	actual = [x0]

	for i in range(total_ks):
		x_k = x[-1]
		if r != 0:
			random_noise = random.uniform(-r, r)
			random_noise2 = random.uniform(-r, r)
		else:
			random_noise = 0
			random_noise2 = 0



		# A pirori
		z_k = actual[-1] + random_noise
		a_priori = x_k - K*z_k
		kalman_gain = state_variance/(state_variance + measurement_variance)

		actual.append(actual[-1] - K*(z_k))

		# Update Estimate
		x_k = a_priori - kalman_gain*(random_noise2)
		x.append(x_k)
	return(simpleControl(K, x0, r), actual)

if __name__ == "__main__":
	x0 = 100
	K = 0.5
	ks = range(total_ks + 1)
	no_error = simpleControl(K, x0, 0)

	small_error, kalman_small = kalmanFilter(K, x0, 1)
	med_error, kalman_med = kalmanFilter(K, x0, 2.5)
	large_error, kalman_large = kalmanFilter(K, x0, 10)

	sd1 = standard_deviation(no_error, small_error)
	sd2 = standard_deviation(no_error, kalman_small)

	sd3 = standard_deviation(no_error, med_error)
	sd4 = standard_deviation(no_error, kalman_med)

	sd5 = standard_deviation(no_error, large_error)
	sd6 = standard_deviation(no_error, kalman_large)

	print[(sd1, sd2), (sd3, sd4), (sd5, sd6)]

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111)
	ax1.plot(ks, no_error, label='No Variance')
	plt.xlabel("K (# of iterations)")
	plt.ylabel("Distance From Origin")
	plt.title("R = 0")
	ax1.legend()
	
	fig2 = plt.figure()
	ax2 = fig2.add_subplot(111)
	ax2.plot(ks, small_error, color="red", label="Normal")
	ax2.plot(ks, kalman_small, color="blue", label="Kalman Filtered")
	plt.xlabel("K (# of iterations)")
	plt.ylabel("Distance From Origin")
	plt.title("R = 1")
	ax2.legend()

	fig3 = plt.figure()
	ax3 = fig3.add_subplot(111)
	ax3.plot(ks, med_error, color="red", label="Normal")
	ax3.plot(ks, kalman_med, color="blue", label="Kalman Filtered")
	plt.xlabel("K (# of iterations)")
	plt.ylabel("Distance From Origin")
	plt.title("R = 2.5")
	ax3.legend()
	
	fig4 = plt.figure()
	ax4 = fig4.add_subplot(111)
	ax4.plot(ks, large_error, color="red", label="Normal")
	ax4.plot(ks, kalman_large, color="blue", label="Kalman Filtered")
	plt.xlabel("K (# of iterations)")
	plt.ylabel("Distance From Origin")
	plt.title("R = 10")
	ax4.legend()
	
	plt.show()
