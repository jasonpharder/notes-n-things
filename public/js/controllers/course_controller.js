App.CourseaddController = Ember.ObjectController.extend({
	
        actions: {
                add: function(courseName, courseAltName) {
                        var name = courseName;
                        var altName = courseAltName;

			var cookie = document.cookie;			
			
			if (cookie.length != 0){
				var courseAdd =this.store.createRecord('course', {
                                	name: name,
                                	alt_name: altName,
                               		professor: 1 // This need to be the user logged in 
                        	});
                        	courseAdd.save();
				document.getElementById('coursesMsg').innerHTML = "Successfully added course";
			}
			else {
				document.getElementById('coursesMsg').innerHTML = "Please register or signin to create a course";
			}
                }

        }
});

App.CourseController = Ember.ObjectController.extend({
	needs: "user",
	actions: {
		subscribe: function(){
			console.log(this.get('name'));
			//var course = this.get('model');

			console.log(this.get('users'));

			var users = this.get('users');

			users.addObject(this.get("controllers.user.content"));
			this.set('users', users);

			this.save();

			//console.log(userList);
                },

		unsubscribe: function(){

		}
	}

});
