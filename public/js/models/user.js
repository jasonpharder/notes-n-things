App.User = DS.Model.extend({
	uid : DS.attr(),
	username : DS.attr('string'),
	password : DS.attr('string'),
	email : DS.attr('string'),
	admin : DS.attr('boolean')
})