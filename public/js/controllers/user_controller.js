App.UserController = Ember.ObjectController.extend({
	isEditing: false,

  	actions: {
		edit: function() {
			this.set('isEditing', true);
		},

		doneEditing: function() {
			this.set('isEditing', false);
			//var record = this.get('store').createRecord(
			//'user', {
			//  id : 4,
		    //  username: "Fewer Moving Parts",
		    //  password: "asdasdas",
		    //   email: "David Bazan",
		    //   admin: true
		    // });
			var record = this.get('model');
		    record.save();

		    //var post = this.store.find('user', 1);
		    //post.save();
		}
	}
});