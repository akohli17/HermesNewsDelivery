import scipy as sp
import numpy as np
import math
import database_handling as dbh

def nonoutliers(user_id):

	times = dbh.f(user_id)
	iqr = sp.iqr(times)
	times_filter = []
	for t in times:
		if (t < 1.5*iqr):
			times_filter.append(t)
	return times_filter

def average_time(user_id):

	times_filter = nonoutliers(user_id)
	return np.mean(times_filter)

def max_nonoutlier(user_id):

	times_filter = nonoutliers(user_id)
	return math.max(times_filter)