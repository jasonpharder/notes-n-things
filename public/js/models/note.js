App.Note = DS.Model.extend({
	title:   DS.attr('string'),
	uid:     DS.attr('string'),
	content: DS.attr('string')
})

App.Note.FIXTURES = [
	{
		uid:     "1",
		id :     1,
		title:   "Test Note",
		content: "test content"
	},
	{
		uid:     "2",
		id :     2,
		title:   "Test Note 2",
		content: "test content 2"
	},
	{
		uid:     "3",
		id :     3,
		title:   "Test Note 3",
		content: "test content 3"
	},
]