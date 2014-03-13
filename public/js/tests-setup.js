// put app in qunit-fixture
window.App = Ember.Application.create({
  rootElement: '#qunit-fixture'
});

// turn on testing mode
window.App.setupForTesting();