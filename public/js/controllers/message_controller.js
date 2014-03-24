App.MycourseController = Ember.ArrayController.extend({
        currCourse : -1,

        actions: {

                addMessage: function(messageText) {
                        var message = messageText;
                        var currCourse = this.get('currCourse');

                        var messageAdd =this.store.createRecord('message', {
                                message: message,
                                posttime: "12:00pm",
                                courseid: 4,
                                userid: 1
                        });

                        messageAdd.save();
                }
        }

});

App.MessageController = Ember.ObjectController.extend({
        needs: 'message',

        actions: {

                addComment: function(commentText) {
                        var comment = commentText;
                        var message = this.get('controllers.message.content');

                        var commentAdd =this.store.createRecord('comment', {
                                comment: comment,
                                posttime: "12:00pm",
                                messageid: parseInt(message.get('id')),
                                userid: parseInt(message.get('userid'))
                        });

                        commentAdd.save();
                        message.get('comments').addObject(commentAdd);
                }
        }

});
