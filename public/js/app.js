App = Ember.Application.create();

App.Router.map(function() {
  this.resource('notes');
  this.resource('courses');
  this.resource('login');
});

App.NotesRoute = Ember.Route.extend({
	model: function() {
		return [{
			title: "test tile",
			id: '1'
		}, {
			title: "test title 2",
			id: '2'
		}];
	}
});
