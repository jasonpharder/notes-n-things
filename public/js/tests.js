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

test("Does the homepage work correctly", function() {
	visit("/")
		.assertElementExists("ul#home-sidebar", "found homepage course sidebar");

	visit("/")
		.assertElementExists("h1#home-header", "found homepage header");

});

test("Does the notes page work correctly", function() {

	visit("/notes")
		.assertElementExists("button#create-note", "found create note button");

	visit("/notes")
		.assertElementExists("div#notes-sidebar", "found notes sidebar");

	visit("/notes")
		.assertElementExists("h1#notes-header", "found notes header");

});

test("Does the courses page work correctly", function(){

	visit("/courses")
		.assertElementExists("ul#courses-sidebar", "found courses sidebar");

	visit("/courses")
		.click("a[href$=\"courseadd\"]")
		.assertElementExists("div#course-container", "add course form successfully loads");

	visit("/courses")
		.assertElementExists("h1#courses-header", "found courses header");
});

test("Does the login page work correctly", function(){

	visit("/login")
		.assertElementExists("form#signin-form", "found login form");

	visit("/login")
		.assertElementExists("input#email-field", "found email field");

	visit("/login")
		.assertElementExists("input#password-field", "found password field");

	visit("/login")
		.assertElementExists("input#remember-checkbox", "found remember me checkbox");

	visit("/login")
		.assertElementExists("button#signin-button", "found signin button");

	visit("/login")
		.assertElementExists("button#register-link", "found register link");

});

test("Does the users page work correctly", function(){

	visit("/users")
		.assertElementExists("ul#users-sidebar", "found users sidebar");

	visit("/users")
		.assertElementExists("h1#users-header", "found users header");

});

