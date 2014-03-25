App.NotesaddController = Ember.ObjectController.extend({
    actions: {
        add: function(noteName) {
            var name   = noteName;
			var cookie = document.cookie;			

			if (cookie.length != 0) {
				if(noteName.length <= 30) {
    				var cookieUID = cookie.split(';');
					var temp      = cookieUID[1].split('=');
					var userID    = temp[1];
			
    				var store = this.store;
					var notes = DS.PromiseArray.create({
						promise: this.store.find('note')
					});	

					notes.then(function() {
		                var courseAdd = store.createRecord('course', {
                    		name:      name,
	    	                alt_name:  altName,
	        			    professor: userID
        				});

            			courseAdd.save();
                   		document.getElementById('notesMsg').innerHTML = "Successfully added note";
					});
				} else {
					document.getElementById('notesMsg').innerHTML = "Course name has to be 30 or less characters long";
				}
			} else {
				document.getElementById('notesMsg').innerHTML = "Please register or signin to create a Note";
			}
        }
    }
});

App.NotesController = Ember.ArrayController.extend({
	actions: {
		editNote: function () {
    		this.set('isEditing')
		},
		doneEditing: function() {
			this.set('isEditing', false);
			//var record = this.get('model');
		    //record.save();
		},
		createNote: function (title, course) {
			var cookie = document.cookie;

            if (cookie.length != 0) {
				var cookieUID = cookie.split(';');
	            var temp = cookieUID[1].split('=');
	            var userID = temp[1];	

	            if (userID != '1') {
	            	var notes = DS.PromiseArray.create({
						promise: this.store.find('note')
					});

	            	var note = this.store.createRecord('note', {
	            		file_name: title,
	            		owner: userID
	                });

        	        note.save();
            	} else {
					document.getElementById('errorMsg').innerHTML = "Guests can not create notes";
				}
			} else {
                console.log("Cannot add message: currently not logged in");
	            document.getElementById('errorMsg').innerHTML = "Guests can not create notes";
            }
  		}
	},

	isEditing: false,    
});
