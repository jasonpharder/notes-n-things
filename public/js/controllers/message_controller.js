App.MycourseController = Ember.ArrayController.extend({
        actions: {

                addMessage: function(messageText) {
                        var message = messageText;
                        var currCourse = this.get('currCourse');        

                        console.log(this.get('currCourse'));
                        var messageAdd =this.store.createRecord('message', {
                                message: message,
                                posttime: "12:00pm",
                                courseid: this.get('currCourse'),
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
                        console.log(message);
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
