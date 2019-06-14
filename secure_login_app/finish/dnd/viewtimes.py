import math
import user_distribution as ud

tau_1 = 20 # first threshold in minutes
tau_2 = 60 # second threshold in minutes
phi = 1.2

def last_in_session(time):

	global tau_1
	return time > tau_1

def last_in_session_maybe_read(time):

	global tau_2
	return time < tau_2

def record_time(time, user_id):

	if not last_in_session:
		return time

	if last_in_session_maybe_read:

		global phi
		return phi*ud.average_time(user_id)

	return average_time(user_id)

def filter_outliers(user_id):

	return math.min(time, ud.max_nonoutlier(user_id))
