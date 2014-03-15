App.MycourseController = Ember.ArrayController.extend({

        actions: {
                addMessage: function(messageText) {
                        var message = messageText;
                       
                        var messageAdd =this.store.createRecord('message', {
                                message: message,
                                posttime: '2011-05-16 15:36:38',
                                course: 4,
                                user: 1
                        });
                        messageAdd.save();
                }
        }
});
