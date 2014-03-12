// put app in qunit-fixture
window.App = Ember.Application.create({
  rootElement: '#qunit-fixture'
});

// turn on testing mode
window.App.setupForTesting();

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

test("Does the index template load properly", function() {
	visit("/")
		.find("h3.masthead-brand")
		.then(function(header) {
			equal(header.length, 1, 'found title');
		});
});