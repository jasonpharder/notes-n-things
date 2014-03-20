App.UserController = Ember.ObjectController.extend({
	isEditing: false,

  	actions: {
		edit: function() {
			this.set('isEditing', true);
		},

		doneEditing: function() {
			this.set('isEditing', false);
			
			var record = this.get('model');
		    record.save();
		}
	}
});

App.CreateaccountController = Ember.ObjectController.extend({

	actions: {
		add: function( name, email, password){
			var name = name;
			var email = email;
			var password = password;			

                        var userAdd =this.store.createRecord('user', {
                                username: name,
                                email: email,
                                password: password,
				admin: false
                        });
                        userAdd.save();

		}
	}
});
