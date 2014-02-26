App.Note = DS.Model.extend({
	title: DS.attr('string'),
	uid: DS.attr('string')
})

App.Note.FIXTURES = [
	{
		uid: "1",
		id : 1,
		title: "Test Note"
	},
	{
		uid: "2",
		id : 2,
		title: "Test Note 2"
	},
	{
		uid: "3",
		id : 3,
		title: "Test Note 3"
	},
]