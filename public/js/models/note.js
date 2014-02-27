App.Note = DS.Model.extend({
	title:    DS.attr('string'),
	uid:      DS.attr('string'),
	contents: DS.attr('string')
})

App.Note.FIXTURES = [
	{
		uid:      "1",
		id :      1,
		title:    "Test Note",
		contents: "test content"
	},
	{
		uid:      "2",
		id :      2,
		title:    "Test Note 2",
		contents: "test content 2"
	},
	{
		uid:      "3",
		id :      3,
		title:    "Test Note 3",
		contents: "test content 3"
	},
]