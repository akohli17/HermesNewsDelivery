-=Weekly Progress DND Team=-

#########################################################################################################

* Week of: 22nd October - 26th October

* Contribution by: Ruben Dicker
* Brief Description: news.py

#########################################################################################################

* Week of: 29th October - 4th November

* Contribution by: Matteo Russo
* Brief Description: Skeleton Website Implementation

* Reference: This is the tailored-to-our-purposes code that accompanies the video here: https://www.youtube.com/watch?v=8aTnmsDMldY

* Implements the Skeleton App in the Flask Web Framework (better than Bottle as it has better tutorials on the web):

	- Secure User Database (Enrypted Passwords) with both Login and Register.
	- Navigation Bar which you can see at the top of the web page.
	- Skeleton UI with different buttons and the initial screen.
	- Dashboard: type on the searchbar http://127.0.0.1:5000/dashboard once you have registered and logged in.

* I will explain the pieces of code following so that everyone is on the same page (but watch the video above for a much better and extensive explanation of the components):

	- The 'finished' directory has the code the video with which I tailored to our scopes: thus, please cd finished.
	- In app.py you will see functions that have decorators right above them: those reference html files which are stored in the templates folder. You will see that those html files are really rudimentary and linked to equally rudimentary CSS files in the static folder. Feel free to modify them as you like (not a priority but I admit they are ugly).
	- The "class User(UserMixin, db.Model)" on line 26 of app.py references the fields of the table in the database.db (do not care about user.sqlite).

* I thought about these next steps with this priority so that we make a great prototype:

	1) Link the website to the NewsApi database (this has the uttermost priority):
		* Once someone logs in, make a screen with the username of the user and output a page with one piece of news (it can be random or if you want to implement some more logic, please go ahead).
		* The same page has to have the history of what this user has looked for with the respective statistics in terms of view time (if we manage), topic (sports, fashion, politics, etc.) and others.
	2) Deploying the app to Heroku (very important for the prototype): lots of tutorials on youtube, such as https://www.youtube.com/watch?v=skc-ZEU9kO8, https://www.youtube.com/watch?v=p5RMfAp9YYw and https://www.youtube.com/watch?v=jXMHB-DNtIY&t=38s. 
	3) Create a better looking user interface (we can do this later on but I have some ideas, so, before proceeding let us discuss those once we are together).

#########################################################################################################

* Week of: 4th November - 11th November

* Contribution by: Georgy Noarov
* Brief Description: Enhanced Skeleton Website Implementation with connection to the news database

* Enhances the Skeleton App as follows:

	- After the login, the app asks the user to input his/her interest (singular for the moment being).
	- The user database saves the interest corresponding to the respective user.
	- Whenever the user logs in, the website displays the news of the user's interest sorted by popularity. 

* I thought about these next steps with this priority so that we make a great prototype:

	1) Deploying the app to Heroku (very important for the prototype): lots of tutorials on youtube, such as https://www.youtube.com/watch?v=skc-ZEU9kO8, https://www.youtube.com/watch?v=p5RMfAp9YYw and https://www.youtube.com/watch?v=jXMHB-DNtIY&t=38s.
	2) Improve this link between the website to the NewsApi database as follows:
	   * The same page has to have the history of what this user has looked for with the respective statistics in terms of view time (if we manage), topic (sports, fashion, politics, etc.) and others.
	3) Create a better looking user interface (as above, before proceeding let us discuss those once we are together).

#########################################################################################################