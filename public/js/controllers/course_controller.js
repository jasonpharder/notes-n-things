App.CourseaddController = Ember.ObjectController.extend({
	
        actions: {
                add: function(courseName, courseAltName) {
                        var name = courseName;
                        var altName = courseAltName;
			var cookie = document.cookie;			

			if (cookie.length != 0){
				var cookieUID = cookie.split(';');
				var temp = cookieUID[1].split('=');
				var userID = temp[1];

				var foundCourse = new Boolean();
				foundCourse = false;
			
				var store = this.store;
				var courses = DS.PromiseArray.create({
					promise: this.store.find('course')
				});	

				courses.then(function() {
					var course = "";
					var tempCourseName = "";
					var tempStack = new Array();					
					
					course = courses.get('firstObject');
					course = courses.popObject();
					while (!foundCourse && course != null){
						tempCourseName = course.get('name');

						if (name.localeCompare(tempCourseName) == 0){
							foundCourse = true;
							tempStack.push(course);
						}
						else {
							tempStack.push(course);
							course = courses.popObject();
						}
					}
					var temp = tempStack.pop();
					while (temp != null) {
						courses.pushObject(temp);
						temp = tempStack.pop();
						
					}
					if (foundCourse){
						document.getElementById('coursesMsg').innerHTML = "Course name is already being used";
					}
					else {
        	                        	var courseAdd =store.createRecord('course', {
                	                        	name: name,
		        	                        alt_name: altName,
                			                professor: userID
                                		});
	                                	courseAdd.save();
        	                       		document.getElementById('coursesMsg').innerHTML = "Successfully added course";
					}
				});
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
        subscribe: function() {
            var course = this.get('model');
            var user = this.get('controllers.user.content');
            console.log(user);
            course.get('users').addObject(user);
            course.save();
        },

        unsubscribe: function(){

        }
    }

});
