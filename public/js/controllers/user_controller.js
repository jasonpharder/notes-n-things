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

