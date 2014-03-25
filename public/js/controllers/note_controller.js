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
		createNote: function () {

  		}
	},

	isEditing: false,    
});
