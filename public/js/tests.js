module("Testing the homepage", {
	setup: function() {
		App.reset();
		App.injectTestHelpers();
	}
});

test("App Instantiation", function() {
	equal(
		App.constructor, Ember.Application,
		'App is an Ember App!'
	);
});

test("Do the templates load correctly", function() {
	visit("/")
		.find("ul#course-list")
		.then(function(header) {
			equal(header.length, 1, 'found contents');
		});
	visit("/notes")
		.find("ul#notes-list")
		.then(function(list) {
			equal(list.length, 1, 'found notes list');
		});
	visit("/courses")
		.find("ul#courses-list")
		.then(function(list) {
			equal(list.length, 1, 'found courses list');
		});
	visit("/login")
		.find("form.form-signin")
		.then(function(form) {
			equal(form.length, 1, 'found login');
		});
	visit("/users")
		.find("ul#user-list")
		.then(function(list) {
			equal(list.length, 1, 'found user list');
		});
});
