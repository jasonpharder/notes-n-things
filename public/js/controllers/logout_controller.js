App.LogoutController = Ember.ObjectController.extend({

        actions: {
                logout: function() {
          		document.cookie  = "username=; expires=Thu, 01 Jan 1970 00:00:00 GMT";
			document.cookie = "userID=; expires=Thu, 01 Jan 1970 00:00:00 GMT";             
        
			document.getElementById('login').style.display = "inline";
			document.getElementById('logout').style.display = "none";
			document.getElementById('currUser').style.display = "none";
			document.getElementById('addCourseBtn').style.display = "none";
			document.getElementById('signout').innerHTML = "You have successfully signed out";
	        }
        }
});
