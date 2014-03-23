App.CourseaddController = Ember.ObjectController.extend({

        actions: {
                add: function(courseName, courseAltName) {
                        var name = courseName;
                        var altName = courseAltName;
                        var courseAdd =this.store.createRecord('course', {
                                name: name,
                                alt_name: altName,
                                professor: 1 // This need to be the user logged in 
                        });
                        courseAdd.save();
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
